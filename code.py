from django.db import models

class PyContent(models.Model):
  headline = models.CharField(max_length=300)
  img = models.URLField(null=True, blank=True)
  url = models.TextField()
  def __str__(self):
    return self.headline

#Content1, 2, and 3 are your content topics

class Content1(models.Model):
  headline = models.CharField(max_length=300)
  img = models.URLField(null=True, blank=True)
  url = models.TextField()
  def __str__(self):
    return self.headline
 
class Content2(models.Model):
  headline = models.CharField(max_length=300)
  img = models.URLField(null=True, blank=True)
  url = models.TextField()
  def __str__(self):
    return self.headline
 
class CovidContent(models.Model):
  headline = models.CharField(max_length=300)
  img = models.URLField(null=True, blank=True)
  url = models.TextField()
  def __str__(self):
    return self.headline
    
Py manage.py makemigrations
Py manage.py migrate
