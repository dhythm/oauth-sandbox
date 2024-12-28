from django.urls import path

from oauth.views import authorize_sap, get_users, hello

urlpatterns = [
    path("sap/hello/", hello, name="hello"),
    path("sap/users/", get_users, name="get_users"),
    path("sap/authorize/", authorize_sap, name="authorize_sap"),
]
