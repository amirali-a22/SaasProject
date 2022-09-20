from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Category
from .forms import CategoryForm


class CategoriesLV(LoginRequiredMixin, ListView):
    template_name = 'bookmark/categories.html'
    model = Category


class CategoriesDV(LoginRequiredMixin, DetailView):
    template_name = 'bookmark/category.html'
    model = Category


class CategoriesCV(LoginRequiredMixin, CreateView):
    template_name = 'bookmark/category_creat.html'
    model = Category
    fields = ['title', 'description']
    success_url = reverse_lazy('bookmark:categories')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        obj.save()
        return super(CategoriesCV, self).form_valid(form)
