from django.db import models

# Create your models here.
class fun(models.Model):
    m_year=models.IntegerField(blank=False,max_length=4),
    m_month=models.CharField(blank=False,max_length=20)