from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=200)
    price=models.FloatField()
    stock=models.IntegerField()
    image_url=models.CharField(max_length=2083)
class offer(models.Model):
    code=models.CharField(max_length=10)
    description=models.CharField(max_length=255)
    discount=models.FloatField()
class search(models.Model):
    search_name=models.CharField(max_length=200)

class carty(models.Model):
    name=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()
    image_url=models.CharField(max_length=2083)
class remove(models.Model):
    name=models.CharField(max_length=100)
class check(models.Model):
    name=models.CharField(max_length=100)
    phone_number=models.IntegerField()
    address=models.CharField(max_length=100)
    mail=models.EmailField()
    