import requests
import json

TMDB_API_KEY = '95b860a11ebc499441e83162dd92d89f'

def get_movie_data():
    total_data = []
    request_url_genre = f'https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}&language=ko-KR'
    genres = requests.get(request_url_genre).json()
    
    for genre in genres['genres']:
        fields = {
            'name': genre['name'],
        }
        data_g = {
            'model':'movies.genre',
            'pk': genre['id'],
            'fields': fields,
        }
        total_data.append(data_g)

    page = 101
    idx = 0
    for i in range(1, page):
        request_url_movie = f'https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}'

        movies = requests.get(request_url_movie).json()

        for j in range(len(movies['results'])):
            movie = movies['results'][j]
            if movie.get('overview') != '' and movie.get('poster_path') != None and movie.get('release_date') != None:
                idx += 1
                fields = {
                    'title': movie['title'],
                    'movie_id': movie['id'],
                    'title': movie['title'],
                    'release_date': movie['release_date'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path'],
                    'vote_count': movie['vote_count'],
                    'vote_average': movie['vote_average'],
                    'genres': movie['genre_ids'],
                }


                data = {
                    "model": "movies.movie",
                    "pk": idx,
                    "fields": fields
                }

                total_data.append(data)

    for i in range(1, page):
        request_url_movie_en = f'https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=en-US&page={i}'

        movies_en = requests.get(request_url_movie_en).json()

        for movie_en in movies_en['results']:
            for movie in total_data:
                if movie["model"] == "movies.movie":
                    if movie_en["id"] == movie["fields"]["movie_id"]:
                        movie["fields"]["overview_en"] = movie_en["overview"]

    with open("./movie_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=2, ensure_ascii=False)

get_movie_data()