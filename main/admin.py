from django.contrib import admin
from .models import Image, ImageTwo
from .forms import ShowImageForm, ShowImageFormTwo


#class ShowPhotoInline(admin.TabularInline):
#    model = ShowPhoto


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    form = ShowImageForm

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        form.save_photos(form.instance)

@admin.register(ImageTwo)
class ImageAdmin(admin.ModelAdmin):
    form = ShowImageFormTwo

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        form.save_photos(form.instance)
