from django.db import models

# Create your models here.
from django.db import models

class Goods(models.Model):
    gname = models.CharField(null=False,max_length=256)
    gprice = models.FloatField(null=False,)
    gmain_catalog = models.CharField(null=True,max_length=256)
    gsales = models.CharField(null=True,max_length=256)
    gvocation = models.CharField(null=True,max_length=256)

    def __str__(self):
        return self.gname

class Catalog(models.Model):
    pass