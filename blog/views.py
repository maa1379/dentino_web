from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.edit import FormMixin

from .forms import BlogForm
from .models import Blog, BlogTag


# Create your views here.
class BlogList(ListView):
    model = Blog
    template_name = "blog/list.html"
    paginate_by = 8


class BlogDetail(FormMixin, DetailView):
    def get_object(self, **kwargs):
        blog = get_object_or_404(Blog.objects.all(), slug=self.kwargs.get("slug"))
        ip_address = self.request.user.ip_address
        if ip_address not in blog.hits.all():
            blog.hits.add(ip_address)
        return blog

    template_name = "blog/detail.html"


class BlogCreate(CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy("blog:list")
    template_name = "blog/create.html"
