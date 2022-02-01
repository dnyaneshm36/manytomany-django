from dataclasses import field
from tokenize import group
from rest_framework import serializers
from .models import *




class GroupSerializer(serializers.ModelSerializer):
    # members=PersonSerializer(many=True,read_only=True)
    class Meta:
        model = Group
        fields = [
            'id',
            'name',
            'Person',
        ]
        # read_only_fields=[
        # 'Person',
        # ]
        depth=1


class Group_used_by_PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = [
            'id',
            'name'
        ]


class PersonSerializer(serializers.ModelSerializer):
    # persons_in_group=GroupSerializer(many=True, read_only=True)
    persons_in_group=Group_used_by_PersonSerializer(many=True,read_only=True)
    class Meta:
        model = Person
        fields = [
            'id',
            'name',
            'persons_in_group'
        ]
        depth=1

# from drf_writable_nested.serializers import WritableNestedModelSerializer,UniqueFieldsMixin,NestedUpdateMixin
# from drf_writable_nested.serializers import *
class Person_userby_MembershipSerializer(
        serializers.ModelSerializer):
    class Meta:
        model = Person
        fields =[ 'id','name']

class Group_used_by_MembershipSerializer(
        serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = [
            'id','name'
        ]


class MembershipreadonlySerializer(serializers.ModelSerializer):
    Person = Person_userby_MembershipSerializer(many=False,read_only=True)
    Group=Group_used_by_MembershipSerializer( many = False,read_only=True)
    class Meta:
        model = Membership
        fields = [
            'id',
            'Person',
            'Group',
            'date_joined',
            'invite_reason'
        ]

class MembershipSerializer(serializers.ModelSerializer):
    Person = serializers.PrimaryKeyRelatedField(many=False,queryset=Person.objects.all())
    Group=serializers.PrimaryKeyRelatedField( many = False,queryset=Group.objects.all())
    class Meta:
        model = Membership
        fields = [
            'id',
            'Person',
            'Group',
            'date_joined',
            'invite_reason'
        ]