class Video:
    
    def __init__(self, name, year, director, rating, genre, rentalStatus="Available"):
        self.name = name
        self.year = year
        self.director = director
        self.rating = rating
        self.genre = genre
        self.rentalStatus = rentalStatus
        
    def getName(self):
        return self.name
    
    def getYear(self):
        return self.year
        
    def getDirector(self):
        return self.director
        
    def getRating(self):
        return self.rating
        
    def getGenre(self):
        return self.genre
        
    def getRentalStatus(self):
        return self.rentalStatus


    def editName(self, name):
        self.name = name

    def editYear(self, year):
        self.year = year

    def editDirector(self, director):
        self.director = director

    def editRating(self, rating):
        self.rating = rating

    def editGenre(self, genre):
        self.genre = genre

    def editRentalStatus(self, rentalStatus):
        self.rentalStatus = rentalStatus
