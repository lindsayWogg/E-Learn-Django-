from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf.urls import handler404
#from django.conf.urls import url
handler404 = views.error_404

urlpatterns = [
    path('', views.home, name='home'),
    path('webadmin/send_message/', views.sendmessage, name='send'),
    
    path('nfablog/', views.home, name='nfablog'),
    path('sendmessage/', views.sendmessage, name='sendmessage'),
    path('nfalogin/', views.user_login, name='nfalogin'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard2/', views.dashboard2, name='dashboard2'),
    path('show_course/<str:formation_id>', views.show_free_formation, name='show_course'),
    path('show_chapter/<int:chap_id>/<str:frmt_id>/', views.show_chapter, name='show_chapter'),
    path('show_quizz/<int:chap_id>/<str:frmt_id>/', views.show_quizz, name='show_quizz'),
    path('formations/', views.formation_payante, name='formations'),
    path('formations-availables/', views.formations_available, name='formations-availables'),
    path('send_subscription_request/', views.send_subscription_request, name='send_subscription_request'),
    # path('details_course/<str:formation_id>', views.show_formation_details, name='details_course'),
    path('details_course', views.show_formation_details, name='details_course'),
    path('view_profile', views.prifile_view, name='view_profile'),
    path('update_activity', views.update_activity, name='update_activity'),
    path('update_user_information', views.update_user_information, name='update_user_information'),
    path('update_user_password', views.update_user_password, name='update_user_password'),
    path('calendar', views.calendar_view, name='calendar'),
    path('advanced_calendar_view', views.advanced_calendar_view, name='advanced_calendar_view'),

    ############################ADMINISTRATION################################
    path('admin_dashboard/', views.administration, name='admin_dashboard'),
    path('gestion_utilisateurs/', views.gestion_utilisateur, name='gestion_utilisateurs'),
    path('subscription/', views.subscription, name='subscription'),
    path('validate_subscription/', views.validate_subscription, name='validate_subscription'),
    path('deny_subscription/', views.deny_subscription, name='deny_subscription'),
    path('show_user/<int:matricule>', views.about_user, name='show_user'),
    path('creation_atelier/', views.creation_atelier, name='creation_atelier'),
    path('gestion_formation/', views.gestion_formation, name='gestion_formation'),
    path('free_formation/', views.gestion_free_formation, name='free_formation'),
    path('paid_formation/', views.gestion_paid_formation, name='paid_formation'),
    path('create_formation/', views.create_formation, name='create_formation'),
    path('create_chapter/', views.create_chapter, name='create_chapter'),
    path('add_course/', views.add_course, name='add_course'),
    path('edit_formation/', views.edit_formation, name='edit_formation'),
    path('delete_formation/', views.delete_formation, name='delete_formation'),
    path('subscribe_course/', views.subscribe_course, name='subscribe_course'),
    path('join_course/', views.subscribe_course_already_signed_up, name='join_course'),
    path('subscribe_formation_demand/', views.subscribe_formation_demand, name='subscribe_formation_demand'),
    path('gestion_paiements/', views.gestion_paiement, name='gestion_paiements'),
    path('validate_formation_subscription/', views.validate_formation_subscription, name='validate_formation_subscription'),
    path('deny_formation_subscription/', views.deny_formation_subscription, name='deny_formation_subscription'),
    path('set_waiting/', views.make_wait_formation_subscription, name='set_waiting'),
    path('getsion_quizz/', views.getsion_quizz, name='getsion_quizz'),
    path('create_quizz/', views.create_quizz, name='create_quizz'),
    path('validate_quizz/', views.validate_quizz, name='validate_quizz'),
    path('update_profile_picture/', views.update_profile_picture, name='update_profile_picture'),
    path('gestion_atelier/', views.gestion_atelier, name='gestion_atelier'),
    path('details_atelier/', views.details_atelier, name='details_atelier'),
    path('del_subs_atelier/', views.del_user_from_atelier, name='del_subs_atelier'),
    path('edit_atelier/', views.edit_atelier, name='edit_atelier'),
    path('delete_atelier/', views.delete_atelier, name='delete_atelier'),
    path('ateliers/', views.voir_atelier, name='ateliers'),
    path('inscription_atelier/', views.inscription_atelier, name='inscription_atelier'),
    path('exporter-pdf/<int:atelier_id>', views.exporter_pdf, name='exporter_pdf'),
    path('exporter-pdf-post/', views.exporter_pdf_post, name='exporter_pdf_post'),
    path('update_formation_presentation/', views.update_formation_presentation, name='update_formation_presentation'),
    path('update_chapter_presentation/', views.update_chapter_presentation, name='update_chapter_presentation'),
    path('update_course_content/', views.update_course_content, name='update_course_content'),
    path('delete_formation_presentation/', views.delete_formation_presentation, name='delete_formation_presentation'),
    path('delete_chapter/', views.delete_chapter, name='delete_chapter'),
    path('delete_course/', views.delete_course, name='delete_course'),
    path('update_chapter_title/', views.update_chapter_name, name='update_chapter_title'),
    path('update_course_title/', views.update_course_name, name='update_course_title'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
