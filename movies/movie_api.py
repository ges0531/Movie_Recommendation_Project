import http.client
import json
for date in range(1980, 2020):
    conn = http.client.HTTPSConnection("api.themoviedb.org")
    payload = "{}"
    date_api = "/3/discover/movie?primary_release_year={}&page=1&include_video=false&include_adult=false&sort_by=popularity.desc&language=ko-KR&api_key=c7071549de08bd22fd6ecb4d67cf2099".format(date)
    genre_api = "/3/genre/movie/list?language=ko-KR&api_key=c7071549de08bd22fd6ecb4d67cf2099"
    image_api = "https://image.tmdb.org/t/p/w300_and_h450_bestv2"
    conn.request("GET", genre_api, payload)
    res = conn.getresponse()
    data = res.read()
    movie_data = json.loads(data.decode("utf-8"))
    for genre in movie_data['genres']:
        Genre.objects.create(genre_id=genre['id'], name=genre['name'])
    conn = http.client.HTTPSConnection("api.themoviedb.org") 
    payload = "{}"
    date_api = "/3/discover/movie?primary_release_year={}&page=1&include_video=false&include_adult=false&sort_by=popularity.desc&language=ko-KR&api_key=c7071549de08bd22fd6ecb4d67cf2099".format(date)
    conn.request("GET", date_api, payload)
    res = conn.getresponse()
    data = res.read()
    movie_data = json.loads(data.decode("utf-8"))
    result = movie_data['results']
    for i in range(10):
        Movie.objects.create(title=result[i]['title'], overview=result[i]['overview'], popularity=result[i]['popularity'], poster_url=image_api+result[i]['poster_path'], release_date=result[i]['release_date'])
# print(movie_data)
# for i in range(10):
#     print(movie_data['results'][i]['title'])


