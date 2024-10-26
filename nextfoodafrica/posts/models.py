from django.db import models
from datetime import datetime
from django.utils import timezone
from autoslug import AutoSlugField
from django.contrib.auth.models import User,AbstractBaseUser, BaseUserManager, PermissionsMixin
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

###########authentification and signup
from django.contrib.auth.models import AbstractUser
###########end authentification and signup
import time
from datetime import datetime
import os
from edureka import settings
from django.contrib.postgres.fields import ArrayField



class Category(models.Model):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank = True, null=True)
    title = models.CharField(max_length=100) 
    slug = AutoSlugField(populate_from='title', unique=True, null=False, editable=True)
    logo = models.ImageField(upload_to='media/catlogo', blank=True, null=True, help_text='Optional')
    logo1 = models.ImageField(upload_to='media/catlogo', blank=True, null=True, help_text='Optional')
    logo2 = models.ImageField(upload_to='media/catlogo', blank=True, null=True, help_text='Optional')
    top_three_cat = models.BooleanField(default=False)
    more = models.BooleanField(default=False, blank=True, verbose_name="For Add In Right Menu")
    created_at = models.DateTimeField(auto_now_add=True)
    disc = models.BooleanField(default=False, verbose_name='Add In Disclaimer')
    hit = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def post_count(self):
        return self.posts.all().count()    

    class Meta:
        #enforcing that there can not be two categories under a parent with same slug
        
        # __str__ method elaborated later in post.  use __unicode__ in place of

        unique_together = ('slug', 'parent',)    
        verbose_name_plural = "categories"     

    def __str__(self):                           
        full_path = [self.title]                  
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' -> '.join(full_path[::-1])    

class subcat(models.Model):
    parent = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcat', blank = True, null=True, help_text='Select Only Sub Category')
    title = models.CharField(max_length=100) 
    slug = AutoSlugField(populate_from='title', unique=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    disc = models.BooleanField(default=False, verbose_name='Add In Disclaimer')

    def __str__(self):
        return self.title

    class Meta:
        #enforcing that there can not be two categories under a parent with same slug
        
        # __str__ method elaborated later in post.  use __unicode__ in place of

        unique_together = ('slug', 'parent',)
        #This is for outside or main which shows outside panel.    
        verbose_name_plural = "Sub Categories"     

    def __str__(self):                           
        full_path = [self.title]                  
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' -> '.join(full_path[::-1])    

class MainCourse(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title', unique=True, null=False, editable=True)
    disc = models.BooleanField(default=False, verbose_name='Add In Disclaimer')

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=500)
    meta_tags = models.CharField(max_length=2000, blank=True)
    meta_desc = models.TextField(max_length=2000, blank=True)
    slug = AutoSlugField(populate_from='title', max_length=500, unique=True, null=False)
    image = models.ImageField(upload_to='media/post')
    image_alt_name = models.CharField(max_length=200, blank=True)
    logo = models.ImageField(upload_to='media/post') #If user want to add university logo(Slider and Post) 
    desc = RichTextField(blank=True, null=True)
    #for live classes or offline classes
    badge = models.CharField(max_length=70)
    youtube = models.URLField(max_length=500, default='' )
    author = models.CharField(max_length=20, default="admin" )
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, related_name="posts")
    subcategory = models.ForeignKey(subcat, on_delete=models.CASCADE, default=1, related_name="subcat", blank=True, null=True)
    hit = models.PositiveIntegerField(default=0) #This field is for popular posts
    button_text = models.CharField(max_length=20, default="Apply Now") #Apply Now and enroll button text
    slider_post = models.BooleanField(default=False, blank=True)
    maincourse = models.ManyToManyField(MainCourse, blank=True, related_name='posts')
    price = models.IntegerField(default=0)
    old_price = models.IntegerField(default=0)
    discount = models.IntegerField()
    emi_start_price = models.IntegerField()
    why_title = models.CharField(max_length=500, blank=True)
    why1 = RichTextField(blank=True)
    why2 = RichTextField(blank=True)
    why3 = RichTextField(blank=True)
    file = models.FileField(upload_to='media/certificate', null=True, blank=True)
    disc = models.BooleanField(default=False, verbose_name='Add In Disclaimer')
    
    def __str__(self):
        return self.title    
        
    def get_rating(self):
        total = sum(int(review['stars']) for review in self.review.values() )

        return total / self.reviews.count()

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.image = self.compressImage(self.image)
    #     super(Upload, self).save(*args, **kwargs)
    
    # def compressImage(self,image):
    #     imageTemproary = Image.open(image)
    #     outputIoStream = BytesIO()
    #     imageTemproaryResized = imageTemproary.resize( (1300,400) ) 
    #     imageTemproary.save(outputIoStream , format='JPEG', quality=60)
    #     outputIoStream.seek(0)
    #     image = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % image.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
    #     return image    

