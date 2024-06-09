from django.contrib import admin
from .models import category_model  # Import the model directly


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}  # 'name' should be in a tuple
    list_display = ['name', 'slug']

admin.site.register(category_model, CategoryAdmin)  # Use the actual model class name
