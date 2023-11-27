from django.urls import path
from . import views
urlpatterns=[
    path("addexp/",views.addexp,name="addexp"),
    path("login/",views.login,name="login"),
    path("signup/",views.signup,name="signup"),
    path("incspent/",views.incspent,name="incspent"),
    path("",views.welcome,name="welcome"),
    path("logout/",views.logout,name="logout"),
]