from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.main_page, name='main_page'),
    url(r'^ajax/translate_text/$', views.translate, name="translate"),
]