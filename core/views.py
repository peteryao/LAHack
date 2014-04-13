from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, Permission

def index(request):
    context = {}
    context['index_page'] = True
    return render(request, 'core/index.html', context)
