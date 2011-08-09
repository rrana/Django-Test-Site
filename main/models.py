from django.db import models

# Create your models here.
class Category(models.Model):
    Name = models.CharField(max_length=255)
    def __unicode__(self):
        return self.Name
    class Admin:
        pass
    class Meta:
        verbose_name_plural = "Categories"
