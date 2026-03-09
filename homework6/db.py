_users = {}
_books = {}
_user_books = []

_user_counter = 1
_book_counter = 1


def insert_user(name, email):
    global _user_counter
    user = {"id": _user_counter, "name": name, "email": email}
    _users[_user_counter] = user
    _user_counter += 1
    return user

def get_all_users():
    return list(_users.values())

def get_user(user_id):
    return _users.get(user_id)

def delete_user(user_id):
    return _users.pop(user_id, None)


def insert_book(title, author, year):
    global _book_counter
    book = {"id": _book_counter, "title": title, "author": author, "year": year}
    _books[_book_counter] = book
    _book_counter += 1
    return book

def get_all_books():
    return list(_books.values())

def get_book(book_id):
    return _books.get(book_id)

def delete_book(book_id):
    return _books.pop(book_id, None)


def insert_user_book(user_id, book_id):
    if not any(ub["user_id"] == user_id and ub["book_id"] == book_id for ub in _user_books):
        _user_books.append({"user_id": user_id, "book_id": book_id})
        return True
    return False

def get_user_book_ids(user_id):
    return [ub["book_id"] for ub in _user_books if ub["user_id"] == user_id]

def remove_user_book(user_id, book_id):
    global _user_books
    before = len(_user_books)
    _user_books = [ub for ub in _user_books
                   if not (ub["user_id"] == user_id and ub["book_id"] == book_id)]
    return len(_user_books) < before