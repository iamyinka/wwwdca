from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('courses/', views.courses, name="courses"),
    path('contact_us/', views.contact_us, name="contact_us"),
    path('course/<slug:slug>/', views.course_detail, name="course_detail"),
    path('faqs/', views.faqs, name="faqs"),
    path('freetaster/', views.freetaster, name="freetaster"),
    path('work_experience_program/', views.work_experience_program, name="wep"),
]
