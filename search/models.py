from django.db import models

class Keyword(models.Model):
    text = models.TextField(default='')