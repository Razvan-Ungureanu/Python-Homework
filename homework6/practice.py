class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


book1 = Book("1984", "George Orwell", 1949)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

print(book1.get_info())
print(book2.get_info())