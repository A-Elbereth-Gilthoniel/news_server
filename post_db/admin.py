from django.contrib import admin

from post_db.models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)
