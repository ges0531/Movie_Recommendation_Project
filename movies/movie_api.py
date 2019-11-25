import http.client
import json

conn = http.client.HTTPSConnection("api.themoviedb.org")

payload = "{}"
date_api = "/3/discover/movie?primary_release_year=2018&page=1&include_video=false&include_adult=false&sort_by=popularity.desc&language=ko-KR&api_key=c7071549de08bd22fd6ecb4d67cf2099"
genre_api = "/3/genre/movie/list?language=ko-KR&api_key=c7071549de08bd22fd6ecb4d67cf2099"
image_api = "https://image.tmdb.org/t/p/w300_and_h450_bestv2"
conn.request("GET", genre_api, payload)
res = conn.getresponse()
data = res.read()
movie_data = json.loads(data.decode("utf-8"))
print(movie_data)
# for i in range(10):
#     print(movie_data['results'][i]['title'])


