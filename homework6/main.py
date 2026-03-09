from classes import Users, Books, UserBooks

users = Users()
users.add("Alice", "alice@example.com")
users.add("Bob", "bob@example.com")

books = Books()
books.add("Book Title", "Author Orwell", 1949)

user_books = UserBooks()
user_books.add_book(1, 1)

print("Alice's books:", user_books.get_books(1))