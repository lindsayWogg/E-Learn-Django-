# 
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.views import generic
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.hashers import check_password
# 
from django.template.loader import render_to_string
from weasyprint import HTML
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *
import random
import string
from django.contrib import messages
from django.contrib.auth import authenticate, login as loginUser, update_session_auth_hash
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
import io
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.urls import reverse
import json
from time import time
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from edureka.settings import *
import razorpay
from collections import defaultdict
import calendar
from datetime import datetime
from django.shortcuts import render
# import logging
#client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))
client = razorpay.Client(auth=('46', 'secret'))
# Create your views here.

def home(request):
    part = partenaires.objects.all()
    formations = formation.objects.filter(formation_type='payant')
    
    prog=formation.objects.filter(formation_type='gratuit')
    for item in prog:
        item.short_descr = ' '.join(item.formation_descr.split()[:11])
    for item in formations:
        item.short_descr = ' '.join(item.formation_descr.split()[:11])
    collabos=collabo.objects.all()
    return render(request, 'webadmin/nfablog.html', {'part': part, 'formations': formations, 'prog':prog, 'collabos':collabos})





@login_required
def prifile_view(request):
        user_logged=get_user_logged(request)
        formations=souscription_formation.objects.select_related('formation_id', 'matricule').filter(matricule=user_logged.matricule)
        return render(request,'users/nfa-profile.html',{'user_logged':user_logged,"formations":formations})
    
@login_required
def update_activity(request):
    user_logged=get_user_logged(request)
    choice=request.POST['optionsRadios']
    utilisateur.objects.filter(matricule=user_logged.matricule).update(activitys=choice)
    return redirect('view_profile')

@login_required
def update_user_password(request):
    user_logged=get_user_logged(request)
    current_user=User.objects.get(id=user_logged.matricule)
    old_password=request.POST['old_pwd']
    current_pwd=current_user.password
    new_pwd1=request.POST['new_pwd1']
    new_pwd2=request.POST['new_pwd2']
    print(f"""
          old pwd:{current_pwd}
          old inserted:{old_password}
          new_pwd1:{new_pwd1}
          new_pwd2:{new_pwd2}
          """)
    if check_password(old_password, current_pwd):
        if new_pwd1==new_pwd2:
            current_user.set_password(new_pwd2)
            current_user.save()
            messages.success(request,("Modification effectuée avec succès!!!.Vous devez vous reconnecter pour continuer."))
            return redirect('logout')    
            
        else:
            messages.error(request,("Modification non-effectuée!!!Veuillez confirmer le nouveau mot de passe."))
            return redirect('view_profile')
    else:
        messages.error(request,("Modification non-effectuée!!! Veuillez vérifier l'ancien mot de passe."))
        return redirect('view_profile')

@login_required
def update_profile_picture(request):     
    user_logged=get_user_logged(request)
    new_profile_pic = request.FILES.get('new_pdp')
    # upload file
    if new_profile_pic:
            upload_path = os.path.join(settings.MEDIA_ROOT, 'media', 'profile_pic')
            os.makedirs(upload_path, exist_ok=True)
            with open(os.path.join(upload_path, new_profile_pic.name), 'wb+') as destination:
                print(f"*******DESTINATIONN: {destination}")
                for chunk in new_profile_pic.chunks():
                    destination.write(chunk)
            new_path= os.path.join('media', 'profile_pic', new_profile_pic.name)
            utilisateur.objects.filter(matricule=user_logged.matricule).update(profile_pic=new_path)
    print(f"""
          NEW PICTURE :{new_profile_pic}
          NEW PICTURE PATH:{new_path}
            
          """)
    # end upload path
    messages.success(request,("Modification effectuée avec succès!!!"))
    return redirect('view_profile')
    
    
    
@login_required
def update_user_information(request):
    user_logged=get_user_logged(request)
    nom=request.POST['name']
    prenom=request.POST['prenom']
    adress=request.POST['adress']
    phone=request.POST['phone']
    email=request.POST['email']
    skype=request.POST['skype']
    matricule=request.POST['matricule']
    login=request.POST['username']
    organization=request.POST['organisation']
    sexe=request.POST['sex']
        
    print(f"""
          INFORMATIONS RECUPÉRÉ
          ID:{user_logged.matricule}
          Nom:{nom}
          Prenom: {prenom}
          Adresse:{adress}
          phone:{phone}
          email:{email}
          skype:{skype}
          """)
    utilisateur.objects.filter(matricule=matricule).update(sex=sexe,username=login,organisation=organization,first_name=nom,last_name=prenom,adress=adress,phone=phone,email=email,skype=skype)
    User.objects.filter(id=user_logged.matricule).update(first_name=nom,last_name=prenom,email=email)
    messages.success(request,("Modification effectuée avec succès!!!."))
    
    if user_logged.user_type=='student':
        return redirect('view_profile')
    elif user_logged.user_type=='admin':
        return redirect('gestion_utilisateurs')




def sendmessage(request):
    client=request.POST['sender']
    email=request.POST['email']
    phone=request.POST['phone']
    content=request.POST['message']
    # Message(sender=client, email=email, phone=phone, content=content).save()  
    # Message.objects.create(sender=client, email=email, phone=phone, content=content, date=datetime.today())
    email_address = 'nextfoodafricamg@gmail.com'
    email_password = 'ivyz bbjd rvfa rkym '
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    to_email = 'nextfoodafricamg@gmail.com'
    message = MIMEMultipart()
    message['From'] = email_address
    message['To'] = to_email
    message['Subject'] = f'Message de {client}'
    message_text=f"""
        ***********
        From : {client}
        At : {datetime.today()}
        Email : {email}
        Phone : {phone}
        ***********
        Content:
        {content}

    """
    message.attach(MIMEText(message_text, 'plain'))
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(email_address, email_password)

        # Envoyer l'e-mail
        server.sendmail(email_address, to_email, message.as_string())
        print('E-mail envoyé avec succès !')

    except Exception as e:
        print('Erreur lors de l\'envoi de l\'e-mail :', str(e))

    finally:
        # Fermer la connexion SMTP
        server.quit()
    return redirect('nfablog')

def subscription_request(request):
    if request.method=="POST":
        data=demande_inscription(
            formation_id=request.POST['formation_id'], 
            email=request.POST['email'], 
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            sex=request.POST['sex'],
            adress=request.POST['adress'],
            phone=request.POST['phone'],
            username=request.POST['username'],
            password=request.POST['password1']
        )
        data.save()
        messages.success(request,("<b>Félicitation!!! Votre de mande d'inscription a bien été enregistré!</b> <br>Vous serez notifié par E-mail après la validation de votre demande."))
        return redirect('nfablog')

def join_formation(request):
    if request.method=="POST":
        already_signed_up=request.POST['already_signed_up']
        if already_signed_up=='Yes':
            user_identity=utilisateur.objects.get(
                username=request.POST['username'],
            email=request.POST['username'], 
            phone=request.POST['phone']
            )
            data=demande_inscription(
            formation_id=request.POST['formation_id'],
            email=user_identity.email(),
            first_name=user_identity.first_name(),
            last_name=user_identity.last_name(),
            sex=user_identity.sex(),
            adress=user_identity.adress(),
            phone=user_identity.phone(),
            username=user_identity.username(),
            password=user_identity.password()
            )
        elif already_signed_up=='No':
            subscription_request(request)
            
def subscribe_course_already_signed_up(request):
    if request.method=="POST":
        print("REQUEST METHOD: POST")
        username=request.POST['username']
        phone=request.POST['phone']
        email=request.POST['email']
        formation_id=request.POST['formation_id']
        customer=utilisateur.objects.get(email=email,phone=phone,username=username)
        print(f"USER INFORMATIONS: {customer.last_name} {customer.first_name}")
        data=demande_inscription(
            formation_id=formation_id, 
            matricule=customer.matricule,
            email=email,
            first_name=customer.first_name,
            last_name=customer.last_name,
            sex =customer.sex,
            adress=customer.adress,
            phone=phone,
            username=username,
            already_signed_up='Yes'
        )
        data.save()
        messages.success(request, ("Votre demande a bien été enregistré."))
        return redirect('nfalogin')
        
