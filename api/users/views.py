from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Details
from rest_framework import generics, filters
from rest_framework import status
from rest_framework.response import Response
import datetime
import logging

# logger settings
logger = logging.getLogger("api.users")


class AddUser(generics.ListCreateAPIView):

    """
        View to create and add a user
    """

    def post(self, request):
        """
            Parameters:
                {
                    "username": "username",
                    "password": "password",
                    "email": "emailid"
                }
        """
        self.username = request.DATA.get("username", None)
        self.password = request.DATA.get("password", None)
        self.email = request.DATA.get("email", None)

        if not self.username:
            return Response(dict(error=["username_empty"], data=dict()),
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            self.userObj = User.objects.get(username=self.username)
        except:
            self.userObj = None

        if self.userObj:
            return Response(dict(error=["username_already_exists"], data=dict()),
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            User.objects.create_user(self.username, self.email, self.password)
            response_dict = dict(username=self.username)
            return Response(dict(error=[], data=response_dict), status=status.HTTP_200_OK)
        except:
            return Response(dict(error=["user cant not be added"], data=dict()),
                            status=status.HTTP_400_BAD_REQUEST)
