from django.db import models
from django.contrib.auth import get_user_model
import secrets

# Create your models here.

User = get_user_model()

class ScraperFile(models.Model):
    owner = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'scraper_files')
    file_id = models.SlugField(blank= True, max_length= 25)
    name = models.CharField(max_length=50, blank= True)
    download_link = models.CharField(max_length=200, blank= True)
    created_on = models.DateTimeField(auto_now= True)
    modified_on = models.DateField(auto_now_add= True)

    class Meta:
        ordering = ['-created_on',]

class Notifications(models.Model):
    owner = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'notifications')
    file_id = models.CharField(max_length= 25, blank= True)
    document = models.ForeignKey(ScraperFile, blank= True, null= True, on_delete= models.CASCADE, related_name= 'notifications')
    header = models.CharField(max_length= 50, blank= True)
    body = models.CharField(max_length= 150, blank= True)
    created_on = models.DateTimeField(auto_now_add= True, null= True)
    viewed_status = models.IntegerField(default= 2)

    class Meta:
        ordering = ['-created_on',]