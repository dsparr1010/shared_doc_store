from django.contrib import admin
from .models import Topic, Document, Folder

admin.site.register(Topic)
admin.site.register(Document)
admin.site.register(Folder)
