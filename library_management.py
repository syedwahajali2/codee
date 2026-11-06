books = {
    "B101": {"title": "Python Basics", "available": True},
    "B102": {"title": "Data Science Intro", "available": True},
    "B103": {"title": "Learning Matplotlib", "available": False},
}

def show_books():
    print("\nLibrary Books")
    for book_id, book in books.items():
        status = "Available" if book["available"] else "Borrowed"
        print(book_id, "-", book["title"], "-", status)

def borrow_book(book_id):
    if book_id not in books:
        print("Book not found.")
    elif not books[book_id]["available"]:
        print("This book is already borrowed.")
    else:
        books[book_id]["available"] = False
        print("Book borrowed successfully.")

def return_book(book_id):
    if book_id not in books:
        print("Book not found.")
    else:
        books[book_id]["available"] = True
        print("Book returned successfully.")

while True:
    print("\n1. Show books")
    print("2. Borrow book")
    print("3. Return book")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        show_books()
    elif choice == "2":
        borrow_book(input("Enter book ID: ").upper())
    elif choice == "3":
        return_book(input("Enter book ID: ").upper())
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
