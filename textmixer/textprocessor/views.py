from django.shortcuts import render
from .forms import UploadFileForm
import random

def shuffle_word(word):
    if len(word) <= 3:
        return word
    middle = list(word[1:-1])
    random.shuffle(middle)
    return word[0] + ''.join(middle) + word[-1]

def process_text(text):
    words = text.split()
    return ' '.join(shuffle_word(word) for word in words)

def home(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            text = file.read().decode('utf-8')
            result = process_text(text)
            return render(request, 'result.html', {'result': result})
    else:
        form = UploadFileForm()
    return render(request, 'home.html', {'form': form})
