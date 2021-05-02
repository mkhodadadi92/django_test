from django.db import models
from django.contrib.auth.models import User


# # Create your models here.
# class ContactList(models.Model):
#     user_id = models.DateTimeField('date published')


class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    role = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)


class TestList(models.Model):
    name = models.CharField(max_length=100)
