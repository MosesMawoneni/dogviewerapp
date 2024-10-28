from django.db import models

class Dog(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=100,blank=True,null=True)
    street = models.CharField(max_length=100,blank=True,null=True)
    description = models.TextField()
    photo = models.ImageField(upload_to="images/")
    value = models.DecimalField(max_digits=10,decimal_places=2)
    owner =models.CharField(max_length=100)

    def __str__(self):
        return self.name

