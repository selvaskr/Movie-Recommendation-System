from tmdbv3api import Movie
from tmdbv3api import TMDb
import requests
from bs4 import BeautifulSoup
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

with open('similarity_object.pkl', 'rb') as file:
    similarity_matrix = pickle.load(file)

# HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.99 Safari/537.36'}

def upcoming_movies():

    url = "https://www.imdb.com/calendar/?region=us"
    response = requests.get(url ,headers=HEADERS)

    # Parse the HTML using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Initialize lists to store extracted data
    titles = []

    # Find all the list items containing the entries
    entries = soup.find_all('li', class_='ipc-metadata-list-summary-item')

    # Iterate through the entries and extract data
    for entry in entries[:10]:
        # Extract the title
        title_element = entry.find('a', class_='ipc-metadata-list-summary-item__t')
        title = title_element.text.strip() if title_element else None
        parts = title.split(" (", 1)
        movie_title = parts[0]
        titles.append(movie_title)

    movieposters=fetchposter(titles,6)

    return movieposters


def topratedmovies():

    url = "https://www.imdb.com/chart/top/"
    response = requests.get(url ,headers=HEADERS)
    
    soup = BeautifulSoup(response.content, 'html.parser')

    movies=soup.find('ul',class_='ipc-metadata-list')
    s=movies.find_all('li',class_='ipc-metadata-list-summary-item')
    
    titles=[]

    for i in movies:
        title_element=i.find('h3',class_="ipc-title__text")
        title = title_element.text.strip() if title_element else None
        parts = title.split(" (", 1)
        movie_title = parts[0]
        titles.append(movie_title[3:])

    movieposters=fetchposter(titles[:6],6)

    return movieposters



tmdb = TMDb()
tmdb_movie=Movie()
tmdb.api_key = '415fc8ed6895e8c714ed4862143e8882'

def extract_moviedetails(x):     
    
    params = {
        'api_key': tmdb.api_key,
        'append_to_response': 'credits,videos'
    }

    result=tmdb_movie.search(x)
    
    if result['results']:
        
        movie_id=result['results'][0]['id']
        movie_url = f'https://api.themoviedb.org/3/movie/{movie_id}'
        
        # Make a GET request with the specified query parameters
        response = requests.get(movie_url, params=params)
        # The final URL will be constructed as: https://example.com/api/resource?param1=value1&param2=value2
        
        movie_details = response.json()
        genres   =    [genre['name'] for genre in movie_details['genres']]
        casts    =    [cast['name'] for cast in movie_details['credits']['cast'][:3]]
        overview =    movie_details['overview']
        dur      =    movie_details['runtime']
        ratings  =    movie_details['vote_average']
        status   =    movie_details['status']
        poster   =   'https://image.tmdb.org/t/p/original/'+movie_details['poster_path']

        movie_detail=[x,genres,casts,overview,dur,ratings,status,poster]
        
        return movie_detail


def fetchposter(names,number):

    posters=[]
    moviename=[]
    movieposter = {}
    params = {
        'api_key': tmdb.api_key,
        'append_to_response': 'credits,videos'
    }

    for name in names:
        result=tmdb_movie.search(name)
        if result['results']:
            
            movie_id=result['results'][0]['id']
            movie_url = f'https://api.themoviedb.org/3/movie/{movie_id}'
            
            # Make a GET request with the specified query parameters
            response = requests.get(movie_url, params=params)
            # The final URL will be constructed as: https://example.com/api/resource?param1=value1&param2=value2
            
            movie_details = response.json()
            #Extract the poster for the movie name.
            if movie_details['poster_path']:

                poster   =   'https://image.tmdb.org/t/p/original/'+movie_details['poster_path']
                moviename.append(name)
                posters.append(poster)
    
    for i in range(0,number):
        key=f'key{i+1}'
        movieposter[key]=[moviename[i],posters[i]]
    return  movieposter


def recommendation(movie):
    global similarity_matrix
    movies=[]
    #Read the dataset 
    data=pd.read_csv("D:/MoviesRecommendationSystem/recommendsystem/data/movies_1816to2022.csv")
    
    #Find the index of the movie which we want to find the recommended list of movies.
    index = data[data['movie_title'] == movie].index[0]
    #With the help of index find the similarity movies from the similarity matrix.
    distances = sorted(list(enumerate(similarity_matrix[index])),reverse=True,key = lambda x: x[1])
    #Append the 1st 10 movies having the highest similarity score in the movies list.
    for i in distances[0:11]: 
        movies.append(data.iloc[i[0]].movie_title)

    inputmovie=extract_moviedetails(movies[0])
    recommended=fetchposter(movies[1:],10)

    print("Recommended Movies: ",len(recommended))

    return inputmovie,recommended
