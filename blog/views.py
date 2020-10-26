from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    return render(request, 'blog/index.html')


class IndexPage(TemplateView):
    template_name = 'blog/index.html'
