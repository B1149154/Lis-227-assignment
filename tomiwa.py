class Book:
    def __init__(self, title, author, isbn, quantity):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.quantity = quantity

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]

    def search_book(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]

    def display_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books:
                print(f"{book.title} by {book.author} (ISBN: {book.isbn}, Quantity: {book.quantity})")
        else:
            print("No books in the library.")

def main():
    library = Library()

    while True:
        print("\n1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Display All Books")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            isbn = input("Enter the ISBN of the book: ")
            quantity = int(input("Enter the quantity of the book: "))
            book = Book(title, author, isbn, quantity)
            library.add_book(book)
            print("Book added successfully!")

        elif choice == 2:
            isbn = input("Enter the ISBN of the book to remove: ")
            library.remove_book(isbn)
            print("Book removed successfully!")

        elif choice == 3:
            title = input("Enter the title to search: ")
            found_books = library.search_book(title)
            if found_books:
                print("Found Books:")
                for book in found_books:
                    print(f"{book.title} by {book.author} (ISBN: {book.isbn}, Quantity: {book.quantity})")
            else:
                print("Book not found.")

        elif choice == 4:
            library.display_books()

        elif choice == 5:
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