class blog(models.Model):
    title = models.CharField(max_length=70)
    meta_tags = models.CharField(max_length=2000, blank=True)
    meta_desc = models.TextField(max_length=2000, blank=True)
    slug = AutoSlugField(populate_from='title', unique=True, null=False, editable=True)
    image = models.ImageField(upload_to='media/blog')
    image_alt_name = models.CharField(max_length=200, blank=True)
    desc = RichTextField(blank=True, null=True)
    author = models.CharField(max_length=20, default="admin" )
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, related_name="blog")
    hit = models.PositiveIntegerField(default=0) #This field is for popular posts
    disc = models.BooleanField(default=False, verbose_name='Add In Disclaimer')
    
    def __str__(self):
        return self.title    
        
    def get_rating(self):
        total = sum(int(review['stars']) for review in self.review.values() )

        return total / self.reviews.count()

class blankpage(models.Model):      
    title = models.CharField(max_length=70)
    meta_tags = models.CharField(max_length=2000, blank=True)
    meta_desc = models.TextField(max_length=2000, blank=True)
    slug = AutoSlugField(populate_from='title', unique=True, null=False, editable=True)
    image = models.ImageField(upload_to='media/blog')
    image_alt_name = models.CharField(max_length=200, blank=True)
    desc = RichTextField(blank=True, null=True)
    author = models.CharField(max_length=20, default="admin" )
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, related_name="blank")
    hit = models.PositiveIntegerField(default=0) #This field is for popular posts
    disc = models.BooleanField(default=False, verbose_name='Add In Disclaimer')
    
    def __str__(self):
        return self.title    
        
    def get_rating(self):
        total = sum(int(review['stars']) for review in self.review.values() )

        return total / self.reviews.count()

class Curriculam(models.Model):    
    title = models.CharField(max_length=500)
    Post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='acc_posts')
    content = RichTextField(blank=True, null=True)

#Terms and Condition for blogs
class tcforblog(models.Model):    
    title = models.CharField(max_length=500)
    blank_page = models.ForeignKey(blankpage, on_delete=models.CASCADE, related_name='tc_blank_page', blank=True, null=True)
    content = RichTextField(blank=True, null=True)

class faq(models.Model):    
    title = models.CharField(max_length=500)
    Post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='faq_posts')
    content = RichTextField(blank=True, null=True)

class timing(models.Model):    
    date = models.CharField(max_length=100, blank=True, null=True)
    day_duration = models.CharField(max_length=100, blank=True, null=True)
    time_duration1 = models.CharField(max_length=100, blank=True, null=True)
    time_duration2 = models.CharField(max_length=100, blank=True, null=True)
    Post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='time_posts')

class Certificate(models.Model):
    file = models.FileField(upload_to='media/certificate', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    Post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='cert_posts')

class features(models.Model):    
    title = models.CharField(max_length=500)
    Post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='feature_posts')
    content = RichTextField(blank=True, null=True)

class boxes_three(models.Model):
    title = models.CharField(max_length=70)
    slug = AutoSlugField(populate_from='title', unique=True, null=False, editable=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title    

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='comments'
    )
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)    

