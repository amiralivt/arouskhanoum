from django.shortcuts import render
from django.views.generic import ListView
from .models import Article


def index(request):
    return render(request, 'blog/index.html')


class IndexPage(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        return Article.objects.all()
