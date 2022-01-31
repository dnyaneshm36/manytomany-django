from django.shortcuts import render

# Create your views here.
from rest_framework import generics,mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny

from .models import *
from .Serializer import *

# edit required .

class PersonAPIView(mixins.CreateModelMixin,generics.ListAPIView): #crea te list 
    permission_classes        =[AllowAny]
    authentication_classes    =[]
    serializer_class          =PersonSerializer

    def get_queryset(self):
        qs = Person.objects.all()
        query = self.request.GET.get('q')

        if query is not None:
            qs = qs.filter(content__icontains = query)
        return qs

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class PersonDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin , generics.RetrieveAPIView):
    # permission_classes        =[IsAuthenticated]
    # authentication_classes    =[BasicAuthentication]
    serializer_class          =PersonSerializer
    
    queryset                   =Person.objects.all()

    def put(self, request, *args, **kwargs):
        return  self.update(request,*args,**kwargs)
    
    def patch(self, request, *args, **kwargs):
        return  self.partial_update(request,*args,**kwargs)

    def delete(self, request, *args, **kwargs):
        return  self.destroy(request,*args,**kwargs)

class GroupAPIView(mixins.CreateModelMixin,generics.ListAPIView): #crea te list 
    permission_classes        =[AllowAny]
    authentication_classes    =[]
    serializer_class          =GroupSerializer

    def get_queryset(self):
        qs = Group.objects.all()
        query = self.request.GET.get('q')

        if query is not None:
            qs = qs.filter(content__icontains = query)
        return qs

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class GroupDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin , generics.RetrieveAPIView):
    # permission_classes        =[IsAuthenticated]
    # authentication_classes    =[BasicAuthentication]
    serializer_class          =GroupSerializer
    
    queryset                   =Group.objects.all()

    def put(self, request, *args, **kwargs):
        return  self.update(request,*args,**kwargs)
    
    def patch(self, request, *args, **kwargs):
        return  self.partial_update(request,*args,**kwargs)

    def delete(self, request, *args, **kwargs):
        return  self.destroy(request,*args,**kwargs)


class MembershipAPIView(mixins.CreateModelMixin,generics.ListAPIView): #crea te list 
    permission_classes        =[AllowAny]
    authentication_classes    =[]
    serializer_class          =MembershipSerializer

    def get_queryset(self):
        qs = Membership.objects.all()
        query = self.request.GET.get('q')

        if query is not None:
            qs = qs.filter(content__icontains = query)
        return qs

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class MembershipDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin , generics.RetrieveAPIView):
    # permission_classes        =[IsAuthenticated]
    # authentication_classes    =[BasicAuthentication]
    serializer_class          =MembershipSerializer
    
    queryset                   =Membership.objects.all()

    def put(self, request, *args, **kwargs):
        return  self.update(request,*args,**kwargs)
    
    def patch(self, request, *args, **kwargs):
        return  self.partial_update(request,*args,**kwargs)

    def delete(self, request, *args, **kwargs):
        return  self.destroy(request,*args,**kwargs)