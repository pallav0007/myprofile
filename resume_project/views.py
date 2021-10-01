from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import myprojects
# Create your views here.
class projectsview(ListView):
    model = myprojects
    template_name = 'myprojects.html'

