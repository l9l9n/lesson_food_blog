from django.shortcuts import render
from django.views.generic import FormView, CreateView, TemplateView, ListView, DetailView
from .models import *

class IndexView(TemplateView):
    template_name = 'index.html'


class CategoryListView(ListView):
    template_name = 'category_list.html'
    model = Category
    queryset = Category.objects.all()


# def get_categories(request):
#     categories = Category.objects.all()
#     context = {
#         'categories': categories
#     }
#     return render(request, 'category_list.html', context)

class PostListView(ListView):
    template_name = 'post_list.html'
    model = Post
    queryset = Post.objects.filter(is_draft=False)


class PostDetailView(DetailView):
    template_name = 'post_detail.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_post = Post.objects.filter(is_draft=False)
        if len(latest_post) < 5:
            context['latest_post'] = latest_post
        else:
            context['latest_post'] = latest_post[:5]

        context['categories'] = Category.objects.all()

        return context
