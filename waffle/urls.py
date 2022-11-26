from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('get-10/', views.Get10View.as_view()),
    path('get-all/', views.GetAllView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
