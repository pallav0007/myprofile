from django.shortcuts import render
from .models import myskills
# Create your views here.

def skills(request):
    c=myskills.objects.all()
    context={}
    for a in c:
        context[a.name]=a.about.split(",")
    print(context)
    return render(request,"myskills.html",context={"d":context})