# E-learning-Django

Live Link:-
https://edurekanet.herokuapp.com/   

Screenshots:- 

![Screenshot_2021-04-01 edureka ](https://user-images.githubusercontent.com/59178005/113218249-d6ba0200-929c-11eb-8ee9-40067b996f7e.png)
![Screenshot_2021-04-01 edureka (1)](https://user-images.githubusercontent.com/59178005/113218261-d9b4f280-929c-11eb-981f-9b385bb6de34.png)
![Screenshot_2021-04-01 edureka (2)](https://user-images.githubusercontent.com/59178005/113218264-db7eb600-929c-11eb-8c67-036461ad73f5.png)
![Screenshot_2021-04-01 Admin Dashboard Add Posts](https://user-images.githubusercontent.com/59178005/113218277-dde11000-929c-11eb-80a0-e17baa1c1a0f.png)
![Screenshot_2021-04-01 Admin Dashboard Add Posts(1)](https://user-images.githubusercontent.com/59178005/113218281-dfaad380-929c-11eb-963f-d293a6239f2d.png)


Features of My E-learning Platform code:-

Dynamic Slider
User Login/ Registration
Add To Cart / Remove From Cart
Add Coupons
Payment Gateway Integration
Custom Admin Panel
User Panel
Search bar
Image Size Compressor

a) User Panel

-> Purchase Courses
-> Download Certificate after completing the course
-> Watch Videos
-> Edit Profile
-> Change Password
-> Order History
-> Add To Cart, Remove from Cart.
-> Calculate Total Amount 

b) Custom Admin Panel

-> Upload Video for Particular course
-> Add Post
-> Category, Sub Category, and Sub Sub Category
-> Autoslug
-> Add Multiple Sections like FAQ or Price or Features
-> Add Discount Coupons
-> All Orders
-> All Users
-> Allow Certificates to Users, Admin has permission to enable or disable the certificate.
-> Index Categories and Post (Move post and Categories)
-> Add Dynamic Sections on Homepage
-> Add latest offers on banners
-> Add Blogs 

and many other functionalities in this project...

Before running the project, run these commands, 
 1) pip install -r requirements.txt   

 2) python manage.py migrate   

3) python manage.py runserver   

# change git credenttials
'''bash
git credential-cache exit
# Or, if credentials are stored persistently
git config --global --unset credential.helper
git credential-store --file ~/.git-credentials erase
'''

# PAT
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


# Structure technique de Next Food Africa

```mermaid
graph TD
    client[utilisateur]-->NFA
    NFA[Next Food Africa]-->python[PYTHON]
    NFA-->dcr[DOCKER]
    dcr-->db[PostgreSQL]
    python --> django[Librarie DJANGO]
    django-->mvc[Model View Controller - M.V.C]
    mvc--> model[MODELS]
    mvc --> view[VIEWS]
    mvc --> controller[Controlleur]

    view-->bootstrap[BOOTSTRAP 5]
    bootstrap-->html[HTML]
    bootstrap-->css[CSS]
    bootstrap-->js[JAVASCRIPT]
```
# Structure générale du MVC

```mermaid
graph TD
  A[Utilisateur] --> B[Django];
    B --> C[URLs];
    C --> D[Vue];
    D --> E[Modèle];
    E --> F[Base de données];
    F --> D;
    D --> C;
    C --> B;
    B --> A;
```


    
  
```mermaid
classDiagram
    class partenaires {
        - partner_id: IntegerField
        - nom: CharField
        - logo: CharField
        - Description: TextField
    }
    class formation {
        - formation_id: CharField
        - formation_img: CharField
        - formation_name: CharField
        - formation_descr: TextField
        - formation_type: CharField
        - formation_prix: IntegerField
        - formation_duree: CharField
        - created_at: CharField
    }
    class demande_inscription {
        - dmd_id: AutoField
        - matricule: IntegerField
        - formation_id: CharField
        - status: CharField
        - dmd_date: CharField
        - date_validation: CharField
        - email: EmailField
        - first_name: CharField
        - last_name: CharField
        - sex: CharField
        - adress: CharField
        - phone: CharField
        - username: CharField
        - password: CharField
        - already_signed_up: CharField
    }
    class chapitre {
        - chap_id: AutoField
        - frmt_id: CharField
        - chap_order: IntegerField
        - titre: TextField
        - description: TextField
        - cours_content: TextField
        - cours_file_type: TextField
        - exemple_content: TextField
        - exemple_file_type: TextField
        - quizz_content: TextField
        - quizz_file_type: TextField
        - duree_min: CharField
        - date_creation: DateTimeField
    }
    class objectif {
        - chap_id: IntegerField
        - frmt_id: CharField
        - objctf_id: IntegerField
        - objctf_content: TextField
        - duree_min: CharField
    }
    class quizz {
        - chap_id: IntegerField
        - frmt_id: CharField
        - quizz_id: IntegerField
        - question: TextField
        - qst_type: TextField
        - answer: TextField
        - status: BooleanField
    }
    class collabo {
        - firstname: CharField
        - lastname: CharField
        - sex: CharField
        - date_birth: DateField
        - picture: CharField
        - date_member: DateField
        - post: CharField
    }
    class utilisateur {
        - matricule: AutoField
        - email: EmailField
        - first_name: CharField
        - last_name: CharField
        - sex: CharField
        - adress: CharField
        - phone: CharField
        - username: CharField
        - password: CharField
        - last_login: CharField
        - user_type: CharField
        - profile_pic: CharField
        - date_souscription: DateField
        - is_online: BooleanField
        - is_active: BooleanField
        - is_staff: BooleanField
    }
    class souscription_formation {
        - dmd_souscription_id: AutoField
        - formation_id: CharField
        - matricule: CharField
        - operator: CharField
        - ref_transact: CharField
        - souscription_status: CharField
        - date_souscription: DateField
        - date_modification: CharField
    }
    class paiement {
        - transaction_id: AutoField
        - date_paiement: DateField
        - matricule: CharField
        - montant: IntegerField
        - ref_transact: CharField
        - formation_id: CharField
        - sender: CharField
        - receiver: CharField
        - transact_type: CharField
        - remarque: TextField
    }
    class Student_progess {
        - matricule: IntegerField
        - chap_id: AutoField
        - frmt_id: CharField
        - status: CharField
    }
 

  
  
    chapitre <|-- formation
    objectif <|-- chapitre
    quizz <|-- chapitre
    utilisateur <|-- demande_inscription
    souscription_formation <|--  utilisateur
    formation <|-- souscription_formation
    utilisateur <|-- paiement
    utilisateur <|-- Student_progess

