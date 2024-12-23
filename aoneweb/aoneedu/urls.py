from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"), 
    path("reg/", views.examsform, name="examsform"), 
    path("rules/", views.rules_v, name="rules"),
    path("aboutus/", views.aboutus_v, name="aboutus"),
    path('register/', views.register_view, name="register"), 
    path('listform/<aoneEducational_id>', views.formviews, name="listform"), 
    path('updateforms/<aoneEducational_id>', views.updateforms, name="updateforms"), 
    path('viewedit/', views.viewedit, name="viewedit"), 
    path('courses/', views.coursespage, name="courses"), 
    path('logout/', views.loguserout, name="logout"), 
]