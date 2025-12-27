class Library:

    def __init__(self):
        self.books = []
        self.members = []
    
    def add_book(self,book):
        self.books.append(book)
    
    def add_member(self,member):
        self.members.append(member)
    
    def lend_book(self,bn,member_id):
        for book in self.books:
            if book.bn == bn and book.is_available:
                for member in self.members:
                    if member.member_id == member_id:
                        book.is_available = False
                        member.borrowed_books.append(book)
                        print(f"{member.name} has borrowed {book.title}")
                        return True
        print("Book not available or member not found")
        return False

class Book:
    def __init__(self,title,author, bn):
        self.title = title
        self.author = author
        self.bn = bn
        self.is_available = True

class Member:
    def __init__(self,name,member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
    
library = Library()

b1 = Book("Python Basics", "Guido", "101")
m1 = Member("VK", 1)

library.add_book(b1)
library.add_member(m1)

library.lend_book("101", 1)
library.lend_book("101", 1)