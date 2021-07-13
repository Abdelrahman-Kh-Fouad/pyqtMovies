from src.Api import *
import requests

if __name__ == '__main__':
    x = API()
    x.TopMovies()
    print(x.urlRequest)
    request = requests.get( x.urlRequest)
    for _ in API.JsonToMovies(request.json()):
        print(_)
