from django.contrib import admin
from .models import Post

# Register the model to make the model visible on the admin page
admin.site.register(Post)