# Class Book
class Book:
    def __init__(self, name, type):
        self.name = name
        self.type = type
 
    def __str__(self):
        return f"Book Name: {self.name}, Book Type: {self.type}"

# Class Member
class Member:
   def __init__(self, name, memberId, borrowedBooks):
        self.name = name
        self.memberId = memberId
        self.borrowedbooks = borrowedBooks
 
   def __str__(self):
        return f"Member Name: {self.name}, Member Type: {self.memberId}, Member Borrowed Books: {self.borrowedBooks}"
 
class Library:
   def __init__(self, collectionOfBooks, member):
        self.collectionOfBooks = collectionOfBooks
        self.member = member
 
   def __str__(self):
        return f"Book Name: {self.name}, Book Type: {self.type}"
 
   def addBook(self, book):
        self.collectionOfBooks.append(book)
 
  # Remove book
   def removeBook(self, book):
        self.collectionOfBooks.remove(book)
 
   # Borrow book means lending
   def borrowBook(self, member, book):
        if book in self.collectionOfBooks:
            self.collectionOfBooks.remove(book)
            member.borrowedbooks.append(book)
            print("Book borrowed successfully")
        else:
            print("Book not available")
 
   def registerMember(self, member):
        self.member = member
        print("Member registered successfully")
 
book1 = Book("Slash", "Horror")
book2 = Book("Fairy", "Fantasy")
 
collectionOfBooks = [book1, book2]
member1 = Member("John", 1, [])
 
library1 = Library(collectionOfBooks, member1)
 
library1.addBook(book1)
library1.addBook(book2)
library1.removeBook(book1)
 
library1.borrowBook(member1, book2)
library1.registerMember(member1)
