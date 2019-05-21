from django.db import models
from django.contrib.auth.models import User


class Blog_details(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    author=models.CharField(max_length=100,default=User)
    title=models.CharField(max_length=100)
    descrription=models.CharField(max_length=1000)
    date_pub=models.DateTimeField(auto_now_add=True)
    time_stamp=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def slice(self):
        return self.descrription[:50]+'....'

    class Meta:
        verbose_name_plural='Blog_Details'
