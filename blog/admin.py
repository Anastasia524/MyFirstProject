from django.contrib import admin

# Register your models here.
from blog.models import Article, BuyTyr, Comments

admin.site.register([Article, BuyTyr, Comments])