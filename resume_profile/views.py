
from django.shortcuts import render,HttpResponse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.models import User
from .models import Information,Bio
from .chatbot import chat
# Create your views here.

class informationview(ListView):
    model = Information
    template_name = 'informationview.html'

    def get_context_data(self, **kwargs):
        context = super(informationview, self).get_context_data(**kwargs)
        context['roles'] = Bio.objects.all()
        return context

def myresume(request):
    return render(request,"myresume.html")
def contactme(request):
    return render(request,"contactme.html")
def myskills(request):
    context={}
    context["w"]=["a","b","c"]
    context["t"]=[1,2,4]
    return render(request,"myskills.html",context)

def get_bot_response(request):
    print("yes hello")
    userText = request.GET.get('msg',"hello")
    print(userText)
    reply=chat(userText)
    return HttpResponse(reply)