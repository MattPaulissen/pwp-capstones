from abc import ABC, abstractmethod


class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("User {} email has been updated!".format(self.name))

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        total = 0
        div_by = 0
        if len(self.books) > 0:
            for book in self.books:
                if self.books[book] is not None:
                    total += self.books[book]
                    div_by += 1
            return total / div_by
        else:
            return 0

    def __repr__(self):
        return "User {user}, email: {email}, books read: {books_read}".format(user=self.name, email=self.email, books_read=len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False


class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn
        print("{book} isbn has been updated to {isbn}".format(book=self.title, isbn=self.isbn))

    def add_rating(self, rating):
        if rating is not None:
            if 4 >= rating >= 0:
                self.ratings.append(rating)
            else:
                print("Invalid Rating")
        else:
            print("Invalid Rating")


    def get_average_rating(self):
        total = 0
        for rating in self.ratings:
            total += rating
        try:
            return total / len(self.ratings)
        except ZeroDivisionError:
            return 0

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return False

    def __repr__(self):
        return self.title


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super(Fiction, self).__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super(Non_Fiction, self).__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)


class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, isbn, author):
        return Fiction(title, isbn, author)

    def create_non_fiction(self, title, isbn, subject, level):
        return Non_Fiction(title, isbn, subject, level)

    def add_book_to_user(self, book, email, rating=None):
        if email in self.users:
            self.users[email].read_book(book, rating)
            book.add_rating(rating)
            if book in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print("No user with the email {email}".format(email=email))

    def add_user(self, name, email, user_books=None):
        self.users[email] = User(name, email)
        if user_books is not None:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for book in self.books:
            print(book)

    def print_users(self):
        for user in self.users:
            print(self.users[user])

    def most_read_book(self):
        most_read_book = None
        number_of_reads = 0
        for book in self.books:
            if self.books[book] > number_of_reads:
                most_read_book = book
                number_of_reads = self.books[book]
        return most_read_book

    def highest_rated_book(self):
        highest_rated_book = None
        highest_rating = 0
        for book in self.books:
            if book.get_average_rating() > highest_rating:
                highest_rated_book = book
                highest_rating = book.get_average_rating()
        return highest_rated_book

    def most_positive_user(self):
        most_positive_user = None
        highest_average_rating = 0
        for email in self.users:
            if self.users[email].get_average_rating() > highest_average_rating:
                most_positive_user = self.users[email]
                highest_average_rating = self.users[email].get_average_rating()
        return most_positive_user
