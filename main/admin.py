from django.contrib import admin
from .models import Image
from .forms import ShowImageForm


#class ShowPhotoInline(admin.TabularInline):
#    model = ShowPhoto


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    form = ShowImageForm
    #inlines = [ShowPhotoInline]

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        form.save_photos(form.instance)
