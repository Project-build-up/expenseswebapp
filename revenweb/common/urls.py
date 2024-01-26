from django.urls import path
from . import views
urlpatterns=[
    path("incsal/",views.incsal,name="incsal"),
    path("login/",views.login,name="login"),
    path("signup/",views.signup,name="signup"),
    path("incspent/",views.incspent,name="incspent"),
    path("",views.welcome,name="welcome"),
    path("logout/",views.logout,name="logout"),
    path("download/",views.download,name="download"),
    path("downloadincome/",views.downloadincome,name="downloadincome"),
    path("downloadspent/",views.downloadspent,name="downloadspent"),
]