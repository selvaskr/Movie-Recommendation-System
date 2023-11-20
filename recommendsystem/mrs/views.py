
from django.shortcuts import render
from .helpers import *


def home(request):
    
    #Fetch the details of upcoming and top rated movies list from imdb website using web scrapping.
    upcomingmovie=upcoming_movies()
    topratedmovie=topratedmovies()    

    context = {
        'detail1':upcomingmovie,
        'detail2':topratedmovie
    }

    return render(request, 'index.html', context)


def recommend(request):

    if request.method=='POST':
        moviename = request.POST.get('input_field')
    else:
        moviename=request.GET.get('movie_name')
    
    inputmovie,recommendmovie=recommendation(moviename)
    context={
        'detail1':inputmovie,
        'detail2':recommendmovie
    }
    return render(request,'details.html',context)