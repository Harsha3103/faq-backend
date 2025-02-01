from django.contrib import admin
from .models import FAQ  # Import the FAQ model

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')  # Fields to display in the admin panel
