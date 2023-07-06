import requests
from django.shortcuts import render
from .forms import ImageForm
from .models import Image
from django.core.files.base import ContentFile


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST)
        if form.is_valid():
            image_url = form.cleaned_data['image_url']
            response = requests.get(image_url)

            image = Image(title='Uploaded Image', image_url=image_url)
            image.uploaded_image.save('image.jpg', ContentFile(response.content), save=True)

            # Optionally, you can save the image URL to the database as well
            # image.save()

            return render(request, 'app/success.html')
    else:
        form = ImageForm()

    return render(request, 'app/index.html', {'form': form})
