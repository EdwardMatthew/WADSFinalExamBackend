from django.db import models

# Create your models here.
class NewProd(models.Model):
    name = models.CharField(max_length=60)
    desc = models.CharField(max_length=60)

    def __str__(self):
        return self.name, self.desc

class Login(models.Model):
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=60)

    def __str__(self):
        return self.email, self.password

class Register(models.Model):
    email = models.CharField(max_length=60) 
    password = models.CharField(max_length=60)

    def __str__(self):
        return self.email, self.password
