from django.db import models
from django.utils import timezone

# Create your models here.

class Tag(models.Model):
    tag = models.CharField(max_length=80, null=False, blank=False)	

    def __str__(self):
        return self.tag

class Comment(models.Model):
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def save(self):
        self.created_date = timezone.now()
        self.save()

class Idea(models.Model):
    content = models.TextField(null=False, blank=False)
    pub_date = models.DateTimeField(default=timezone.now)
    votes = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag, blank=True)
    name = models.CharField(max_length=80, blank=True, null=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def publish(self):
        self.pub_date = timezone.now()
        self.save()
