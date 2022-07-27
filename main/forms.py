from django import forms
from django.core.validators import validate_image_file_extension
from django.utils.translation import gettext as _


from .models import Image, ImageTwo, Trait


class ShowImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = (
            "title",
        )

    images = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
        label=_("Add photos"),
        required=False,
    )

    def clean_photos(self):
        """Make sure only images can be uploaded."""
        for upload in self.files.getlist("images"):
            validate_image_file_extension(upload)

    def save_photos(self, show):
        """Process each uploaded image."""
        for upload in self.files.getlist("images"):
            image = Image(img_photo=upload)
            image.save()

class ShowImageFormTwo(forms.ModelForm):
    class Meta:
        model = Image
        fields = (
            "title",
        )

    images = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
        label=_("Add photos"),
        required=False,
    )

    def clean_photos(self):
        """Make sure only images can be uploaded."""
        for upload in self.files.getlist("images"):
            validate_image_file_extension(upload)

    def save_photos(self, show):
        """Process each uploaded image."""
        for upload in self.files.getlist("images"):
            image = ImageTwo(img_photo=upload)
            image.save()

class ShowTraitForm(forms.ModelForm):
    class Meta:
        model = Trait
        fields = (
            "uniqueId",
        )