class promocode(models.Model):
    code = models.CharField(max_length=50, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    # discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    amount = models.FloatField()
    active = models.BooleanField()

    def __str__(self):
        return self.code

class Cart(models.Model):
    cart_id = models.CharField(max_length=500, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
    item = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='item')
    purchase = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    certificate = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.item}'

    def get_total(self):
        total = self.item.price
        float_total = format(total, '0.2f')
        return float_total    

class Order(models.Model):
    method = (
        ('EMI', "EMI"),
        ('ONLINE', "Online"),
    )
    orderitems = models.ManyToManyField(Cart)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    phone = models.CharField(max_length=10, null = False, default='0')
    coupon = models.ForeignKey(promocode, on_delete=models.SET_NULL, blank=True, null=True)
    total = models.DecimalField(max_digits=10, default=0, decimal_places=2, verbose_name='INR ORDER TOTAL')
    emailAddress = models.EmailField(max_length=250, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    payment_id = models.CharField(max_length=100, null=True)
    order_id =  models.CharField(max_length=100, null=True)

    def get_totals(self):
        total = 0
        for order_item in self.orderitems.all():
            total += float(order_item.get_total())
        if self.coupon:    
            total -= self.coupon.amount    
        return total

class Reviews(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    content = models.TextField(blank=True, null=True)
    stars = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

class clients(models.Model):    
    image= models.ImageField(upload_to='media/clients',null=True,blank=True)

class video(models.Model):
    title = models.CharField(max_length=100, null=False)
    post = post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='videos')
    serial_number = models.IntegerField(null=False)
    video_id = models.CharField(max_length=100)
    is_preview = models.BooleanField(default=False)
    desc = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title

class offers(models.Model):
    off = models.CharField(max_length=100, verbose_name='Total Off') 
    title = models.CharField(max_length=100, verbose_name='Title') 
    subtitle = models.CharField(max_length=100, verbose_name='Sub Title') 
    price = models.CharField(max_length=100, verbose_name='Price') 
    desc = models.CharField(max_length=100, verbose_name='Description') 
    button_text = models.CharField(max_length=100, verbose_name='Button Text') 
    button_url = models.URLField(max_length=500, default='', verbose_name='Button Link')
    small_desc = models.CharField(max_length=100, verbose_name='Small Description')
    active = models.BooleanField(default=False, verbose_name="Status")

    def __str__(self):
        return self.title 
    
class partenaires(models.Model):
    partner_id=models.IntegerField(default=0)
    nom = models.CharField(max_length=100, default='')
    logo = models.CharField(max_length=100, default='')
    Description = models.TextField(default='')

class formation(models.Model):
    formation_id=models.CharField(primary_key=True,max_length=100, default='')
    formation_img=models.CharField(max_length=300, default='')
    formation_name= models.CharField(max_length=100, default='')
    formation_descr= models.TextField(default='')
    formation_presentation=models.CharField(max_length=500, default='')
    formation_type=models.CharField(max_length=100, default='')
    formation_prix=models.IntegerField(default=0)
    formation_duree=models.CharField(max_length=300, default='UNDEFINED')
    created_at = models.DateField(default=datetime.today) 


class demande_inscription(models.Model):
    # ID Demande (clé primaire)
    # ID Utilisateur (clé étrangère faisant référence à la table Utilisateurs)
    # ID Formation (clé étrangère faisant référence à la table Formations)
    # Statut (en attente, approuvée, refusée)
    # Date de la demande
    dmd_id=models.AutoField(primary_key=True)
    matricule=models.IntegerField(default=0)
    formation_id=models.ForeignKey(formation, on_delete=models.CASCADE) #models.CharField(max_length=100, default='Unspecified')
    status=models.CharField(max_length=100, default='waiting')
    dmd_date=models.CharField(max_length=100, default=datetime.today().strftime('%F'))
    date_validation=models.CharField(max_length=50, default='')
    email=models.EmailField(max_length=50, default='')
    first_name=models.CharField(max_length=50, default='')
    last_name=models.CharField(max_length=50, default='')
    sex =models.CharField(max_length=50, default='')
    adress=models.CharField(max_length=50, default='')
    phone=models.CharField(max_length=50, default='')
    username=models.CharField(max_length=50, default='')
    password=models.CharField(max_length=50, default='')
    already_signed_up=models.CharField(max_length=50, default='No')
    

class bientot(models.Model):
    prog_id=models.IntegerField(default=0)
    prog_title=models.CharField(max_length=100, default='')
    prog_descr=models.TextField(default='')
    prog_img=models.CharField(max_length=100, default='')
    prog_resume=models.TextField(default='')
    

class chapitre(models.Model):
    chap_id = models.AutoField(primary_key=True)
    frmt_id = models.CharField(max_length=100, default='')
    chap_order=models.IntegerField(default=0)
    titre = models.TextField(default='UNDEFINED')
    description = models.TextField(default='Description du chapitre ...')
    cours_content = models.TextField(default='UNUPLOADED')
    cours_file_type = models.TextField(default='UNKNOWN')
    exemple_content = models.TextField(default='UNUPLOADED')
    exemple_file_type = models.TextField(default='UNKNOWN')
    quizz_content = models.TextField(default='UNUPLOADED')
    quizz_file_type = models.TextField(default='UNKNOWN')
    # status = models.IntegerField(default=0)  # in_progress ou done
    duree_min = models.CharField(max_length=100, default='UNDEFINED')
    date_creation = models.DateTimeField(default=timezone.now)  # Utilisation de timezone.now comme valeur par défaut

    def save(self, *args, **kwargs):
        if not self.pk:  # Si l'instance n'a pas encore de clé primaire, c'est-à-dire qu'elle est nouvellement créée
            last_instance = chapitre.objects.last()
            if last_instance:
                self.chap_id = last_instance.chap_id + 1
            else:
                self.chap_id = 1
        super().save(*args, **kwargs)

class objectif(models.Model):
    chap_id=models.IntegerField(default=0)
    frmt_id=models.CharField(max_length=100, default='')
    objctf_id=models.IntegerField(default=0)
    objctf_content=models.TextField(default='')
    duree_min=models.CharField(max_length=100, default='Undefined')
    
    
class quizz(models.Model):
    chap_id=models.IntegerField(default=0)
    frmt_id= models.CharField(max_length=100, default='')
    quizz_id=models.IntegerField(default=0)
    question=models.TextField(default='')
    qst_type=models.TextField(default='')
    answer=models.TextField(default='')
    status=models.BooleanField(default=False)#in_progress ou done
    
class collabo(models.Model):
    firstname=models.CharField(max_length=100, default='')
    lastname=models.CharField(max_length=100, default='')
    sex=models.CharField(max_length=100, default='')
    date_birth=models.DateField(default='')
    picture=models.CharField(max_length=100, default='')
    date_member=models.DateField(default='')
    post=models.CharField(max_length=100, default='')

    
 
class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, password, **extra_fields)
# 
    
