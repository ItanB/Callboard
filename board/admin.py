from django.contrib import admin
from .models import BoardUser, Ad, Category, AdCategory

admin.site.register(BoardUser)
admin.site.register(Ad)
admin.site.register(Category)
admin.site.register(AdCategory)
