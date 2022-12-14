from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Category, Bookmark


class CategoriesUV(LoginRequiredMixin, UpdateView):
    template_name = 'bookmark/category_creat.html'
    model = Category
    fields = ['title', 'description']

    def get_context_data(self, **kwargs):
        context = super(CategoriesUV, self).get_context_data()
        context['canAdd'] = True
        return context

    def get_success_url(self):
        messages.success(request=self.request, message='updated successfully!', )
        return reverse_lazy('bookmark:categories')


class CategoriesLV(LoginRequiredMixin, ListView):
    template_name = 'bookmark/categories.html'
    model = Category


class CategoriesDV(LoginRequiredMixin, DetailView):
    template_name = 'bookmark/category.html'
    model = Category

    def get_context_data(self, **kwargs):
        context = super(CategoriesDV, self).get_context_data()
        bookmarks = self.get_object().bookmarks.values('id', 'category_id', 'title', 'description', 'url',
                                                       'visit_count')
        for bookmark in bookmarks:
            bookmark['target'] = '_blank'
            if bookmark['url'] is None:
                bookmark['url'] = '#'
                bookmark['target'] = '_self'
            bookmark['edit_url'] = reverse('bookmark:bookmark_edit',
                                           kwargs={'pk': bookmark['id'], 'category_id': bookmark['category_id']})
        context['bookmarks'] = str(list(bookmarks))
        return context


class CategoriesDelete(LoginRequiredMixin, DeleteView):
    template_name = 'bookmark/category_delete.html'
    model = Category

    # success_url = reverse_lazy('bookmark:categories')
    def get_success_url(self):
        messages.error(request=self.request, message='deleted successfully!', )
        return reverse_lazy('bookmark:categories')


class CategoriesCV(LoginRequiredMixin, CreateView):
    template_name = 'bookmark/category_creat.html'
    model = Category
    fields = ['title', 'description']
    success_url = reverse_lazy('bookmark:categories')

    def get_context_data(self, **kwargs):
        context = super(CategoriesCV, self).get_context_data()
        context['canAdd'] = True
        catcount = self.request.user.categories.count()
        if self.request.user.profile.plan == 'basic' and (catcount >= 5):
            context['canAdd'] = False
            context['canAddMessage'] = 'you cant have more than 5 categories when you are in basic plan.'
        elif self.request.user.profile.plan == 'pro' and (catcount >= 50):
            context['canAdd'] = False
            context['canAddMessage'] = 'you cant have more than 50 categories when you are in pro plan.'
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        obj.save()
        messages.success(request=self.request, message='created successfully!', )
        return super(CategoriesCV, self).form_valid(form)


class BookmarksLV(LoginRequiredMixin, ListView):
    template_name = 'bookmark/bookmarks.html'
    model = Bookmark


class BookmarksDV(LoginRequiredMixin, DetailView):
    template_name = 'bookmark/bookmark.html'
    model = Bookmark


class BookmarksUV(LoginRequiredMixin, UpdateView):
    template_name = 'bookmark/bookmark_creat.html'
    model = Bookmark
    # success_url = reverse_lazy('bookmark:bookmarks')
    fields = ['title', 'description', 'url']

    def get_context_data(self, **kwargs):
        context = super(BookmarksUV, self).get_context_data()
        context['canAdd'] = True
        return context

    def get_success_url(self):
        messages.success(request=self.request, message='updated successfully!', )
        return reverse_lazy('bookmark:category_detail', args=[self.kwargs.get('category_id')])


class BookmarksDelete(LoginRequiredMixin, DeleteView):
    template_name = 'bookmark/bookmark_delete.html'
    model = Bookmark

    def get_success_url(self):
        messages.error(request=self.request, message='deleted successfully!', )
        return reverse_lazy('bookmark:category_detail', args=[self.kwargs.get('category_id')])


class BookmarksCV(LoginRequiredMixin, CreateView):
    template_name = 'bookmark/bookmark_creat.html'
    model = Bookmark
    fields = ['title', 'description', 'url']

    def get_context_data(self, **kwargs):
        context = super(BookmarksCV, self).get_context_data()
        context['canAdd'] = True
        book_count = self.request.user.bookmarks.count()
        if self.request.user.profile.plan == 'basic' and (book_count >= 50):
            context['canAdd'] = False
            context['canAddMessage'] = 'you cant have more than 50 bookmarks when you are in basic plan.'
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        obj.category_id = self.kwargs.get('category_id')
        obj.save()
        return super(BookmarksCV, self).form_valid(form)

    def get_success_url(self):
        messages.success(request=self.request, message='created successfully!', )
        return reverse_lazy('bookmark:category_detail', args=[self.kwargs.get('category_id')])

    def form_invalid(self, form):
        messages.success(request=self.request, message=f'try again! {form.errors}', )
        return super(BookmarksCV, self).form_invalid(form)