def register(request):
    if request.method=="POST":
        print("REQUEST METHOD: POST")
        data=demande_inscription(
            formation_id=request.POST['formation_id'], 
            email=request.POST['email'], 
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            sex=request.POST['sex'],
            adress=request.POST['adress'],
            phone=request.POST['phone'],
            username=request.POST['username'],
        )
        data.save()
        messages.success(request,("Félicitation!!! Votre de mande d'inscription a bien été enregistré! Vous serez notifié par E-mail après la validation de votre demande."))
        return redirect('subscribe_course')
        # form=RegisterUserForm(request.POST)
        # if form.is_valid():
            # user=form.save()
            # print(f"""
            #       USERNAME:{form.cleaned_data['username']}
            #       PASSWORD1:{form.cleaned_data['password1']}
            #       PASSWORD2:{form.cleaned_data['password2']}
            #       """)
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password1']
            # data=utilisateur(
            #     email=form.cleaned_data['email'],
            #     first_name=form.cleaned_data['first_name'],
            #     last_name=form.cleaned_data['last_name'],
            #     sex=form.cleaned_data['sex'],
            #     adress=form.cleaned_data['adress'],
            #     phone=form.cleaned_data['phone'],
            #     username=form.cleaned_data['username'],
            #     password=form.cleaned_data['password1']
            # )
            # data.save()
            # user=authenticate(username=username,password=password)
            
            # login(request,user,backend='django.contrib.auth.backends.ModelBackend')
            # messages.success(request,("registration successfull"))
            # return redirect('dashboard')
        
    else:
        print("REQUEST METHOD: GET")
        form = RegisterUserForm()
        form.fields['last_name'].widget.attrs['class'] = "form-control"
        form.fields['first_name'].widget.attrs['class'] = "form-control"
        form.fields['email'].widget.attrs['class'] = "form-control"
        SEX_CHOICES = [
        ('H', 'Homme'),
        ('F', 'Femme'),
    ]
        form.fields['sex'] = forms.ChoiceField(choices=SEX_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
        form.fields['adress'].widget.attrs['class'] = "form-control"
        form.fields['phone'].widget.attrs['class'] = "form-control"
        form.fields['username'].widget.attrs['class'] = "form-control"
        form.fields['password1'].widget.attrs['class'] = "form-control"
        form.fields['password2'].widget.attrs['class'] = "form-control"
        
        form.fields['first_name'].widget.attrs['placeholder'] = "Prénom(s)"
        form.fields['last_name'].widget.attrs['placeholder'] = "Nom"
        form.fields['email'].widget.attrs['placeholder'] = "email"
        form.fields['adress'].widget.attrs['placeholder'] = "Votre adresse"
        form.fields['phone'].widget.attrs['placeholder'] = "Numéro de téléphone"
        form.fields['username'].widget.attrs['placeholder'] = "Nom d'utilisateur"
        form.fields['password1'].widget.attrs['placeholder'] = "Votre mot de passe"
        form.fields['password2'].widget.attrs['placeholder'] = "Merci de confirmer votre mot de passe"
        
    return render(request,'webadmin/nfa-signup.html',{'form':form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']    
        password = request.POST['password']    
        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            login(request, user)    
            user_logged=get_user_logged(request)
            print(f"USER TYPE: {user_logged.user_type}")
            if user_logged.user_type=='student':
                return redirect('dashboard')
            elif user_logged.user_type=='admin':
                return redirect('admin_dashboard')
        else:
            messages.success(request, (" Nom d'utilisateur ou mot de passe incorrect. Veuillez réessayer"))
            return redirect('nfalogin')

    else:
        
        return render(request, 'webadmin/nfa-login.html')


def get_user_logged(req):
    user_logged=req.user
    id=user_logged.id
    user_logged=utilisateur.objects.get(matricule=id)
    print(f"""
          Firstname:{user_logged.first_name}
          """)
    return user_logged

@login_required
def dashboard(request):
    user_logged=get_user_logged(request)
    prog=formation.objects.all()
    for item in prog:
        item.short_descr = ' '.join(item.formation_descr.split()[:20])
    return render(request, 'users/nfa-student-dashboard.html',{'prog': prog,'user_logged':user_logged})

@login_required
def dashboard2(request):
    user_logged=get_user_logged(request)
    prog=formation.objects.all()
    for item in prog:
        item.short_descr = ' '.join(item.formation_descr.split()[:20])
    return render(request, 'users/nfa-dashboard.html',{'prog': prog,'user_logged':user_logged})


@login_required
def calendar_view(request):
    user_logged=get_user_logged(request)
    today = datetime.today()
    year = today.year
    month = today.month
    cal = calendar.Calendar(firstweekday=0)
    month_days = cal.monthdayscalendar(year, month)

    ateliers = Atelier.objects.all()

    return render(request, 'users/nfa-calendar.html', {
        'user_logged':user_logged,
        'month_days': month_days,
        'ateliers': ateliers,
    })

def advanced_calendar_view(request):
    today = datetime.today()
    user_logged = get_user_logged(request)

    # Obtenir le mois et l'année depuis les paramètres GET, sinon utiliser le mois courant
    year = int(request.GET.get('year', today.year))
    month = int(request.GET.get('month', today.month))

    # Calculer les mois précédent et suivant
    previous_month = month - 1
    previous_year = year
    if previous_month < 1:
        previous_month = 12
        previous_year -= 1

    next_month = month + 1
    next_year = year
    if next_month > 12:
        next_month = 1
        next_year += 1

    # Nom du mois pour l'affichage
    month_name = calendar.month_name[month]

    # Générer les jours du mois
    cal = calendar.Calendar(firstweekday=0)
    month_days = cal.monthdayscalendar(year, month)

    # Récupérer les ateliers de la base de données
    ateliers = Atelier.objects.filter(date_debut__month=month, date_debut__year=year)
    formations = formation.objects.filter(created_at__month=month, created_at__year=year)

    # Récupérer les souscriptions aux ateliers
    list_souscription_ateliers = Souscription_atelier.objects.select_related('atelier_id', 'matricule').filter(matricule=user_logged.matricule)

    # Récupérer les souscriptions aux formations
    list_souscription_formations = souscription_formation.objects.select_related('formation_id', 'matricule').filter(matricule=user_logged.matricule)

    # Créer la liste des ateliers avec le statut d'inscription
    ateliers_with_subscription_status = []
    for atelier in ateliers:
        is_subscribed = list_souscription_ateliers.filter(atelier_id=atelier).exists()  # Vérifie si l'utilisateur est inscrit
        atelier_dict = {
            'atelier': atelier,  # L'atelier complet avec tous ses attributs
            'is_subscribed': is_subscribed  # Ajout du statut d'inscription
        }
        ateliers_with_subscription_status.append(atelier_dict)

    # Créer la liste des formations avec le statut d'inscription
    formations_with_subscription_status = []
    for formation_item in formations:
        is_subscribed = list_souscription_formations.filter(formation_id=formation_item).exists()  # Vérifie si l'utilisateur est inscrit
        formation_dict = {
            'formation': formation_item,  # La formation complète avec tous ses attributs
            'is_subscribed': is_subscribed  # Ajout du statut d'inscription
        }
        formations_with_subscription_status.append(formation_dict)

    # Affichage pour vérification
    for item in ateliers_with_subscription_status:
        print(f"""
            Atelier: {item['atelier'].titre}
            Lieu: {item['atelier'].lieu}
            Date début: {item['atelier'].date_debut}
            Inscrit: {item['is_subscribed']}""")

    for item in formations_with_subscription_status:
        print(f"""
            Formation: {item['formation'].formation_name}
            Description: {item['formation'].formation_descr}
            Description: {item['formation'].created_at}
            Inscrit: {item['is_subscribed']}""")

    return render(request, 'users/nfa-calendar-advanced.html', {
        'month_days': month_days,
        'month_name': month_name,
        'year': year,
        'previous_month': previous_month,
        'previous_year': previous_year,
        'next_month': next_month,
        'next_year': next_year,
        'user_logged': user_logged,
        'ateliers_with_subscription_status': ateliers_with_subscription_status,
        'formations_with_subscription_status': formations_with_subscription_status,
    })


def logout_user(request):
    logout(request)
    messages.success(request,("Vous avez été déconnecté(e)."))
    return redirect('nfalogin')

@login_required
def show_free_formation(request,formation_id):
    user_logged=get_user_logged(request)
    free_formation=formation.objects.get(formation_id=formation_id)
    chapitres=chapitre.objects.filter(frmt_id=formation_id).order_by('chap_id')
    chapitres_with_notes = chapitres.prefetch_related('notes_set')
    video_chaps=Video_chap.objects.filter(formation_id=formation_id)
    quizz=Question.objects.all()
    prev_ch_done = False
    next_ch_to_do = True
    chapitres_with_status = []
    counter=0
    nb_done=0
    progress=0
    nb_chap=len(chapitres_with_notes)
    for ch in chapitres_with_notes:
        notes_exist = ch.notes_set.exists()
        counter+=1
        ch.num=counter
        if not notes_exist:
            ch.status = "to do" if next_ch_to_do else "waiting"
            next_ch_to_do = False
        else:
            note = ch.notes_set.first()
            if note.note >= 50:
                ch.status = "done"
                prev_ch_done = True
                next_ch_to_do = True
                nb_done+=1
            else:
                ch.status = "waiting" if prev_ch_done else "to do"
                prev_ch_done = False
                next_ch_to_do = False
        
        chapitres_with_status.append({'chapitre': ch, 'status': ch.status,'num':ch.num})
        
    for ch_with_status in chapitres_with_status:
        print(f"Chapitre : {ch_with_status['chapitre'].titre}, Statut : {ch_with_status['status']}")
    if nb_chap>0:
        progress=(nb_done*100)/nb_chap

    return render(request,'users/nfa-formation.html'
                  ,{
                      'formation':free_formation
                    ,'chap':chapitres
                    ,'notes':chapitres_with_notes
                    ,'chapitres_with_status':chapitres_with_status
                    ,'user_logged':user_logged
                    ,'video_chaps': video_chaps
                    ,'progress':round(progress,1)
                    ,'quizz':quizz
                    })

@login_required
def show_chapter(request,chap_id,frmt_id):
    user_logged=get_user_logged(request)
    chapitres=chapitre.objects.get(chap_id=chap_id,frmt_id=frmt_id)
    objectifs=objectif.objects.filter(chap_id=chap_id,frmt_id=frmt_id).order_by('objctf_id')
    quizz_with_answers = []
    quizz = Question.objects.select_related('formation_id').filter(chap_id=chap_id)
    counter=0
    for question in quizz:
        counter+=1
        # Récupération des réponses possibles pour chaque question
        answers = Answer_possible.objects.filter(question_id=question.question_id)
        quizz_with_answers.append({'id':counter,'question': question, 'answers': answers})
    return render(request,'users/nfa-chapitre.html',{'chap':chapitres,'objectifs':objectifs, 'quizz_with_answers': quizz_with_answers ,'user_logged':user_logged})

@login_required
def show_quizz(request,chap_id,frmt_id):
    user_logged=get_user_logged(request)
    chapitres=chapitre.objects.get(chap_id=chap_id,frmt_id=frmt_id)
    quizz_with_answers = []
    quizz = Question.objects.select_related('formation_id').filter(chap_id=chap_id)
    counter=0
    for question in quizz:
        counter+=1
        # Récupération des réponses possibles pour chaque question
        answers = Answer_possible.objects.filter(question_id=question.question_id)
        quizz_with_answers.append({'id':counter,'question': question, 'answers': answers})
    return render(request,'users/nfa-quizz.html',{'chap':chapitres,'quizz_with_answers': quizz_with_answers ,'user_logged':user_logged})


@login_required
def validate_quizz(request):
    user_logged=get_user_logged(request)
    frmt_id=request.POST['formation_id'] 
    chap_id=request.POST['chap_id'] 
    chapitres=chapitre.objects.get(chap_id=chap_id,frmt_id=frmt_id)
    objectifs=objectif.objects.filter(chap_id=chap_id,frmt_id=frmt_id).order_by('objctf_id')
    quizz_with_answers = []
    quizz = Question.objects.select_related('formation_id').filter(chap_id=chap_id)
    counter=0
    for question in quizz:
        counter+=1
        answers = Answer_possible.objects.filter(question_id=question.question_id)
        quizz_with_answers.append({'id':counter,'question': question, 'answers': answers})
    reponse=None
    nb_question=len(quizz_with_answers)
    nb_true_answers=0
    note_prctg=0
    for qa in quizz_with_answers:
        print("#############################################")
        print(f"Chapitre: {chapitres.frmt_id} {chapitres.chap_id}")
        print(f"Name:{chapitres.frmt_id}_{chapitres.chap_id}_{qa['question'].question_id}")
        name=f"{chapitres.frmt_id}_{chapitres.chap_id}_{qa['question'].question_id}"
        print(f"Question ID: {qa['id']}")
        print(f"Question Text: {qa['question'].question_text}")
        print(f"reponses attendus: {qa['question'].answers}")
        print(f"Réponses de l'utilisateur:{request.POST.getlist(name) }")
        if qa['question'].answers==request.POST.getlist(name):
            reponse='Vrai'
            nb_true_answers+=1
        else:
            reponse='Faux'
        print(f"Resultat:{reponse}")
        print("Answers possibles:")
        for answer in qa['answers']:
            print(f"Answer {answer.answer_alias}: {answer.answer_text}")
    note_prctg=(nb_true_answers*100)/nb_question
    print(f"Note:{note_prctg}%")
    note, cree = Notes.objects.update_or_create(
    matricule_id=user_logged.matricule,
    formation_id=formation.objects.get(formation_id=frmt_id),
    chap_id=chapitre.objects.get(chap_id=chap_id,frmt_id=frmt_id),
    defaults={'note': note_prctg}
)
    if note_prctg >=50:
        messages.success(request,f'Félicitaion, vous avez eu {note_prctg}% sur le quizz!!! Vous pouvez passer au chapitre suivant.')
    else:
        messages.error(request,f"Dommage, vous avez eu {note_prctg}%, vous devez repasser le quizz!")
    return render(request,'users/nfa-chapitre.html',{'chap':chapitres,'objectifs':objectifs, 'quizz_with_answers': quizz_with_answers})

    

    



def view_pdf(request,pdf_path):
    # Chemin vers votre fichier PDF
    chemin_vers_pdf = os.path.join(settings.BASE_DIR, pdf_path)
    
    # Ouverture et lecture du fichier PDF
    with open(chemin_vers_pdf, 'rb') as f:
        pdf = f.read()
    
    # Création de la réponse HTTP
    response = HttpResponse(pdf, content_type='application/pdf')
    
    # Configuration des en-têtes pour permettre l'affichage dans une iframe ou un embed
    response['Content-Disposition'] = 'inline; filename="votre_fichier.pdf"'
    response['X-Frame-Options'] = 'ALLOW-FROM *'
    
    return response


@login_required
def update_formation_presentation(request):
    user_logged=get_user_logged(request)
    formation_id=request.POST['formation_id'] 
    current_formation=formation.objects.filter(formation_id=formation_id).update(
        formation_presentation=upload_file(request.FILES.get('formation_presentation'),'presentations')
    )
    formt=formation.objects.get(formation_id=request.POST.get('formation_id'))
    chap=chapitre.objects.filter(frmt_id=request.POST.get('formation_id'))
    counter=0
    for ch in chap:
        counter+=1
        ch.num=counter
    video_chaps=Video_chap.objects.filter(formation_id=request.POST.get('formation_id'))
    messages.success(request,("Modification effectuée avec susscès"))
    return render(request, 'administration/edit_formation.html',{'formt':formt,'chap':chap,'video_chaps': video_chaps})
 
@login_required
def update_course_content(request):
    user_logged=get_user_logged(request)
    video_id=request.POST['video_id'] 
    current=Video_chap.objects.filter(video_id=video_id).update(
        cours_content=upload_file(request.FILES.get('cours_content'),'course')
    )
    formt=formation.objects.get(formation_id=request.POST.get('formation_id'))
    chap=chapitre.objects.filter(frmt_id=request.POST.get('formation_id'))
    counter=0
    for ch in chap:
        counter+=1
        ch.num=counter
    video_chaps=Video_chap.objects.filter(formation_id=request.POST.get('formation_id'))
    messages.success(request,("Modification effectuée avec susscès"))
    return render(request, 'administration/edit_formation.html',{'formt':formt,'chap':chap,'video_chaps': video_chaps})


@login_required
def update_chapter_presentation(request):
    user_logged=get_user_logged(request)
    chap_id=request.POST['chap_id'] 
    current_formation=chapitre.objects.filter(chap_id=chap_id).update(
        cours_content=upload_file(request.FILES.get('cours_content'),'course')
    )
    formt=formation.objects.get(formation_id=request.POST.get('formation_id'))
    chap=chapitre.objects.filter(frmt_id=request.POST.get('formation_id'))
    counter=0
    for ch in chap:
        counter+=1
        ch.num=counter
    video_chaps=Video_chap.objects.filter(formation_id=request.POST.get('formation_id'))
    messages.success(request,("Modification effectuée avec susscès"))
    return render(request, 'administration/edit_formation.html',{'formt':formt,'chap':chap,'video_chaps': video_chaps})
 
  
@login_required
def update_chapter_name(request):
    user_logged=get_user_logged(request)
    chap_id=request.POST['chap_id'] 
    current_formation=chapitre.objects.filter(chap_id=chap_id).update(
        titre=request.POST.get('new_name')
    )
    formt=formation.objects.get(formation_id=request.POST.get('formation_id'))
    chap=chapitre.objects.filter(frmt_id=request.POST.get('formation_id')).order_by('chap_id')
    counter=0
    for ch in chap:
        counter+=1
        ch.num=counter
    video_chaps=Video_chap.objects.filter(formation_id=request.POST.get('formation_id'))
    messages.success(request,("Modification effectuée avec susscès"))
    return render(request, 'administration/edit_formation.html',{'formt':formt,'chap':chap,'video_chaps': video_chaps})
 
@login_required
def update_course_name(request):
    user_logged=get_user_logged(request)
    video_id=request.POST['video_id'] 
    current=Video_chap.objects.filter(video_id=video_id).update(
        titre=request.POST.get('new_name')
    )
    formt=formation.objects.get(formation_id=request.POST.get('formation_id'))
    chap=chapitre.objects.filter(frmt_id=request.POST.get('formation_id')).order_by('chap_id')
    counter=0
    for ch in chap:
        counter+=1
        ch.num=counter
    video_chaps=Video_chap.objects.filter(formation_id=request.POST.get('formation_id'))
    messages.success(request,("Modification effectuée avec susscès"))
    return render(request, 'administration/edit_formation.html',{'formt':formt,'chap':chap,'video_chaps': video_chaps})


  
  
@login_required
def delete_chapter(request):
    user_logged=get_user_logged(request)
    formation_id=request.POST['formation_id'] 
    cur_chap=chapitre.objects.get(chap_id=request.POST['chap_id'] )
    cur_chap.delete()
    formt=formation.objects.get(formation_id=request.POST.get('formation_id'))
    chap=chapitre.objects.filter(frmt_id=request.POST.get('formation_id'))
    counter=0
    for ch in chap:
        counter+=1
        ch.num=counter
    video_chaps=Video_chap.objects.filter(formation_id=request.POST.get('formation_id'))
    messages.success(request,("Suppresssion effectuée avec susscès"))
    return render(request, 'administration/edit_formation.html',{'formt':formt,'chap':chap,'video_chaps': video_chaps})
  
  
  
@login_required
def delete_course(request):
    user_logged=get_user_logged(request)
    formation_id=request.POST['formation_id'] 
    cur_chap=Video_chap.objects.get(video_id=request.POST['video_id'] )
    cur_chap.delete()
    formt=formation.objects.get(formation_id=request.POST.get('formation_id'))
    chap=chapitre.objects.filter(frmt_id=request.POST.get('formation_id'))
    counter=0
    for ch in chap:
        counter+=1
        ch.num=counter
    video_chaps=Video_chap.objects.filter(formation_id=request.POST.get('formation_id'))
    messages.success(request,("Suppresssion effectuée avec susscès"))
    return render(request, 'administration/edit_formation.html',{'formt':formt,'chap':chap,'video_chaps': video_chaps})
  


@login_required
def delete_formation_presentation(request):
    user_logged=get_user_logged(request)
    formation_id=request.POST['formation_id'] 
    current_formation=formation.objects.filter(formation_id=formation_id).update(
        formation_presentation=""
    )
    formt=formation.objects.get(formation_id=request.POST.get('formation_id'))
    chap=chapitre.objects.filter(frmt_id=request.POST.get('formation_id'))
    counter=0
    for ch in chap:
        counter+=1
        ch.num=counter
    video_chaps=Video_chap.objects.filter(formation_id=request.POST.get('formation_id'))
    messages.success(request,("Suppresssion effectuée avec susscès"))
    return render(request, 'administration/edit_formation.html',{'formt':formt,'chap':chap,'video_chaps': video_chaps})

@login_required
def show_formation_details(request):
    user_logged=get_user_logged(request)
    formation_id=request.POST['formation_id'] 
    data=formation.objects.get(formation_id=formation_id)
    chapitres=chapitre.objects.filter(frmt_id=formation_id).order_by('chap_id')
    formation_=souscription_formation.objects.select_related('formation_id', 'matricule').filter(matricule=user_logged.matricule,formation_id=formation_id)
    return render(request,'users/nfa-formation-details.html'
                  ,{
                      'formation':data
                    ,'chap':chapitres
                    ,'user_logged':user_logged
                    ,'autorization':formation_
                    })
    
@login_required
def get_formation_details(request,formation_id):
    user_logged=get_user_logged(request)
    formation_id=request.POST['formation_id'] 
    data=formation.objects.get(formation_id=formation_id)
    chapitres=chapitre.objects.filter(frmt_id=formation_id).order_by('chap_id')
    formation_=souscription_formation.objects.select_related('formation_id', 'matricule').filter(matricule=user_logged.matricule,formation_id=formation_id)
    return render(request,'users/nfa-formation-details.html'
                  ,{
                      'formation':data
                    ,'chap':chapitres
                    ,'user_logged':user_logged
                    ,'autorization':formation_
                    })
    



@login_required
def send_subscription_request(request):
    user_logged=get_user_logged(request)
    ref1=request.POST['ref_transact_1']
    ref2=request.POST['ref_transact_2']
    if ref1==ref2:
        formation_instance = formation.objects.get(formation_id=request.POST['formation_id'])
        user_instance=utilisateur.objects.get(matricule=user_logged.matricule)
        demande=souscription_formation(
        formation_id=formation_instance,
        matricule=user_instance,
        operator=request.POST['operator'],
        ref_transact=ref1
    )
        demande.save()
        messages.success(request,' Votre demande a bien été enregistré, vous serez notifié après la validation de votre demande.')
    else:
        messages.error(request,' Merci de vérifier la référence du transaction.')
    
    # return redirect(f"/details_course/{request.POST['formation_id']}")
    return redirect('formations-availables')


@login_required
def inscription_atelier(request):
    user_logged=get_user_logged(request)
    list_souscription=Souscription_atelier.objects.select_related('atelier_id','matricule').filter(matricule=user_logged.matricule,atelier_id=request.POST['atelier_id'])
    atelier=Atelier.objects.get(atelier_id=request.POST['atelier_id'])
    if user_logged.user_type=='student':
        if not list_souscription:
            user_isntance=utilisateur.objects.get(matricule=user_logged.matricule)
            atelier_instance=Atelier.objects.get(atelier_id=request.POST['atelier_id'])
            new_subscription=Souscription_atelier(matricule=user_isntance,atelier_id=atelier_instance)
            new_subscription.save()
            mail_content=f"""
            Bonjour,
            L'utilisateur {user_logged.first_name} {user_logged.last_name} s'est inscrit à l'atelier {atelier.titre}
            
            ******Informations sur l'utilisateur:
            Atelier: {atelier.titre}
            Nom:    {user_logged.first_name}
            Prénom(s):  {user_logged.last_name}
            Adresse:    {user_logged.adress}
            sexe:   {user_logged.sex}
            Telephone:  {user_logged.phone}
            Email:  {user_logged.email}
            *******
            Ce message est une alerte automatique pour signaler les nouvelle souscriptioin à un atelier.
            Cordialment,
            Next Food Africa
            nextfoodafricamg@gmail.com'
            """
            send_mail('andriamanantenalw@gmail.com',mail_content)
            messages.success(request,'Votre inscription a bien été enregistrée!!!')
            list_souscription=Souscription_atelier.objects.select_related('atelier_id','matricule').filter(matricule=user_logged.matricule,atelier_id=request.POST['atelier_id'])
            
            return render(request, 'users/details_atelier.html',{'atelier':atelier,'user_logged':user_logged,'autorization':list_souscription})
        else:
            return render(request, 'users/details_atelier.html',{'atelier':atelier,'user_logged':user_logged,'autorization':list_souscription})
    elif user_logged.user_type=='admin':
        return redirect('admin_dashboard')
    
    
############################ADMINISTRATION################################
@login_required
def administration(request):
    user_logged=get_user_logged(request)
    if user_logged.user_type=='admin':
        users=utilisateur.objects.filter(user_type='student').count()
        subscription_demand=demande_inscription.objects.filter(status='waiting',already_signed_up='No').count()
        subscription_frmt_demand=souscription_formation.objects.select_related('formation_id', 'matricule').filter(souscription_status='Waiting').count()
        free_formation=formation.objects.filter(formation_type='gratuit').count()
        paid_formation=formation.objects.filter(formation_type='payant').count()
        paiements=souscription_formation.objects.filter(souscription_status='Waiting').count()
        return render(request, 'administration/dashboard.html',{'nb_user':users,'subs_demand':subscription_demand,'free_frmt':free_formation,'paid_frmt':paid_formation,'subscription_frmt_demand':subscription_frmt_demand,'paiements':paiements})
    elif user_logged.user_type=='student':
        return redirect('dashboard')
    
@login_required
def gestion_utilisateur(request):
    user_logged=get_user_logged(request)
    if user_logged.user_type=='admin':
        users=utilisateur.objects.all().filter(user_type='student')
        return render(request, 'administration/gestion_utilisateur_inst_srch.html',{'users':users})
    elif user_logged.user_type=='student':
        return redirect('dashboard')

@login_required
def formation_payante(request):
    user_logged=get_user_logged(request)
    prog=formation.objects.filter(formation_type='payant')
    for item in prog:
        item.short_descr = ' '.join(item.formation_descr.split()[:20])
    
    return render(request, 'users/nfa-formation-payantes.html',{'prog': prog,'user_logged':user_logged})

@login_required
def formations_available(request):
    user_logged=get_user_logged(request)
    all_paid_formations=formation.objects.filter(formation_type='payant')
    prog=souscription_formation.objects.select_related('formation_id', 'matricule').filter(matricule=user_logged.matricule)
    free=formation.objects.filter(formation_type='gratuit')
    paid=list()
    waiting=list()
    available=list()
    frmt_ids=prog.values_list('formation_id', flat=True)
    for item in free:
        item.short_descr = ' '.join(item.formation_descr.split()[:20])
    for item in prog:
        print(item.souscription_status)
        item.formation_id.short_descr = ' '.join(item.formation_id.formation_descr.split()[:20])
        if item.formation_id.formation_type=='gratuit':
            free.append(item)
        if item.souscription_status=='Validated':
            paid.append(item)
        if item.souscription_status in ['Denied','Waiting']:
            waiting.append(item)
    for item in all_paid_formations:
        if item.formation_id not in frmt_ids:
            item.short_descr = ' '.join(item.formation_descr.split()[:20])
            available.append(item)
    return render(request, 'users/nfa-formations-availables.html',{
        'prog': prog
        ,'gratuits':free
        ,'payants':paid
        ,'en_attentes':waiting
        ,'disponibles':available
        ,'user_logged':user_logged
        })
    
@login_required
def gestion_atelier(request):
    user_logged=get_user_logged(request)
    if user_logged.user_type=='admin':
        ateliers=Atelier.objects.all()
        return render(request, 'administration/atelier_home.html',{'ateliers':ateliers})
    elif user_logged.user_type=='student':
        return redirect('dashboard')
    
@login_required
def voir_atelier(request):
    user_logged=get_user_logged(request)
    if user_logged.user_type=='student':
        ateliers=Atelier.objects.all()
        for item in ateliers:
            item.short_descr = ' '.join(item.description.split()[:20])
        return render(request, 'users/nfa-ateliers.html',{'ateliers':ateliers,'user_logged':user_logged})
    elif user_logged.user_type=='admin':
        return redirect('admin_dashboard')
    
def check_update(new_value,old_value):
    if new_value:
        return new_value
    else:
        return old_value


@login_required
def delete_atelier(request):
    user_logged=get_user_logged(request)
    if user_logged.user_type=='admin':
        try:
            atelier=Atelier.objects.get(atelier_id=request.POST['atelier_id'])
            atelier.delete()
            messages.success(request,' Atelier supprimé avec succès!!!')
        except:
            print(f"erreur de suppression")
            messages.error(request,' Oups, une erreur est survenue!!!')
        return redirect('gestion_atelier')
    elif user_logged.user_type=='student':
        return redirect('dashboard')




@login_required
def edit_atelier(request):
    user_logged=get_user_logged(request)
    if user_logged.user_type=='admin':
        atelier=Atelier.objects.get(atelier_id=request.POST['atelier_id'])

        Atelier.objects.filter(atelier_id=request.POST['atelier_id']).update(
        titre=check_update(request.POST['titre'],atelier.titre)
        ,date_debut=check_update(request.POST['date_debut'],atelier.date_debut)
        ,date_fin=check_update(request.POST['date_fin'],atelier.date_fin)
        ,lieu=check_update(request.POST['lieu'],atelier.lieu)
        ,heure_debut=check_update(request.POST['heure_debut'],atelier.heure_debut)
        ,heure_fin=check_update(request.POST['heure_fin'],atelier.heure_fin)
        ,type=check_update(request.POST['type'],atelier.type)
        ,price=check_update(request.POST['price'],atelier.price)
        )
        if request.FILES.get('img'):
            Atelier.objects.filter(atelier_id=request.POST['atelier_id']).update(img= upload_file(request.FILES.get('img'),'image'))
        
        description= check_update(request.POST['description'],atelier.description)
        return redirect('gestion_atelier')
    elif user_logged.user_type=='student':
        return redirect('dashboard')

@login_required
def del_user_from_atelier(request):
    souscription=Souscription_atelier.objects.get(souscription_id=request.POST['souscription_id'])
    atelier=Atelier.objects.get(atelier_id=souscription.atelier_id.atelier_id)
    list_souscription=Souscription_atelier.objects.select_related('atelier_id','matricule').filter(atelier_id=souscription.atelier_id)
    Souscription_atelier.objects.filter(souscription_id=souscription.souscription_id).delete()
    messages.success(request,f'{souscription.matricule.first_name} {souscription.matricule.last_name} a été supprimé de la liste.')
    return render(request, 'administration/edit_atelier.html',{'atelier':atelier,'list_souscription':list_souscription})
    

@login_required
def details_atelier(request):
    user_logged=get_user_logged(request)
    atelier=Atelier.objects.get(atelier_id=request.POST['atelier_id'])
    list_souscription=Souscription_atelier.objects.select_related('atelier_id','matricule').filter(atelier_id=request.POST['atelier_id'])
    if user_logged.user_type=='admin':
        return render(request, 'administration/edit_atelier.html',{'atelier':atelier,'list_souscription':list_souscription})
    elif user_logged.user_type=='student':
        list_souscription=Souscription_atelier.objects.select_related('atelier_id','matricule').filter(matricule=user_logged.matricule,atelier_id=request.POST['atelier_id'])
        for a in list_souscription:
            print(f"===>{a.souscription_id}")
            print(f"===>{a.matricule.matricule}")
        return render(request, 'users/details_atelier.html',{'atelier':atelier,'user_logged':user_logged,'autorization':list_souscription})

def exporter_pdf_post(request):
    print('tonga eto')
    user_logged=get_user_logged(request)
    atelier=Atelier.objects.get(atelier_id=request.POST['atelier_id'])
    list_souscription=Souscription_atelier.objects.select_related('atelier_id','matricule').filter(atelier_id=request.POST['atelier_id'])
    # Générer le contenu HTML
    count=0
    for subs in list_souscription:
        count+=1
        subs.nb=count
    html_string = render_to_string('administration/Template_PDF_ATELIER.html', {'atelier':atelier,'list_souscription':list_souscription})
    # Convertir le HTML en PDF
    pdf_file = HTML(string=html_string).write_pdf()

    # Créer une réponse HTTP avec le fichier PDF
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f"attachment; filename=list_souscription_{atelier.titre}_{timezone.now()}.pdf"

    return response

def exporter_pdf(request,atelier_id):
    print('tonga eto')
    user_logged=get_user_logged(request)
    atelier=Atelier.objects.get(atelier_id=atelier_id)
    list_souscription=Souscription_atelier.objects.select_related('atelier_id','matricule').filter(atelier_id=atelier_id)
    # Générer le contenu HTML
    html_string = render_to_string('administration/edit_atelier.html', {'atelier':atelier,'list_souscription':list_souscription})
    print(html_string)
    # Convertir le HTML en PDF
    pdf_file = HTML(string=html_string).write_pdf()

    # Créer une réponse HTTP avec le fichier PDF
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="list_souscription.pdf"'

    return response

@login_required
def creation_atelier(request):
    user_logged=get_user_logged(request)
    new_atelier=Atelier(
        titre=request.POST['titre']
        ,date_debut=request.POST['date_debut']
        ,lieu=request.POST['lieu']
        ,date_fin=request.POST['date_fin']
        ,heure_debut=request.POST['heure_debut']
        ,heure_fin=request.POST['heure_fin']
        ,type=request.POST['type']
        ,price=request.POST['price']
        ,img= upload_file(request.FILES.get('img'),'image')
        ,description= request.POST['description']
    )
    print(f"""
          ------CREATION ATELIER-----
          {new_atelier.titre}
          {new_atelier.date_creation}
          {new_atelier.date_debut}
          {new_atelier.lieu}
          {new_atelier.date_fin}
          {new_atelier.heure_debut}
          {new_atelier.heure_fin}
          {new_atelier.type}
          {new_atelier.price}
          {new_atelier.img}
          {new_atelier.description}
          """)
    new_atelier.save()
    messages.success(request,' Atelier bien enregistré!!!')
    return redirect('gestion_atelier')

@login_required
def subscription(request):
    user_logged=get_user_logged(request)
    if user_logged.user_type=='admin':
        users=demande_inscription.objects.filter(status='waiting',already_signed_up='No')
        return render(request, 'administration/gestion_inscription.html',{'users':users})
    elif user_logged.user_type=='student':
        return redirect('dashboard')

@login_required
def deny_subscription(request):
    user_logged=get_user_logged(request)
    if user_logged.user_type=='admin':
        apprenant=demande_inscription.objects.filter(status='waiting',already_signed_up='No',dmd_id=request.POST['dmd_id']).update(status='Denied')
        return redirect('/subscription')

@login_required
def validate_subscription(request):
    user_logged=get_user_logged(request)
    if user_logged.user_type=='admin':
        apprenant=demande_inscription.objects.get(status='waiting',already_signed_up='No',dmd_id=request.POST['dmd_id'])
        chiffres = ''.join(random.choices('123456789', k=4))
        majuscules = ''.join(random.choices([c for c in string.ascii_uppercase if c != 'O'], k=2))
        minuscules = ''.join(random.choices(string.ascii_lowercase, k=2))
        mot_de_passe = chiffres + majuscules + minuscules
        mot_de_passe = ''.join(random.sample(mot_de_passe, len(mot_de_passe)))
        form = RegisterUserForm({
            'email': apprenant.email,
            'first_name': apprenant.first_name,
            'phone':apprenant.phone,
            'adress' : apprenant.adress,
            'sex' : apprenant.sex,
            'last_name': apprenant.last_name,
            'username': apprenant.username,
            'password1': mot_de_passe,
            'password2': mot_de_passe
        })
        if form.is_valid():
            user = form.save()
        user_saved=User.objects.get(email=apprenant.email,
            first_name = apprenant.first_name,
            last_name = apprenant.last_name,)
        data=utilisateur(
            matricule=user_saved.id,
            email = apprenant.email,
            first_name = apprenant.first_name,
            last_name = apprenant.last_name,
            sex = apprenant.sex,
            adress = apprenant.adress,
            phone = apprenant.phone,
            username = apprenant.username,
            password = mot_de_passe
        )
        data.save()
        demande_inscription.objects.filter(dmd_id=request.POST['dmd_id']).update(status='validated',already_signed_up='Yes',date_validation=datetime.today().strftime('%F'))
        users=demande_inscription.objects.filter(status='waiting',already_signed_up='No')
        mail_content=f"""
        Bonjour {apprenant.first_name} {apprenant.last_name},
        Votre de mande d'inscription sur la plateforme Next Food Africa a été validé.
        Vous pouvez maintenant naviguer sur notre plateforme et suivre les cours.
        Voici vos accès:
        Nom d'utilisateur:{apprenant.username}
        Mot de passe:{mot_de_passe}
        
        NB: Accédez à votre compte et changez votre mot de passe dès que possible.
        Ne communiquez à personne votre mot de passe.
        """
        send_mail(apprenant.email,mail_content)
        return redirect('subscription')
    elif user_logged.user_type=='student':
        return redirect('dashboard')

@login_required
def about_user(request,id):
    user_logged=get_user_logged(request)
    if user_logged.user_type=='admin':
        account=utilisateur.objects.get(matricule=id)
        return render(request,'administration/show_user.html',{'account':account})
    elif user_logged.user_type=='student':
        return redirect('dashboard')
    
@login_required
def gestion_formation(request):
    user_logged=get_user_logged(request)
    if user_logged.user_type=='admin':
        frmt=formation.objects.all()
        return render(request, 'administration/gestion_formation.html',{'frmt':frmt})
    elif user_logged.user_type=='student':
        return redirect('dashboard')
    

@login_required
def gestion_free_formation(request):
    user_logged=get_user_logged(request)
    if user_logged.user_type=='admin':
        frmt=formation.objects.filter(formation_type='gratuit')
        return render(request, 'administration/gestion_formation.html',{'frmt':frmt})
    elif user_logged.user_type=='student':
        return redirect('dashboard')
    
    
@login_required
def gestion_paid_formation(request):
    user_logged=get_user_logged(request)
    if user_logged.user_type=='admin':
        frmt=formation.objects.filter(formation_type='payant')
        return render(request, 'administration/gestion_formation.html',{'frmt':frmt})
    elif user_logged.user_type=='student':
        return redirect('dashboard')
    
@login_required
def create_formation(request):
    if request.method == 'POST':
        formation_img = request.FILES.get('formation_img')
        formation_id = request.POST.get('formation_id')
        formation_name = request.POST.get('formation_name')
        formation_descr = request.POST.get('formation_descr')
        formation_type = request.POST.get('formation_type')
        if formation_type=="payant":
            formation_prix = request.POST.get('formation_prix')
        else:
            formation_prix=0
        data = formation(
            formation_id=formation_id,
            formation_name=formation_name,
            formation_descr=formation_descr,
            formation_type=formation_type,
            formation_prix=formation_prix
        )
        if formation_img:
            upload_path = os.path.join(settings.MEDIA_ROOT, 'blogdesign', 'assets', 'img')
            os.makedirs(upload_path, exist_ok=True)
            with open(os.path.join(upload_path, formation_img.name), 'wb+') as destination:
                print(f"*******DESTINATIONN: {destination}")
                for chunk in formation_img.chunks():
                    destination.write(chunk)
        data.formation_img = os.path.join('blogdesign', 'assets', 'img', formation_img.name)
        data.formation_presentation=upload_file(request.FILES.get('formation_presentation'),'presentations')
        data.save()
        return redirect('gestion_formation')

def upload_file(file,type):
    if file:
            upload_path = os.path.join(settings.MEDIA_ROOT, 'formations',type)
            os.makedirs(upload_path, exist_ok=True)
            with open(os.path.join(upload_path, file.name), 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            filepath=os.path.join('formations', type, file.name)
    print(f"==>FILE UPLOADED AT: {filepath}")
    return filepath

@login_required
def edit_formation(request):
    if request.method == 'POST':
        print(f"FORMATION_ID:{request.POST.get('formation_id')}")
        formt=formation.objects.get(formation_id=request.POST.get('formation_id'))
        chap=chapitre.objects.filter(frmt_id=request.POST.get('formation_id')).order_by('chap_id')
        counter=0
        for ch in chap:
            counter+=1
            ch.num=counter
        video_chaps=Video_chap.objects.filter(formation_id=request.POST.get('formation_id'))
        return render(request, 'administration/edit_formation.html',{'formt':formt,'chap':chap,'video_chaps': video_chaps})
    else:
        return redirect('gestion_formation')

@login_required
def create_chapter(request):
    formation_id=request.POST.get('frmt_id')
    print(f"=====>ID FORMATION:{formation_id}")
    chap=chapitre()
    chap.frmt_id=formation_id
    chap.titre=request.POST.get('formation_name')
    chap.description=request.POST.get('formation_descr')
    chap.formation_presentation=upload_file(request.FILES.get('formation_presentation'),'presentations')
    # chap.cours_file_type=request.POST.get('cours_file_type')
    # chap.exemple_file_type=request.POST.get('exemple_file_type')
    chap.cours_content=upload_file(request.FILES.get('formation_presentation'),'presentations')
    # chap.exemple_content=upload_file(request.FILES.get('exemple_content'),'exemples')
    # chap.quizz_content=upload_file(request.FILES.get('quizz_content'),'quizz')
    chap.save()
    
    formt=formation.objects.get(formation_id=formation_id)
    chap=chapitre.objects.filter(frmt_id=formation_id)
    video_chaps=Video_chap.objects.filter(formation_id=formation_id)
    return render(request, 'administration/edit_formation.html',{'formt':formt,'chap':chap,'video_chaps': video_chaps})

@login_required
def add_course(request):
    formation_id=request.POST.get('frmt_id')
    print(f"=====>ID FORMATION:{formation_id}")
    print(f"=====>ID Chapitre:{request.POST['chap_id']}")
    vid=Video_chap()
    vid.formation_id=formation.objects.get(formation_id=request.POST['frmt_id'])
    vid.chap_id=chapitre.objects.get(frmt_id=request.POST['frmt_id'] , chap_id=request.POST['chap_id'])
    vid.cours_content=upload_file(request.FILES.get('video_content'),'cours')
    vid.titre=request.POST.get('video_title')
    vid.description=request.POST.get('video_descr')
    vid.save()
    
    
    formt=formation.objects.get(formation_id=formation_id)
    chap=chapitre.objects.filter(frmt_id=formation_id)
    video_chaps=Video_chap.objects.filter(formation_id=formation_id)
    return render(request, 'administration/edit_formation.html',{'formt':formt,'chap':chap,'video_chaps': video_chaps})


@login_required
def delete_formation(request):
    formation_id=request.POST.get('formation_id')
    print(f"SUPPRESSION DE :{formation_id}")
    formation.objects.filter(formation_id=formation_id).delete()
    chapitre.objects.filter(frmt_id=formation_id).delete()
    return redirect('gestion_formation')

@login_required
def subscribe_formation_demand(request):
    user_logged=get_user_logged(request)
    if request.method == 'GET':
        demande = souscription_formation.objects.select_related('formation_id', 'matricule')
        for dmd in demande:
            validation=paiement.objects.filter(matricule=dmd.matricule,formation_id=dmd.formation_id,ref_transact=dmd.ref_transact)
            if validation:
                dmd.paiement_status='PAID'
            else:
                dmd.paiement_status='NOT YET PAID'
        return render(request, 'administration/subscription_formation.html',{'demande':demande,'user':user_logged})

def subscribe_course(request):
        formation_id=request.POST.get('formation_id')
        print(f"INSCRIPTION AU COURS:{formation_id}")
        form = RegisterUserForm()
        form.fields['last_name'].widget.attrs['class'] = "form-control"
        form.fields['first_name'].widget.attrs['class'] = "form-control"
        form.fields['email'].widget.attrs['class'] = "form-control"
        SEX_CHOICES = [
        ('H', 'Homme'),
        ('F', 'Femme'),
    ]
        form.fields['sex'] = forms.ChoiceField(choices=SEX_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
        form.fields['adress'].widget.attrs['class'] = "form-control"
        form.fields['phone'].widget.attrs['class'] = "form-control"
        form.fields['username'].widget.attrs['class'] = "form-control"
        form.fields['password1'].widget.attrs['class'] = "form-control"
        form.fields['password2'].widget.attrs['class'] = "form-control"
        
        form.fields['first_name'].widget.attrs['placeholder'] = "Prénom(s)"
        form.fields['last_name'].widget.attrs['placeholder'] = "Nom"
        form.fields['email'].widget.attrs['placeholder'] = "email"
        form.fields['adress'].widget.attrs['placeholder'] = "Votre adresse"
        form.fields['phone'].widget.attrs['placeholder'] = "Numéro de téléphone"
        form.fields['username'].widget.attrs['placeholder'] = "Nom d'utilisateur"
        # form.fields['password1'].widget.attrs['placeholder'] = "Votre mot de passe"
        # form.fields['password2'].widget.attrs['placeholder'] = "Merci de confirmer votre mot de passe"
        return render(request, 'administration/subscribe_formation.html',{'formation_id':formation_id,'form':form})


@login_required
def validate_formation_subscription(request):
    user_logged=get_user_logged(request)
    if user_logged.user_type=='admin':
        if request.method == 'POST':
            print(f"demande:{request.POST.get('dmd_souscription_id')}")
            souscription_formation.objects.filter(dmd_souscription_id=request.POST.get('dmd_souscription_id')).update(souscription_status='Validated',date_modification=datetime.today().strftime('%F'))
            return redirect('subscribe_formation_demand')
    elif user_logged.user_type=='student':
        return redirect('dashboard')
    
    
@login_required
def getsion_quizz(request):
    user_logged=get_user_logged(request)
    if user_logged.user_type=='admin':
            formation_id=request.POST.get('formation_id')
            chap_id=request.POST.get('chap_id')
            frmtn=formation.objects.get(formation_id=formation_id)
            chap=chapitre.objects.get(chap_id=chap_id)
            quizz=Question.objects.filter(chap_id=chap_id)
            return render(request,'administration/gestion_quizz.html',{'formt':frmtn,'question':quizz,'chap':chap})
    elif user_logged.user_type=='student':
        return redirect('dashboard')

@login_required
def create_quizz(request):
    user_logged=get_user_logged(request)
    if user_logged.user_type=='admin':
        formation_instance = formation.objects.get(formation_id=request.POST['frmt_id'])
        chapitre_id=chapitre.objects.get(chap_id=request.POST.get('chap_id'))
        question_content=request.POST.get('question_content')
        reponse_A=request.POST.get('reponse_A')
        reponse_B=request.POST.get('reponse_B')
        reponse_C=request.POST.get('reponse_C')
        reponses_attendues = request.POST.getlist('reponses_attendues')
        quizz=Question(
            formation_id=formation_instance,
            chap_id=chapitre_id,
            question_text=question_content,
            answers=reponses_attendues
        )
        quizz.save()
        asked=Question.objects.get(
            formation_id=formation_instance,
            chap_id=chapitre_id,
            question_text=question_content,
            answers=reponses_attendues
        )
        reponse_A=Answer_possible(
            question_id=asked,
            answer_text=reponse_A,
            answer_alias='A'
        )
        reponse_B=Answer_possible(
            question_id=asked,
            answer_text=reponse_B,
            answer_alias='B'
        )
        reponse_C=Answer_possible(
            question_id=asked,
            answer_text=reponse_C,
            answer_alias='C'
        )
        reponse_A.save()
        reponse_B.save()
        reponse_C.save()
        print(f"""
              formation ID:{formation_instance}
              Chapitre ID:{chapitre_id}
              question:{question_content}
              reponse_A:{reponse_A}
            reponse_B:{reponse_B}
            reponse_C:{reponse_C}
            reponses_attendues:{reponses_attendues}
              """)
        chap=chapitre.objects.get(chap_id=chapitre_id.chap_id)
        quizz=Question.objects.filter(chap_id=chapitre_id.chap_id)
        return render(request,'administration/gestion_quizz.html',{'formt':formation_instance,'question':quizz,'chap':chap})


@login_required
def deny_formation_subscription(request):
    user_logged=get_user_logged(request)
    date_obj=datetime.strptime(request.POST.get('date_souscription'), "%B %d, %Y")
    date_str= date_obj.strftime('%Y-%m-%d')
    print(f"DATY:{date_str}")
    
    if user_logged.user_type=='admin':
        if request.method == 'POST':
            print(f"demande:{request.POST.get('dmd_souscription_id')}")
            souscription_formation.objects.filter(dmd_souscription_id=request.POST.get('dmd_souscription_id'),matricule=request.POST.get('matricule'),formation_id=request.POST.get('formation_id'),date_souscription=date_str).update(souscription_status='Denied',date_modification=datetime.today().strftime('%F'))
            return redirect('subscribe_formation_demand')
    elif user_logged.user_type=='student':
        return redirect('dashboard')

@login_required
def make_wait_formation_subscription(request):
    user_logged=get_user_logged(request)
    date_obj=datetime.strptime(request.POST.get('date_souscription'), "%B %d, %Y")
    date_str= date_obj.strftime('%Y-%m-%d')
    print(f"DATY:{date_str}")
    
    if user_logged.user_type=='admin':
        if request.method == 'POST':
            print(f"demande:{request.POST.get('dmd_souscription_id')}")
            souscription_formation.objects.filter(dmd_souscription_id=request.POST.get('dmd_souscription_id'),matricule=request.POST.get('matricule'),formation_id=request.POST.get('formation_id'),date_souscription=date_str).update(souscription_status='Waiting',date_modification=datetime.today().strftime('%F'))
            return redirect('subscribe_formation_demand')
    elif user_logged.user_type=='student':
        return redirect('dashboard')
    
@login_required
def gestion_paiement(request):
    user_logged=get_user_logged(request)
    if user_logged.user_type=='admin':
        if request.method == 'POST':
            if(request.POST.get('ref_transact1')==request.POST.get('ref_transact2')):
                formation_instance = formation.objects.get(formation_id=request.POST['formation_id'])
                user_instance=utilisateur.objects.get(matricule=request.POST['matricule'])
                new_payment=paiement(
                matricule=user_instance,
                ref_transact=request.POST.get('ref_transact1'),
                montant=request.POST.get('montant'),
                formation_id=formation_instance,
                sender=request.POST.get('sender'),
                receiver=request.POST.get('receiver'),
                transact_type=request.POST.get('transact_type'),
                remarque=request.POST.get('remarque')
            )
                new_payment.save()
                messages.success(request,' Paiement enregistré!!!')
                return redirect('gestion_paiements')
            else:
                messages.error(request,' Merci de vérifier la référence du transaction.')
                return render(request, 'administration/gestion_paiement.html',{'formations':data,'utilisateurs':users,'paiements':paiements})
        else:
            users=utilisateur.objects.filter(user_type='student')
            data=formation.objects.filter(formation_type='payant')
            paiements=paiement.objects.select_related('formation_id', 'matricule')
            stat_paiement=None
            for i in paiements:
                diff_paiement=i.formation_id.formation_prix-i.montant
                print(diff_paiement)
                if diff_paiement>=0:
                    stat_paiement='Frais entièrements payés.'
                else:
                    stat_paiement=f"Reste à payer:{diff_paiement} Ariary"
                i.stat_paiement=stat_paiement
            return render(request, 'administration/gestion_paiement.html',{'formations':data,'utilisateurs':users,'paiements':paiements})
    elif user_logged.user_type=='student':
        return redirect('dashboard')
    

def error_404(request, exception):
    print('tonga ato am 404')
    return render(request, 'administration/404.html', {})


############################END ADMINISTRATION################################
###########UTILITAIRES#########
def send_mail(to_email,content):
    email_address = 'nextfoodafricamg@gmail.com'
    email_password = 'ivyz bbjd rvfa rkym '
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    message = MIMEMultipart()
    message['From'] = email_address
    message['To'] = to_email
    message['Subject'] = f'Validation demande inscription'
    message_text=f"""
        ***********
        From : Next Food Africa
        At : {datetime.today()}
        ***********
        Content:
        {content}

    """
    print(message_text)
    message.attach(MIMEText(message_text, 'plain'))
    server=None
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(email_address, email_password)

        # Envoyer l'e-mail
        server.sendmail(email_address, to_email, message.as_string())
        print('E-mail envoyé avec succès !')

    except Exception as e:
        print('Erreur lors de l\'envoi de l\'e-mail :', str(e))

    finally:
        # Fermer la connexion SMTP
        server.quit()
        
