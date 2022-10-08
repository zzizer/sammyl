from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("sign_in", views.signin, name='sign_in'),
    path("register_account", views.register, name='register_account'),
    path("sign_out/", views.signout, name='sign_out'),
]
