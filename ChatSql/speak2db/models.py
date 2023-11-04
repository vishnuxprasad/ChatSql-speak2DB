from django.db import models

class DatabaseConnection(models.Model):
    database_type = models.CharField(max_length=20)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    host = models.CharField(max_length=100)
    port = models.IntegerField()
    name = models.CharField(max_length=100)
