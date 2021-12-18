from django.contrib import admin

# Register your models here.


# Register your models here so the admin site can pick up the new tables. It implements the crud functionality inside of it.
from .models import Post
# We Register our models here.

admin.site.register(Post)

