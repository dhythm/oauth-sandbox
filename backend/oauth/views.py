import requests
from authlib.integrations.base_client import OAuthError
from authlib.integrations.django_client import OAuth
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from oauth.models import Token


oauth = OAuth()
oauth.register(
    name="sap",
    access_token_url=settings.AUTHLIB_OAUTH_CLIENTS["sap"]["access_token_url"],
)


@api_view(["GET"])
def hello(request):
    return Response(
        {"message": "Hello, world!", "sap": settings.AUTHLIB_OAUTH_CLIENTS["sap"]},
        status=200,
    )


@api_view(["GET"])
def get_users(request):
    token = Token.objects.first()
    if not token:
        raise OAuthError("invalid_token", "Token not found")

    # print(token.__dict__)
    # response = oauth.sap.get(
    #     "https://us.api.concursolutions.com/api/v3.1/expense/reports",
    #     token=token.access_token,
    # )

    # return Response(response.json(), status=200)

    response = requests.get(
        token.geolocation + "/profile/identity/v4/Users",
        headers={"Authorization": f"Bearer {token.access_token}"},
    )
    print(response.json())
    return Response({}, status=200)


@api_view(["GET"])
def authorize_sap(request):
    error = request.GET.get("error")
    if error:
        description = request.GET.get("error_description")
        raise OAuthError(error, description)

    data = {
        "client_id": settings.AUTHLIB_OAUTH_CLIENTS["sap"]["client_id"],
        "client_secret": settings.AUTHLIB_OAUTH_CLIENTS["sap"]["client_secret"],
        "grant_type": settings.AUTHLIB_OAUTH_CLIENTS["sap"]["grant_type"],
        "username": settings.AUTHLIB_OAUTH_CLIENTS["sap"]["username"],
        "password": settings.AUTHLIB_OAUTH_CLIENTS["sap"]["password"],
    }

    response = requests.post(
        settings.AUTHLIB_OAUTH_CLIENTS["sap"]["access_token_url"], data=data
    )

    Token.objects.all().delete()
    Token.objects.create(**response.json())

    token = response.json()["access_token"]

    data = {"access_token": token}

    return Response(data, status=200)
