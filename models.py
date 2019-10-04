from django.db import models

# Create your models here.
class Fibo(models.Model):
    number = models.IntegerField()
    result = models.IntegerField()
    time = models.CharField(max_length=255)

    class Meta:
        db_table = 'fibo'

    def __unicode__(self):
        return self.number

