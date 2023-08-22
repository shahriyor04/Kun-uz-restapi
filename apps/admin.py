from django.contrib import admin

from apps.models import NewsCategory, AreaCategory, Post

admin.site.register(NewsCategory)
admin.site.register(AreaCategory)
admin.site.register(Post)
# admin.site.register(Introduction)
