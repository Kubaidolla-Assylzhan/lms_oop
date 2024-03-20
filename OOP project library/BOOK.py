class Book:
    def __init__(self, author, title, genre):
        self.author = author
        self.title = title
        self.genre = genre
        self.available = False

    def get_available(self):
        return self.available

    def set_available(self, new_available):
        self.available = new_available

    def __repr__(self):
        return "{} - {} - genre of {}".format(self.author,self.title,self.genre)

