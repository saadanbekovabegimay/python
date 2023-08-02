from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .models import ArticleNew

def news_list(request):
    articles = ArticleNew.objects.all()
    return render(request, 'news/news_list.html', {'articles': articles})

# Create your views here.
def news_detail(request, id):
    news_object = ArticleNew.objects.get(id=id)
    return render(
        request,
        'news/detail.html',
        {'news_object': news_object}
    )

class ArticleCreateView(CreateView):
    model = ArticleNew
    fields = ['author', 'title', 'text']

class ArticleUpdateView(UpdateView):
    model = ArticleNew
    fields = ['author', 'title', 'text']
    template_name = 'news/news_form.html'
    success_url = reverse_lazy('news_list')
