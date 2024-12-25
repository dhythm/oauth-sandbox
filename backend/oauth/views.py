import os
from authlib.integrations.base_client import OAuthError
from authlib.integrations.django_client import OAuth
from rest_framework.decorators import api_view
from rest_framework.response import Response


oauth = OAuth()
oauth.register(
    name="sap",
    access_token_url=os.getenv("SAP_ACCESS_TOKEN_URL"),
    authorize_url=os.getenv("SAP_AUTHORIZE_URL"),
    jwks_uri=os.getenv("SAP_JWKS_URI"),
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
        "client_id": os.getenv("SAP_CLIENT_ID"),
        "redirect_uri": os.getenv("SAP_REDIRECT_URI"),
        "client_secret": os.getenv("SAP_CLIENT_SECRET"),
    }

    response = request.post(os.getenv("SAP_ACCESS_TOKEN_URL"), data=data)

    token = response.json()["access_token"]

    data = {"access_token": token}

    return Response(data, status=200)