class utilisateur(models.Model):
    matricule=models.AutoField(primary_key=True)
    email=models.EmailField(max_length=50, default='')
    first_name=models.CharField(max_length=50, default='')
    last_name=models.CharField(max_length=50, default='')
    sex =models.CharField(max_length=50, default='')
    adress=models.CharField(max_length=50, default='')
    phone=models.CharField(max_length=50, default='')
    username=models.CharField(max_length=50, default='')
    password=models.CharField(max_length=50, default='')
    activitys=models.TextField(max_length=1000,default='')
    last_login=models.CharField(max_length=50, default='')
    titre=models.CharField(max_length=50, default='')
    skype=models.CharField(max_length=50, default='')
    organisation=models.CharField(max_length=50, default='')
    user_type=models.CharField(max_length=50, default='student')
    profile_pic=models.CharField(max_length=500, default='default-pic.jpg')
    date_souscription=models.DateField(default=datetime.today().strftime('%F'))
    is_online = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
class souscription_formation(models.Model):
    dmd_souscription_id=models.AutoField(primary_key=True)
    formation_id=models.ForeignKey(formation, on_delete=models.CASCADE)
    matricule=models.ForeignKey(utilisateur, on_delete=models.CASCADE)
    operator=models.CharField(max_length=50, default='UNSPECIFIED')
    ref_transact=models.CharField(max_length=100, default='UNSPECIFIED')
    souscription_status=models.CharField(max_length=50, default='Waiting')
    date_souscription=models.DateField(default=datetime.today().strftime('%F'))
    date_modification=models.CharField(max_length=50, default='')


    
