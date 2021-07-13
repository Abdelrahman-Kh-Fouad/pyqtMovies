from src.Movie import Movie
from src.Const import *
import requests


class API:
    def __init__(self):
        self.urlRequest = BASIC_URL

    def AddTopRatedMovies(self):
        self.urlRequest += '/' + MOVIE_TOP

    def AddKey(self):
        self.urlRequest += '?api_key=' + API_KEY

    def AddLang(self):
        self.urlRequest += '&' + 'language=en-US'

    def AddPage(self):
        self.urlRequest +='&'+'page=1'


    def TopMovies(self):
        self.AddTopRatedMovies()
        self.AddKey()
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
    def JsonToMovies(cls , jsonFile):
        result =[]
        for movieDic in jsonFile['results']:
            result.append(Movie(int(movieDic['id'])
                                ,movieDic['title']
                                ,movieDic['release_date']
                                ,movieDic['vote_average']))

        return result
