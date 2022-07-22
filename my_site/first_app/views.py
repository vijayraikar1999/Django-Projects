from email.header import Header
from pkgutil import extend_path
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.http.response import HttpResponse
from django.urls import reverse

# Create your views here.

articles = {
    'sports': 'Sports Page',
    'finance': 'Finance Page',
    'politics': 'Politics Page', 
}

def simple_view(request):
    return render(request=request, template_name='first_app/example.html')


def news_view(request, topic):

    try:
        result = articles[topic]
        return HttpResponse(result)
    except:
        result = 'No page for that topic!'
        raise Http404("404 GENERIC ERROR")  # 404.html  

def add_view(request, num1, num2):
    result = num1 + num2
    result = f"{num1} + {num2} = {result}"
    return HttpResponse(str(result))        

def num_page_view(request, num_page):
    
    topic_list = list(articles.keys())
    topic = topic_list[num_page]

    return HttpResponseRedirect(reverse('topic-page', args=[topic]))