class paiement(models.Model):
    transaction_id=models.AutoField(primary_key=True)
    date_paiement=models.DateField(default=timezone.now)
    matricule = models.ForeignKey(utilisateur, on_delete=models.CASCADE, null=True)
    montant=models.IntegerField(default=0)
    ref_transact=models.CharField(max_length=100, unique=True)
    formation_id=models.ForeignKey(formation, on_delete=models.CASCADE)
    sender=models.CharField(max_length=50, default='UNSPECIFIED')
    receiver=models.CharField(max_length=50, default='UNSPECIFIED')
    transact_type=models.CharField(max_length=50, default='UNSPECIFIED')
    remarque=models.TextField(max_length=500, default='AUCUNE')

class Student_progess(models.Model):
    matricule=models.IntegerField(default=0)
    chap_id = models.AutoField(primary_key=True)
    frmt_id = models.CharField(max_length=100, default='')
    status = models.CharField(max_length=100, default='WAITING')

class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    formation_id=models.ForeignKey(formation, on_delete=models.CASCADE,null=True)
    chap_id=models.ForeignKey(chapitre, on_delete=models.CASCADE,null=True)
    question_text = models.CharField(max_length=500)
    answers=ArrayField(models.CharField(max_length=100), blank=True, null=True)

class Answer_possible(models.Model):
    answer_id = models.AutoField(primary_key=True)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=500, default='')
    answer_alias = models.CharField(max_length=50, default='')
    
class Notes(models.Model):
    note_id = models.AutoField(primary_key=True)
    matricule=models.ForeignKey(utilisateur, on_delete=models.CASCADE,null=True)
    formation_id=models.ForeignKey(formation, on_delete=models.CASCADE,null=True)
    chap_id=models.ForeignKey(chapitre, on_delete=models.CASCADE,null=True)
    note=models.IntegerField(default='0')
    
class Video_chap(models.Model):
    video_id = models.AutoField(primary_key=True)
    formation_id=models.ForeignKey(formation, on_delete=models.CASCADE,null=True)
    chap_id=models.ForeignKey(chapitre, on_delete=models.CASCADE,null=True)
    # 
    order=models.IntegerField(default=0)
    titre = models.TextField(default='UNDEFINED')
    description = models.TextField(default='Description du chapitre ...')
    cours_content = models.TextField(default='UNUPLOADED')
    exemple_content = models.TextField(default='UNUPLOADED')
    duree_min = models.CharField(max_length=100, default='UNDEFINED')
    date_creation = models.DateTimeField(default=timezone.now) 
    
class Atelier(models.Model):
    atelier_id=models.AutoField(primary_key=True)
    titre=models.CharField(max_length=500, default='')
    date_creation=models.DateField(default=timezone.now) 
    date_debut=models.DateField(default=None) 
    lieu=models.CharField(max_length=100, default='')
    date_fin=models.DateField(default=None) 
    heure_debut=models.CharField(max_length=20, default='8')
    heure_fin=models.CharField(max_length=20, default='17')
    type=models.CharField(max_length=200, default='UNDEFINED')
    price=models.IntegerField(default=0)
    nb_place=models.IntegerField(default=12)
    img= models.TextField(default='UNUPLOADED')
    description= models.TextField(default='UNUPLOADED')
    
class Souscription_atelier(models.Model):
    souscription_id=models.AutoField(primary_key=True)
    matricule=models.ForeignKey(utilisateur, on_delete=models.CASCADE)
    atelier_id=models.ForeignKey(Atelier, on_delete=models.CASCADE)
    date_inscription=models.DateField(default=timezone.now) 
    priority=models.IntegerField(default=1)
    class Meta:
        unique_together = ('matricule', 'atelier_id')

    def __str__(self):
        return f"{self.matricule} - {self.atelier_id}"