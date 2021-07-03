from django.urls import path

from . import views


urlpatterns = [
    path('', views.index_view, name='add new view'),
    path('<str:redirect_pattern>/', views.redirect_view, name='redirect view'),
]
