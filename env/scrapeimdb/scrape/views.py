import csv

from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import viewsets, permissions, generics

from .forms import UrlForm
from .models import Movie, Role
from .scrape import Scrapster
from .serializers import MovieSerializer, RoleSerializer


def home_view(request):
    form = UrlForm(request.POST or None)
    if form.is_valid():
        url = form.cleaned_data.get('url_link')
        scrape = Scrapster()
        name, star, description, img, content = scrape.scrappy(url)
        valid = Movie.objects.filter(movie_name=name).count()
        if not valid:
            db = Movie(movie_name=name, movie_star=star,
                       movie_description=description, movie_pic=img)
            db.save()
            for cast, character in content.items():
                db1 = Role(cast=db, name=cast, character=character)
                db1.save()
        else:
            messages.success(request, f'Details of {name} already exits ! Please fetch it from the list')
        return redirect('product')
    else:
        form = UrlForm()
    return render(request, "home.html", {'form': form})


def product_view(request):
    movie = Movie.objects.all()
    if request.method == "POST":
        movies = Movie.objects.filter(id=id)
        movies.delete()
        return redirect('')
    return render(request, "product.html", {'movie': movie})


def product_delete(request, id):
    if request.method == "POST":
        movie_column = Movie.objects.get(id=id)
        movie_column.delete()
        messages.success(request, f'"{ movie_name}" was deleted succesfully')
        return redirect('product')
    return render(request, 'delete.html', {})


def product_details(request, id):
    movie = Role.objects.filter(cast__id=id)
    movie_column = Movie.objects.get(id=id)
    return render(request, 'details.html',
                  {'movie': movie, 'movie_column': movie_column})


def export_file(request, id):
    movie_data = Movie.objects.get(id=id)
    c_movie = Role.objects.filter(cast__id=id)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename= "scrap.csv"'
    writer = csv.writer(response)
    writer.writerow(['Movie Name', 'Rating', 'Description'])
    f = movie_data.movie_star
    s = movie_data.movie_name
    d = movie_data.movie_description
    writer.writerow([s, f, d])
    writer.writerow(['Name', 'Character'])
    for cast in c_movie:
        writer.writerow([cast.name, cast.character, '\n'])
    return response


class MovieView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class RoleView(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
