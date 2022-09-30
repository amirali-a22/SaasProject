from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from bookmark.models import Bookmark


class DashboardV(LoginRequiredMixin, View):
    template_name = 'dashboard/dashboard.html'

    def get(self, request, *args, **kwargs):
        bookmarks = request.user.bookmarks.all()[:5]

        context = {
            'bookmarks': bookmarks
        }
        return render(request, self.template_name, context)
