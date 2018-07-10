import operator
import numpy as np



class User(object):
    def __init__(self, name, email,):
        self.name = name
        self.email = email
        self.books = {}
        self.user_email = {}
#        self.user_email[self.name] = self.email, [self.book]
        self.user_email = {name:email for [name, email] in zip(self.name, self.email)}
    
    def read_book(self, title, rating=None):
        self.books = {books:rating for [books, rating] in zip(self.title, self.rating)}
    
    def get_average_rating(self):
        for books, rating in self.books.values():
            return np.mean(rating)
    
    def get_email(self):
        return "User: {name} ; Email: {email}".format(name=self.user_email.keys(), email=self.user_email.values())

    def change_email(self, name, address):
        self.address = address
        for key in self.user_email.keys():
            if key == self.name:
                self.user_email[key] = self.address
                yield True
        return "The user email, \"{email}\" has been updated to \"{address}\"".format(email=self.email, address=self.address)

    def __repr__(self):
        return "User {name}, email: {email}, books read: {books}".format(name=self.name, email=self.email, books=len(dict(self.book)))

    def __eq__(self, other_user):
        self.other_user = other_user
        return "User __eq__ called: {} == {} ?".format(self, self.other_user)
        return self.value == other_user
    
    
    
class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []
        self.title_isbn = {}
        self.title_isbn = {title:isbn for [title, isbn] in zip(self.title, self.isbn)}
        
    def get_title(self):
        return self.title
    
    def get_isbn(self):
        return self.isbn
    
    def set_isbn(self, isbn, new_isbn):
        self.new_isbn = new_isbn
        for key in self.title_isbn.keys():
            if key == self.title:
                self.title_isbn[key] = self.new_isbn
                yield True
        return "The book's ISBN , \"{isbn}\", has been updated to \"{new_isbn}\"".format(isbn=self.isbn, new_isbn=self.new_isbn)

    def add_rating(self, rating):
        rating = 0
        if rating is range(0,5):
            self.ratings.append(rating)
        else:
            return "\"Invalid Rating\""
        
    def __eq__(self, other_book):
        self.other_book = other_book
        return "Book __eq__ called: {} == {} ?".format(self, self.other_book)
        return self.value == other_book   
        
    def get_average_rating(self):
        for books, rating in self.books.items():
            return np.mean(rating)
            
    def __hash__(self):
        return hash((self.title, self.isbn))



class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author
    
    def get_author(self):
        return self.author
    
    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)



class Non_Fiction(Book):
    def __init__(self, title, subject="", level="", isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.leve = level
        
    def get_subject(self):
        return self.subject
    
    def get_level(self):
        return self.evel
    
    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)



class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}
        
    def create_book(self, title, isbn):
        new_book = Book(title, isbn)
        self.books[title] = new_book
        return new_book
#        self.books = {title:isbn for [title, isbn] in zip(self.title, self.isbn)}
#        return "The book, \"{title}\", has ISBN of \"{isbn}\"".formant(title=self.title, isbn=self.isbn)
        
    def create_novel(self, title, author, isbn):
        new_novel = Fiction(title, author, isbn)
        self.books[title] = new_novel
        return new_novel
        
    def create_non_fiction(self, title, subject, level, isbn):
        new_non_fiction = Non_Fiction(title, subject, level, isbn)
        self.books[title] = new_non_fiction
        return new_non_fiction
        
    def add_book_to_user(self, books, email, rating=None):
        if email not in self.users.keys():
            return "No user with email {email}!".format(email=self.email)
        else:
            self.users[user].read_book(book, rating)
            self.books[book].add_rating(rating)
            for book in self.books.keys():
                if book_read not in book:
                    self.books[book_read] = 1
                else:
                    self.books[book_read] += 1
    
    def add_user(self, name, email, books=None):
        new_user = User(name, email)
        self.users[email] = new_user
        if user_book is not None:
            for book in user_books:
                self.add_book_to_user(book, new_user)
        
    def print_catalog(self):
        for b in self.books:
            print(b)
            
    def print_users(self):
        for u in self.users:
            print(u)
    
    def most_read_book(self):
        most_read_title = max(self.books.items(), value=operator.itemgetter(1))[0]
        times_read = max(self.books.items(), key=operator.itemgetter(1))[0]
        return times_read
        return "The most read book, \"{book}\", has been read {num} times.".format(book=most_read_title, num=times_read)
    
    def highest_rating_book(self):
        for book in self.books:
            b_gar = book.get_average_rating()
            for r in b_gar:
                return max(r)
            return "The most read book, \"{book}\", has the highest rating of {r}.".format(book=book, r=r)
        
    def most_positive_user(self, users):
        for user in self.users: 
            mpu = user.get_average_rating()
            for r_u in mpu:
                return max(r_u)
            return "The most positive user, \"{user}\", has the rating of {r}.".format(user=user, r_u=r_u)
            
    def error_testing(self, user, email, isbn):
        if email in self.users.keys():
            return "This email already exists."
        
        for book_isbn in self.books.values():
            for isbn_char in book_isbn:
                return "Every book has their own unique ISBN."
            
        special_char = ["@", ".com", ".edu", ".org"]
        for email in self.email():
            for char in email:
                for sc in special_char:
                    if sc in char:
                        return True
                    else:
                        return False
            