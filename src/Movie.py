class Movie :
    def __init__(self , id , name , year , rate):
        self.id = id
        self.name = name
        self.year = year
        self.rate = rate


    def __str__(self):
        return f"{self.name} , {self.year}  , {self.rate} "