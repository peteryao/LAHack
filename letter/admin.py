from django.contrib import admin
from image_cropping import ImageCroppingMixin

from .models import Letter, CityPhrase

class LetterAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

admin.site.register(Letter, LetterAdmin)
admin.site.register(CityPhrase)