from django.db import models

# Create your models here.
from django.db import models

class Goods(models.Model):
    gname = models.CharField(null=False,max_length=256)
    gprice = models.FloatField(null=False,)
    gcatalog = models.CharField(null=True,max_length=256)
    # gsales = models.CharField(null=True,max_length=256)
    gvocation = models.CharField(null=True,max_length=256)
    gshort_details = models.CharField(null=False,max_length=2048)
    glong_details = models.CharField(null=False,max_length=4056)
    gpub_time = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return self.gname
