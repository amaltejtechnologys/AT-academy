from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('course/', views.course_list, name='course_list'),
    path('courses/<slug:slug>/', views.course_detail, name='course_detail'),
    path('branch/<slug:slug>/', views.branch_detail, name='branch_detail'),
    path('discover/about-us/', views.about, name='about'),
    path('discover/contact-us/', views.contact, name='contact'),
    path('discover/gallery/', views.gallery, name='gallery'),
    path('discover/videos/', views.videos, name='videos'),
    path('blogs/', views.blog_list, name='blog_list'),
    path('blogs/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('placements/alumni/', views.alumni, name='alumni'),
    path('placements/recruiters/', views.recruiters, name='recruiters'),
    path('success-stories/', views.success_stories, name='success_stories'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('policyagreements/terms-of-service/', views.terms_of_service, name='terms_of_service'),
    path('apply-for-jobs/', views.apply_jobs, name='apply_jobs'),
    path('find-my-course/', views.find_course, name='find_course'),
    path('api/enquiry/', views.submit_enquiry, name='submit_enquiry'),
    path('api/callback/', views.submit_callback, name='submit_callback'),
    path('api/recruiter/', views.submit_recruiter, name='submit_recruiter'),
    path('api/brochure/<slug:slug>/', views.download_brochure, name='download_brochure'),
]
