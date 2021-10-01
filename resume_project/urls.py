from django.urls import path, include
from .views import projectsview

app_name = "projects"
urlpatterns = [
    path('', projectsview.as_view(), name="myprojects"),
]