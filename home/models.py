from django.db import models

# Create your models here.
class Contact(models.Model):
     sno= models.AutoField(primary_key=True)
     name= models.CharField(max_length=255)
     phone= models.CharField(max_length=13)
     email= models.CharField(max_length=100)
     content= models.TextField()
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

     def __str__(self):
          return "Message from " + self.name + ' - ' + self.email
          
class Addblog(models.Model):
    sno= models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=14)
    slug=models.CharField(max_length=130)
    content=models.TextField()
class CoepAddblog(models.Model):
    coepsno= models.AutoField(primary_key=True)
    coeptitle=models.CharField(max_length=255)
    coepauthor=models.CharField(max_length=14)
    coepslug=models.CharField(max_length=130)
    coepcontent=models.TextField()

