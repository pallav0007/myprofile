from django.urls import path, include
from .views import skills

app_name = "myskills"
urlpatterns = [
    path('', skills, name="myskills"),
]