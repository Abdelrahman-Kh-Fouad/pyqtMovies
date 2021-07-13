from src.Api import *

if __name__ == '__main__':
    x = API()
    x.TopMovies()
    print(x.urlRequest)
    request = requests.get( x.urlRequest)
    for _ in Request.GetSearchMovie("spiderman"):
        print(_)
