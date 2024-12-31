from django.urls import path

from oauth.views import (
    authorize_sap,
    get_me,
    get_lists,
    get_users,
    get_users_in_identity,
    hello,
)

urlpatterns = [
    path("sap/authorize/", authorize_sap, name="authorize_sap"),
    path("sap/hello/", hello, name="hello"),
    path("sap/me/", get_me, name="get_me"),
    path("sap/users/", get_users, name="get_users"),
    path("sap/identity-users/", get_users_in_identity, name="get_users_in_identity"),
    path("sap/lists/", get_lists, name="get_lists"),
]
