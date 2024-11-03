from django.contrib import admin
from .models import News
# Register your models here.

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'data', )
    list_filter = ('data', )
    search_fields = ('title', 'data', )
    list_per_page = 3


