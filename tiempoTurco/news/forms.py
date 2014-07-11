from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from images.models import Image
from gallery.models import Gallery
from .models import New

#class NewsInlineForm(ModelForm):
#    class Meta:
#        model = New

#ImageFormSet = inlineformset_factory(New,Image)
#GalleryFormSet = inlineformset_factory(New,Gallery)