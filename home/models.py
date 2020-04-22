from django.db import models

# Create your models here.
class SmartPhones(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=400)
    specs = models.CharField(max_length=200)
    ram = models.CharField(max_length=30)
    rom = models.CharField(max_length=30)
    price = models.IntegerField()
    image = models.ImageField(upload_to='smartphones/images')

    def __str__(self):
        return self.product_name

class HomeAppliances(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=400)
    specs = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(upload_to='homeappliances/images')

    def __str__(self):
        return self.product_name

class Wearables(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=400)
    specs = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(upload_to='wearables/images')

    def __str__(self):
        return self.product_name


class Music(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=400)
    specs = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(upload_to='music/images')

    def __str__(self):
        return self.product_name

class Other(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=400)
    specs = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(upload_to='other/images')

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name