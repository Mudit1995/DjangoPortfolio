from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length = 25)
    email = models.EmailField()
    description = models.TextField()
    phonenumber = models.CharField(max_length = 10)

    def __str__(self) -> str:
        return self.name




class blogs(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    authorname = models.CharField(max_length=15)
    date = models.DateField(auto_now_add = True)
    image = models.ImageField(upload_to = 'blog', blank=True,null=True)


    def __str__(self) -> str:
        return self.title 


class Internship(models.Model):
    full_name = models.CharField(max_length=69)
    USN =  models.CharField(max_length=69)
    email =  models.CharField(max_length=69)
    collegename =  models.CharField(max_length=69)
    offer_statsu =models.CharField(max_length=69)
    start_date =  models.CharField(max_length=69)
    end_date =  models.CharField(max_length=69)
    project_report =  models.CharField(max_length=69)
    date = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.usn
    
