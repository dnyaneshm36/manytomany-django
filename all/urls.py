import imp
from django.urls import path,include
from all import views
urlpatterns = [
            path("person", views.PersonAPIView.as_view(),name="Person"),
            path("person-CRUD/<int:pk>", views.PersonDetailAPIView.as_view(),name="person_crud"),
            path("group", views.GroupAPIView.as_view(),name="group"),
            path("group-CRUD/<int:pk>", views.GroupDetailAPIView.as_view(),name="group_crud"),
            path("membership", views.MembershipAPIView.as_view(),name="group"),
            path("membership-CRUD/<int:pk>", views.MembershipDetailAPIView.as_view(),name="group_crud"),
]