"""View for handling Swole User Requests"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

class SwoleUserView(ViewSet):
    # def create
    # def list?
    # def retrieve?