from django import forms

class ImageForm(forms.Form):
    image_url = forms.URLField(label='Image URL')
