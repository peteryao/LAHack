import datetime

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

from django.core.context_processors import csrf
from django.shortcuts import render_to_response

from .models import Letter
from core.views import index

def letter_index(request):
    context = {}
    return render(request, 'letter/index.html', context)

def letter_list_view(request):
    context = {}
    return render(request, 'letter/list_view.html', context)

def letter_query_view(request, filter_choice):
    context = {}
    context['recent_letters'] = Letter.objects.all()[:9]
    if(int(filter_choice) == 1):
        no_texts = []
        for letter in Letter.objects.all():
            if not letter.photo:
                no_texts.append(letter)
        context['recent_letters'] = no_texts
    if(int(filter_choice) == 2):
        no_photo = []
        for letter in Letter.objects.all():
            if letter.photo:
                no_photo.append(letter)
        context['recent_letters'] = no_photo
    context['filter'] = int(filter_choice)

    return render(request, 'letter/query_view.html', context)

def letter_single_view(request, letter_pk):
    context = {}
    context['letter'] = Letter.objects.get(pk=letter_pk)
    return render(request, 'letter/half_and_half.html', context)

def letter_city_view(request, city_info):
    context = {}
    return render(request, 'letter/city_view.html', context)

def letter_submit(request):
    context = {}

    text_input = request.POST['textarea']

    letter = Letter(text=text_input, name="Los Angeles, California")
    # path = letter.photo_upload_to(request.FILES['image_upload'])
    if('image_upload' in request.FILES):
        letter.photo = request.FILES['image_upload']

    letter.save()

    return redirect('index')