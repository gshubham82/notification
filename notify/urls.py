from django.contrib import admin
from django.urls import path
from .views import NotifyView
from rest_framework.urlpatterns import format_suffix_patterns
from notify import views

urlpatterns = {
    path('notification/',views.NotifyView.as_view()),
    path('notification/<int:pk>/', views.NotifyDetail.as_view()),

}

urlpatterns= format_suffix_patterns(urlpatterns)