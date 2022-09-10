from django.db import models

# Create your models here.
class User(models.Model):
    frist_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    phone_number=models.CharField(max_length=11)
    user_name=models.CharField(max_length=18,null=True)

