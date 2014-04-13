from django.contrib import admin
from image_cropping import ImageCroppingMixin

from .models import Letter

class LetterAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

admin.site.register(Letter, LetterAdmin)