class Movie :
    def __init__(self , id , name , year , rate , description):
        self.id = id
        self.name = name
        self.year = year
        self.rate = rate
        self.description = description


    def __str__(self):
        return f"{self.name} , {self.year}  , {self.rate} "