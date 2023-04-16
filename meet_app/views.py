from django.shortcuts import render, redirect
from . models import News
from . form import NewsForm
from django.utils.html import strip_tags
from django.http import HttpResponse


def Home(requset):
    news = News.objects.all()
    return render(requset, "index.html", {"news": news})


def newNews(request):
    if request.method == "GET":
        form = NewsForm()
        return render(request, "newNews.html", {"form": form})
    elif request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

def NewsKAC(request):
    news = News.objects.filter(group="KAC")
    return render(request, "new.html", {"news": news})
    

def NewsMSZK(request):
    news = News.objects.filter(group="MSZK")
    return render(request, "new.html", {"news": news})


def NewsPKSZK(request):
    news = News.objects.filter(group="PKSZK")
    return render(request, "new.html", {"news": news})


def NewsGTSZK(request):
    news = News.objects.filter(group="GTSZK")
    return render(request, "new.html", {"news": news})

def KACnews(request):
    n = News.objects.filter(group="KAC")
    return render(request, "news.html", {"n": n})


def MSZKnews(request):
    n = News.objects.filter(group="MSZK")
    return render(request, "news.html", {"n": n})


def PKSZKnews(request):
    n = News.objects.filter(group="PKSZK")
    return render(request, "news.html", {"n": n})


def GTSZKnews(request):
    n = News.objects.filter(group="GTSZK")
    return render(request, "news.html", {"n": n})
