from django.db import models

class Images(models.Model):

    img_photo = models.ImageField(upload_to='unlocked_buffs/',null=True, blank=True)

    def get_image(self):
        if self.img_photo and hasattr(self.img_photo, 'url'):
            return self.img_photo.url
        else:
            return '/path/to/default/image'

    def __str__(self):
        return str(self.img_photo)
