from django.http import JsonResponse
import pandas as pd


def autocompletelist(request):
    movie = pd.read_csv("D:/MoviesRecommendationSystem/recommendsystem/data/movies_1816to2022.csv")
    term = request.GET.get('term', '')
    filtered_names = movie['movie_title'][movie['movie_title'].str.contains(term, case=False)][:10].tolist()
    
    if not filtered_names:
        return JsonResponse(['No matches found'], safe=False)
    
    return JsonResponse(filtered_names, safe=False)