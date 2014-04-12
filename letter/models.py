from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

import image_cropping

from core.models import TimeStampedModel
from core import utils

class Letter(TimeStampedModel):
    name = models.CharField(max_length=2000)
    text = models.URLField(max_length=500)

    def photo_upload_to(self, filename):
        return 'Letter/{}/photo{}'.format(self.name, utils.extension(filename))
    photo = image_cropping.ImageCropField('Photo', upload_to=photo_upload_to, blank=True)
    photo_thumb = image_cropping.ImageRatioField('photo', '160x160')

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.name