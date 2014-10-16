from django.db import models
from django.contrib.auth.models import User

class question(models.Model):
    header = models.CharField(max_length=30)
    text = models.TextField(max_length=200)
    creationdate = models.DateTimeField(auto_now=False, auto_now_add=True)
    creator = models.ForeignKey(User)
    rating = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.header

    class Meta:
        ordering = ["-creationdate"]

class answer(models.Model):
    text = models.CharField(max_length=30)
    creator = models.ForeignKey(User)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    question = models.ForeignKey(question)
    correctanswer = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)

    def __unicode__(self):
        return self.text

    class Meta:
        ordering = ["date"]
