from . import views
from django.urls import path


urlpatterns = [
    path('', views.add_new_url_view, name='add new view'),
    path('<str:following_pattern>/', views.redirect_view, name='redirect view')
]
