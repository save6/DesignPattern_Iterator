class Book():
    
    def __init__(self,name:str):
        self.name = name
    
    def getName(self):
        return self.name

class BookShelf():

    def __init__(self):
        self.books = []
    
    def addBook(self,book:Book):
        self.books.append(book)

BOOK_SHELF = BookShelf()
BOOK_SHELF.addBook(Book('走れメロス'))
BOOK_SHELF.addBook(Book('羅生門'))
BOOK_SHELF.addBook(Book('人間失格'))

for book in BOOK_SHELF.books:
    print(book.getName())