from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    business_obj = models.TextField()
    tech_details = models.TextField()
    tags = TaggableManager()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['client']