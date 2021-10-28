from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from apirest.models import Cliente


class ClienteListView(ListView):
    model = Cliente
    #template_name = ".html"
