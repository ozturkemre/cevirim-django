from django.shortcuts import render
from django.http import JsonResponse


def main_page(request):
    return render(request, 'blog/main_page.html', {})


def translate(request):
    from googletrans import Translator
    text = request.GET.get('text', None)
    source = request.GET.get('src', None)
    destination = request.GET.get('dest', None)
    if (source is None or destination is None):
        data = {
            'translated': 'Please choose Source and Destination Language to Translate'
        }
        return JsonResponse(data)
    else:
        translator = Translator()
        data = {
            'translated': translator.translate(text, src=source, dest=destination).text
        }
        return JsonResponse(data)