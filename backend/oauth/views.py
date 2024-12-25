import os
from authlib.integrations.base_client import OAuthError
from authlib.integrations.django_client import OAuth
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response


oauth = OAuth()
oauth.register(
    name="sap",
    access_token_url=settings.AUTHLIB_OAUTH_CLIENTS["sap"]["access_token_url"],
    authorize_url=settings.AUTHLIB_OAUTH_CLIENTS["sap"]["authorize_url"],
    jwks_uri=settings.AUTHLIB_OAUTH_CLIENTS["sap"]["jwks_uri"],
)


@api_view(["GET"])
def hello(request):
    return Response(
        {"message": "Hello, world!", "sap": settings.AUTHLIB_OAUTH_CLIENTS["sap"]},
        status=200,
    )


@api_view(["GET"])
def login_sap(request):
    redirect_uri = request.build_absolute_uri(os.getenv("SAP_REDIRECT_URI"))
    return oauth.sap.authorize_redirect(request, redirect_uri)


@api_view(["GET"])
def authorize_sap(request):
    error = request.GET.get("error")
    if error:
        description = request.GET.get("error_description")
        raise OAuthError(error, description)

    data = {
        "grant_type": "authorization_code",
        "code": request.GET.get("code"),
        "client_id": settings.AUTHLIB_OAUTH_CLIENTS["sap"]["client_id"],
        "redirect_uri": settings.AUTHLIB_OAUTH_CLIENTS["sap"]["redirect_uri"],
        "client_secret": settings.AUTHLIB_OAUTH_CLIENTS["sap"]["client_secret"],
    }

    response = request.post(
        settings.AUTHLIB_OAUTH_CLIENTS["sap"]["access_token_url"], data=data
    )

    token = response.json()["access_token"]

    data = {"access_token": token}

    return Response(data, status=200)
