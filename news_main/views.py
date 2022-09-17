from django.shortcuts import render
from .models import News

def index(request):
    
    return render(request, template_name='news_main/index.html', context={
        "News": News.objects.all()
    })


# def get_news(request):
#     data = {
#         "news": News.objects.get(pk=pk)
#     }
