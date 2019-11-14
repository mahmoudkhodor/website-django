from django.contrib import admin
from .models import Tutorial
# Register your models here.


class TutorialAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/date", {"fields": ["tutorial_title", "tutorial_published"]}),
        ("content", {"fields": ["tutorial_content"]})
    ]


admin.site.register(Tutorial)
