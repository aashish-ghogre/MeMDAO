from django.db import models


# Create your models here.
class Team(models.Model):
    id = models.BigIntegerField(unique=True,primary_key=True,auto_created=True)
    name = models.CharField(max_length=255,unique=True)


class Test(models.Model):
    test = models.CharField(max_length=10)
    class Meta:
        db_table='test'
    def __str__(self):
        return ('%d %s') %(self.id ,self.test)