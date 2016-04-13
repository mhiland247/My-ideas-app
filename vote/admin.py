from django.contrib import admin

# Register your models here.

from .models import Idea, Tag, Comment

admin.site.register(Idea)
admin.site.register(Tag)
admin.site.register(Comment)

