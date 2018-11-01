from django.contrib import admin

# Register your models here.
#telling django to display posts app in admin page
from .models import Post

admin.site.register(Post)
