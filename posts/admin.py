from django.contrib import admin

# Register your models here.
from posts.models import Post

class PostAdmin(admin.ModelAdmin):
    empty_value_display = '---empty---'
    list_display = ["__str__", "timestamp", "content", "id"]

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)
