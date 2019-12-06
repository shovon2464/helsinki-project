from django.contrib import admin

from .models import Blog
from .models import ReviewBlog

admin.site.register(Blog)
admin.site.register(ReviewBlog)
