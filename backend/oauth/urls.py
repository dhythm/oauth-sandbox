from django.urls import path

from oauth.views import authorize_sap, login_sap

urlpatterns = [
    path("sap/login/", login_sap, name="login_sap"),
    path("sap/authorize/", authorize_sap, name="authorize_sap"),
]
