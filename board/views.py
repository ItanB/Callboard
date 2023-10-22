from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404, render
from .models import BoardUser, Ad
from .forms import AdForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class AdList(ListView):
    model = Ad
    ordering = '-id'
    template_name = 'list.html'
    context_object_name = 'ads'


class AdDetail(DetailView):
    model = Ad
    template_name = 'addetails.html'
    context_object_name = 'fullad'


class CreateAd(CreateView):
    form_class = AdForm
    model = Ad
    template_name = 'create.html'
    context_object_name = 'create'
    success_url = reverse_lazy("list")


class AdUpdate(UpdateView):
    form_class = AdForm
    model = Ad
    template_name = 'adupdate.html'
    context_object_name = 'update'
    success_url = reverse_lazy("list")


class AdDelete(DeleteView):
    model = Ad
    template_name = 'addelete.html'
    success_url = reverse_lazy("list")
