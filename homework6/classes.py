import db

class Users:
    def add(self, name: str, email: str):
        return db.insert_user(name, email)

    def list(self):
        return db.get_all_users()

    def get(self, user_id: int):
        return db.get_user(user_id)

    def delete(self, user_id: int):
        return db.delete_user(user_id)


class Books:
    def add(self, title: str, author: str, year: int):
        return db.insert_book(title, author, year)

    def list(self):
        return db.get_all_books()

    def get(self, book_id: int):
        return db.get_book(book_id)

    def delete(self, book_id: int):
        return db.delete_book(book_id)


class UserBooks:
    def add_book(self, id_user: int, id_book: int):
        success = db.insert_user_book(id_user, id_book)
        if not success:
            print(f"User {id_user} already has book {id_book}.")
        return success

    def get_books(self, id_user: int):
        book_ids = db.get_user_book_ids(id_user)
        return [db.get_book(bid) for bid in book_ids if db.get_book(bid)]

    def has_read_book(self, id_user: int, id_book: int) -> bool:
        return id_book in db.get_user_book_ids(id_user)

    def remove_book(self, user_id: int, book_id: int):
        return db.remove_user_book(user_id, book_id)