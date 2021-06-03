from . import views
from django.urls import path

urlpatterns = [
    path('', views.input_form, name='input form'),
    path('<str:getted_short_url>/', views.redirect_view, name='redirect view')
]
