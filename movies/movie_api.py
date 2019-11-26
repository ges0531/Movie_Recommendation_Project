import http.client
import json
conn = http.client.HTTPSConnection("api.themoviedb.org")
payload = "{}"
genre_api = "/3/genre/movie/list?language=ko-KR&api_key=c7071549de08bd22fd6ecb4d67cf2099"
image_api = "https://image.tmdb.org/t/p/w300_and_h450_bestv2"
conn.request("GET", genre_api, payload)
res = conn.getresponse()
data = res.read()
movie_data = json.loads(data.decode("utf-8"))
for genre in movie_data['genres']:
    Genre.objects.create(id=genre['id'], name=genre['name'])
# conn = http.client.HTTPSConnection("api.themoviedb.org") 
# payload = "{}"
# image_api = "https://image.tmdb.org/t/p/w300_and_h450_bestv2"
# date_api = "/3/discover/movie?primary_release_year=2018&page=1&include_video=false&include_adult=false&sort_by=popularity.desc&language=ko-KR&api_key=c7071549de08bd22fd6ecb4d67cf2099"
# conn.request("GET", date_api, payload)
# res = conn.getresponse()
# data = res.read()
# movie_data = json.loads(data.decode("utf-8"))
# result = movie_data['results']
# for i in range(5):
#     Movie.objects.create(title=result[i]['title'], overview=result[i]['overview'], popularity=result[i]['popularity'], poster_url=image_api+result[i]['poster_path'], release_date=result[i]['release_date'])
for date in range(1980, 2020):
    conn = http.client.HTTPSConnection("api.themoviedb.org") 
    payload = "{}"
    date_api = "/3/discover/movie?primary_release_year={}&page=1&include_video=false&include_adult=false&sort_by=popularity.desc&language=ko-KR&api_key=c7071549de08bd22fd6ecb4d67cf2099".format(date)
    image_api = "https://image.tmdb.org/t/p/w300_and_h450_bestv2"
    conn.request("GET", date_api, payload)
    res = conn.getresponse()
    data = res.read()
    movie_data = json.loads(data.decode("utf-8"))
    result = movie_data['results']
    for i in range(10):
        Movie.objects.create(title=result[i]['title'], overview=result[i]['overview'], popularity=result[i]['popularity'], poster_url=image_api+result[i]['poster_path'], release_date=result[i]['release_date'])
        my_result = result[i]['genre_ids']
        for j in my_result:
for i in range(5):
    movies[i]['fields']['genre']=result[i]['genre_ids']


# print(movie_data)
# for i in range(10):
#     print(movie_data['results'][i]['title'])

