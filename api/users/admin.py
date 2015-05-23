from django.contrib import admin
from .models import Details

class DetailsAdmin(admin.ModelAdmin):

    """
        ModelAdmin for user Details
    """
    list_display = ['user', 'father_name', 'mother_name', 'city']

admin.site.register(Details, DetailsAdmin)
