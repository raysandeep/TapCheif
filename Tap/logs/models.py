from django.db import models



class Search(models.Model):
    word = models.CharField(max_length=30, blank=True, default='')
    paragraph = models.TextField(max_length=3000, blank=True, default='')
