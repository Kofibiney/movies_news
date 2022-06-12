from django.shortcuts import render, redirect
from django.contrib import messages
from .models import News, Category, Comment, Upcoming


def home(request):
    # New changes
    movies = News.objects.all()
    print('Hello')
    first_news = News.objects.first()
    three_news = News.objects.all()[1:5]
    three_categories = Category.objects.all()[0:3]
    print("************", movies)
    return render(
        request,
        "home.html",
        {
            "first_news": first_news,
            "three_news": three_news,
            "three_categories": three_categories,
            "movies": movies,
        },
    )


# All News
def all_news(request):
    all_news = News.objects.all()
    three_news = News.objects.all()[1:5]
    upcoming_movies = Upcoming.objects.all()

    return render(
        request,
        "all-news.html",
        {
            "all_news": all_news,
            "three_news": three_news,
            "upcoming_movies": upcoming_movies
        },
    )


def upcoming_movies(request):
    upcoming_movies = Upcoming.objects.all()
    print("************", upcoming_movies)
    return render(
        request,
        "all-news.html",
        {
            "upcoming_movies": upcoming_movies,
        },
    )


# Detail Page
def detail(request, id):
    # print('upcoming')
    news = News.objects.get(pk=id)
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        comment = request.POST["message"]
        Comment.objects.create(news=news, name=name, email=email, comment=comment)
        messages.success(request, "Comment submitted.")
    category = Category.objects.get(id=news.category.id)
    rel_news = News.objects.filter(category=category).exclude(id=id)
    comments = Comment.objects.filter(news=news, status=True).order_by("-id")
    return render(
        request,
        "detail.html",
        {"news": news, "related_news": rel_news, "comments": comments},
    )


# Fetch all category
def all_category(request):
    cats = Category.objects.all()
    return render(request, "category.html", {"cats": cats})


# return all movies by year
# def all_news(request):
#     print('all news')
#     all_news = News.objects.all()
#     context = {
#         "all_news": all_news,
#     }
#     return render(request, "all-news.html", context)


def show_movie_by_year(request, year):
    movies = News.objects.all()
    retrieved_year = year
    context = {
        "movies": movies,
        "retrieved_year": retrieved_year,
    }
    return render(request, "show_movie_by_year.html", context)


# Fetch all category
def category(request, id):
    category = Category.objects.get(id=id)
    news = News.objects.filter(category=category)
    return render(
        request, "category-news.html", {"all_news": news, "category": category}
    )
