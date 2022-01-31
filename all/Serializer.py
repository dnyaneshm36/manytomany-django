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



class PersonSerializer(serializers.ModelSerializer):
    # persons_in_group=GroupSerializer(many=True, read_only=True)
    persons_in_group=serializers.StringRelatedField(many=True)
    class Meta:
        model = Person
        fields = [
            'id',
            'name',
            'persons_in_group'
        ]
        depth=1

class MembershipSerializer(serializers.ModelSerializer):
    Group=GroupSerializer( )
    class Meta:
        model = Membership
        fields = [
            'id',
            'Person',
            'Group',
            'date_joined',
            'invite_reason'
        ]
        depth=2     