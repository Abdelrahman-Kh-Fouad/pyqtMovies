from src.Movie import Movie
from src.Const import *
import requests

# https://api.themoviedb.org/3/search/movie?api_key=<<api_key>>&language=en-US&page=1&include_adult=false
class API:
    def __init__(self):
        self.urlRequest = BASIC_URL

    def clear(self):
        self.urlRequest = BASIC_URL

    def AddTopRatedMovies(self):
        self.urlRequest += '/' + MOVIE_TOP

    def AddSearchMovies(self):
        self.urlRequest += '/' + MOVIE_SEARCH

    def AddKey(self):
        self.urlRequest += '?api_key=' + API_KEY

    def AddLang(self):
        self.urlRequest += '&' + 'language=en-US'

    def AddPage(self):
        self.urlRequest +='&'+'page=1'

    def AddQuery(self , movieName):
        self.urlRequest += '&'+'query='+movieName

    def TopMovies(self):
        self.AddTopRatedMovies()
        self.AddKey()
        self.AddLang()
        self.AddPage()


    def SearchMovies(self , movieName):
        self.AddSearchMovies()
        self.AddKey()
        self.AddQuery(movieName)
        self.AddLang()
        self.AddPage()




class Request :
    @classmethod
    def GetTopMovies(cls)->list:
        apiProcess = API()
        apiProcess.TopMovies()

        movieRequest = requests.get(apiProcess.urlRequest)
        return cls.JsonToMovies(movieRequest.json())


    @classmethod
    def GetSearchMovie(cls , movieName):
        apiProcess = API()
        apiProcess.SearchMovies(movieName)

        movieRequest = requests.get(apiProcess.urlRequest)
        return cls.JsonToMovies(movieRequest.json())


    @classmethod
    def JsonToMovies(cls , jsonFile):
        result =[]
        for movieDic in jsonFile['results']:

            result.append(Movie(int(movieDic['id'])
                                ,movieDic['title']
                                ,movieDic['release_date']
                                ,movieDic['vote_average']
                                ,movieDic['overview']))

        return result
