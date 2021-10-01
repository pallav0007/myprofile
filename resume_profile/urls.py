from django.urls import path,include
from .views import informationview,myresume,contactme,myskills,get_bot_response
from django.views.generic import TemplateView
app_name="information"
urlpatterns = [
    path('', informationview.as_view(),name="informationview"),
    path('myresume/',myresume,name="myresume"),
    path('contactme/', contactme, name="contactme"),
    path("index/",TemplateView.as_view(template_name="index.html")),
    path("chat/",get_bot_response),
    path("assistant/",TemplateView.as_view(template_name="my_assisant.html"),name="assistant")


]