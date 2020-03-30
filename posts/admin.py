from django.contrib import admin
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["__str__", "author", "timestamp"]
    list_filter = ["updated", "timestamp", "author"]
    search_fields = ["title", "content", "author"]
    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)