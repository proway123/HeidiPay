from django.urls import path
from . import views

urlpatterns = [
    path('top-up/', views.TopUp.as_view()),
    path('payment/', views.Payment.as_view()),
]
