from django.db import models
from django.contrib.auth.models import User

# class Website(models.Model):
#     def __str__(self):
#         return self.url[:30]
    
#     url = models.URLField()


class UserWebsite(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)  
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    clicks = models.IntegerField(default=0)
    data_sent = models.FloatField(default=0)
    data_received = models.FloatField(default=0)

    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     existing_website = Website.objects.filter(url=self.url).first()

    #     if not existing_website:
    #         existing_website = Website.objects.create(url=self.url)

    #     self.url = existing_website

    #     super().save(*args, **kwargs)