from django.shortcuts import render
from rest_framework import permissions,authentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from .models import Scheme
from .serializers import SchemeSerializer


FIELD_NOT_EMPTY = "field should not be empty."
BAD_REQUEST = status.HTTP_400_BAD_REQUEST
CREATE_REQUEST = status.HTTP_201_CREATED
GET_REQUEST = status.HTTP_200_OK
USER_EXIST = "with the given credentials already exist."
USER_NOT_EXIST = "with the given credentials does not exist."


class SchemeViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    authentication_classes = [authentication.TokenAuthentication]
    model = Scheme
    serializer_class = SchemeSerializer
    queryset = Scheme.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['scheme_name','department_name','last_date','income_criteria','caste_criteria','region_criteria','education_criteria']
    search_fields = ['scheme_name','department_name','last_date','income_criteria','caste_criteria','region_criteria','education_criteria',]
    ordering = ['last_date']

    def create(self, request):
        serializer = SchemeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)