from django.urls import path

from oauth.views import authorize_sap, hello

urlpatterns = [
    path("sap/hello/", hello, name="hello"),
    path("sap/authorize/", authorize_sap, name="authorize_sap"),
]
