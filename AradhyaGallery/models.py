from django.db import models
from django import forms

# Create your models here.
class Gallery(models.Model):
    g_name = models.CharField(max_length=30)
    g_image = models.ImageField(upload_to='images',default='/default.png')
    date_created = models.DateField(auto_now_add=True)

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__'