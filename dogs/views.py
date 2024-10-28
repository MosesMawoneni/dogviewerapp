from django.shortcuts import render
from django.views.generic import ListView

from dogs.models import Dog


class ShowAllDogsList(ListView):
    model = Dog
    template_name = "dog_list.html"
    context_object_name = "dogs"
