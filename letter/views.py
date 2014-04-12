import datetime

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

from .models import Letter

def letter_index(request):
    context = {}
    return render(request, 'letter/index.html', context)

def letter_list_view(request):
    context = {}
    return render(request, 'letter/list_view.html', context)

def letter_query_view(request, filter_choice, order_choice):
    context = {}
    return render(request, 'letter/query_view.html', context)

def letter_single_view(request, letter_pk):
    context = {}
    return render(request, 'letter/index.html', context)