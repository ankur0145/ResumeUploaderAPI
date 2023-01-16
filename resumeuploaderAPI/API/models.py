from django.db import models

class Profile(models.Model):
    name=models.CharField(max_length=10)
    email=models.EmailField()
    DOB=models.DateField(auto_now=False,auto_now_add=False)
    State=models.CharField(max_length=10)
    gender=models.CharField(max_length=10)
    location=models.CharField(max_length=10)
    pimage=models.ImageField(upload_to='pimages',blank=True)
    rdoc=models.FileField(upload_to='rdocs', blank=True)


