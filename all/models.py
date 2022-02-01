from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    Person = models.ManyToManyField(Person, through='Membership',related_name='persons_in_group')

    def __str__(self):
        return self.name

class Membership(models.Model):
    Person = models.ForeignKey(Person, on_delete=models.CASCADE)
    Group = models.ForeignKey(Group, on_delete=models.CASCADE)  #to avoid deleting object when field aare change
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)