from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=150)
    cover = models.ImageField(upload_to='images/')
    book = models.FileField(upload_to='books/')

    def __str__(self):
        return self.title

class DS(models.Model):
    title = models.CharField(max_length=150)
    dsimg = models.ImageField(upload_to='imgDS/')
    book = models.FileField(upload_to='filles/')

    def __str__(self):
        return self.title

class AB(models.Model):
    title = models.CharField(max_length=150)
    abimg = models.ImageField(upload_to='imgDS/')
    book = models.FileField(upload_to='filles/')

    def __str__(self):
        return self.title

class Skill(models.Model):
    title = models.CharField(max_length=150)
    skillimg = models.ImageField(upload_to='imagesSkill/')
    book = models.FileField(upload_to='fileSkill/')
