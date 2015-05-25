from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Details
from rest_framework import generics, filters
from rest_framework import status
from rest_framework.response import Response
import datetime
import logging
from .serializers import UserSerializer

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
            return Response(dict(error=["user_cant_not_be_added"], data=dict()),
                            status=status.HTTP_400_BAD_REQUEST)


class AddDetails(generics.ListCreateAPIView):
    """
        View to add user details
    """
    def post(self, request):
        """
            Parameters:
            {
                "father_name": "father's name",
                "mother_name": "mother's name",
                "city": "city",
                "user": "username" 
            }
        """
        self.username = request.DATA.get("user", None)
        self.father = request.DATA.get("father_name", None)
        self.mother = request.DATA.get("mother_name", None)
        self.city = request.DATA.get("city", None)

        if not self.username:
            return Response(dict(error=["username_empty"], data=dict()),
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            self.userObj = User.objects.get(username=self.username)
        except:
            self.userObj = None

        if not self.userObj:
            return Response(dict(error=["user_does_not_exists"], data=dict()),
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            self.detailObj = Details.objects.create(father_name=self.father,
                                                    mother_name=self.mother,
                                                    city=self.city,
                                                    user=self.userObj)
            self.detailObj.save()
            response_dict = dict(father_name=self.father,
                                 mother_name=self.mother,
                                 city=self.city,
                                 user=self.username)
            return Response(dict(error=[], data=response_dict), status=status.HTTP_200_OK)
        except:
            return Response(dict(error=["details_cant_not_be_saved"], data=dict()),
                            status=status.HTTP_400_BAD_REQUEST)


class UserDelete(generics.DestroyAPIView):
    """
        View to delete a user
    """
    def delete(self, request):
        """
            parameters:
            {
                "user": "username"
            }
        """
        self.username = request.DATA.get("user", None)

        if not self.username:
            return Response(dict(error=["username_empty"], data=dict()),
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            self.userObj = User.objects.get(username=self.username)
        except:
            self.userObj = None

        if not self.userObj:
            return Response(dict(error=["user_does_not_exists"], data=dict()),
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            User.objects.filter(username=self.username).delete()
            return Response(dict(error=[], data=dict(), status=status.HTTP_200_OK))
        except:
            return Response(dict(error=["user_cant_not_be_deleted"], data=dict()),
                            status=status.HTTP_400_BAD_REQUEST)


class ListAllUser(generics.ListAPIView):
    """
        List user(s) details
    """
    serializer_class = UserSerializer

    def get_queryset(self):
        """
            get query set
        """
        return User.objects.all()

    def list(self, request, *args, **kwargs):
        """
            send custom response using overriding the list method
        """
        
        response = generics.ListAPIView.list(self, request, *args, **kwargs).data
        return Response(dict(data=response, error=[]), status=status.HTTP_200_OK)


class ListUser(generics.ListAPIView):
    """
        List user details
    """
    serializer_class = UserSerializer

    def get_queryset(self):
        """
            get query set
        """
        return [User.objects.get(id=self.kwargs.get("user_id"))]

    def list(self, request, *args, **kwargs):
        """
            send custom response using overriding the list method
        """
        try:
            response = generics.ListAPIView.list(self, request, *args, **kwargs).data
        except:
            return Response(dict(data=[], error=['user_not_found']), status=status.HTTP_400_BAD_REQUEST)
        return Response(dict(data=response, error=[]), status=status.HTTP_200_OK)


class EditUser(generics.ListCreateAPIView):
    """
        View to edit user
    """
    def post(self, request):
        """
            parameters:
            {
                "username": "<user>",
                "email": "<email id>"
            }
        """
        self.username = request.DATA.get("username", None)
        self.email = request.DATA.get("email", None)

        if not self.username:
            return Response(dict(error=["username_empty"], data=dict()),
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            self.userObj = User.objects.get(username=self.username)
        except:
            self.userObj = None

        if not self.userObj:
            return Response(dict(error=["user_does_not_exists"], data=dict()),
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            self.userObj.email = self.email
            self.userObj.save()
            response_dict = dict(username=self.username, email=self.email)
            return Response(dict(error=[], data=response_dict), status=status.HTTP_200_OK)
        except:
            return Response(dict(data=[], error=['can_not_edit_user']), status=status.HTTP_400_BAD_REQUEST)




