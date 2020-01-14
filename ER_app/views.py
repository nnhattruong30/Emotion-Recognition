from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageForm
from django.conf import settings
from .emotion_recog import emotion_classify

def homepage(request):
    form = ImageForm()
    if request.method =='POST' and request.FILES:
        form = ImageForm(request.POST, files= request.FILES)
        if form.is_valid():
            form.save()

            max_id = Image.objects.latest('id').id
            obj = Image.objects.get(id=max_id)
            input_path = settings.BASE_DIR + obj.image.url
            output_path = settings.BASE_DIR + "/media/out/output.jpg"
            num_face = emotion_classify.recognition(input_path, output_path)
            return render(request, 'ER/result.html', {'obj': obj, 'face': num_face})

    return render(request, 'ER/upload.html', {'form': form})