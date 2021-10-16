from abc import ABCMeta, abstractmethod

class MyIterator(metaclass=ABCMeta):
    @abstractmethod
    def hasNext(self) -> bool:
        pass

    @abstractmethod
    def next(self):
        pass

class Aggregate(metaclass=ABCMeta):
    @abstractmethod
    def getIterator(self) -> MyIterator:
        pass

class Book():
    
    def __init__(self,name:str):
        self.name = name
    
    def getName(self):
        return self.name

class BookShelf(Aggregate):

    def __init__(self):
        self.books = []
    
    def getBookAt(self,index:int):
        return self.books[index]
    
    def addBook(self,book:Book):
        self.books.append(book)
    
    def countBooks(self):
        return len(self.books)

    def getIterator(self) -> MyIterator:
        return BookShelfIterator(self)

class BookShelfIterator(MyIterator):

    def __init__(self,bookSelf:BookShelf):
        self.bookShelf = bookSelf
        self.index = 0
    
    def hasNext(self) -> bool:
        return self.index < self.bookShelf.countBooks()

    def next(self):
        BOOK = self.bookShelf.getBookAt(self.index)
        self.index += 1

        return BOOK

BOOK_SHELF = BookShelf()
BOOK_SHELF.addBook(Book('走れメロス'))
BOOK_SHELF.addBook(Book('羅生門'))
BOOK_SHELF.addBook(Book('人間失格'))

BOOK_SHELF_ITERSTOR = BOOK_SHELF.getIterator()

while BOOK_SHELF_ITERSTOR.hasNext():
    book = BOOK_SHELF_ITERSTOR.next()

    print(book.getName())