import sqlite3

DATABASE_FILE = "library.db"

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

def add_book_to_database(book):
    try:
        connection = sqlite3.connect(DATABASE_FILE)
        cursor = connection.cursor()

        # Create a table if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                            title TEXT,
                            author TEXT,
                            isbn TEXT,
                            available INTEGER
                        )''')

        # Insert the book data into the table
        cursor.execute("INSERT INTO books VALUES (?, ?, ?, ?)",
                       (book.title, book.author, book.isbn, book.available))

        connection.commit()
        connection.close()
    except sqlite3.Error as e:
        print("Error adding book to the database:", e)

def search_book_by_title(title):
    try:
        connection = sqlite3.connect(DATABASE_FILE)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM books WHERE title LIKE ?", ('%' + title + '%',))
        search_result = cursor.fetchall()

        connection.close()
        return search_result
    except sqlite3.Error as e:
        print("Error searching for books:", e)
        return None

def borrow_book(member, book):
    # Implement book borrowing logic
    pass

def return_book(member, book):
    # Implement book returning logic
    pass

def show_menu():
    print("1. Add a book")
    print("2. Search for a book")
    print("3. Borrow a book")
    print("4. Return a book")
    print("5. Exit")

# Main program loop
while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        isbn = input("Enter book ISBN: ")
        new_book = Book(title, author, isbn)
        add_book_to_database(new_book)
        print("Book added successfully.")

    elif choice == '2':
        title = input("Enter book title to search: ")
        search_result = search_book_by_title(title)
        # Display search results
        if search_result:
            print("Search results:")
            for book_data in search_result:
                print(f"Title: {book_data[0]}, Author: {book_data[1]}, ISBN: {book_data[2]}")
        else:
            print("No matching books found.")

    elif choice == '3':
        # Implement book borrowing logic
        pass

    elif choice == '4':
        # Implement book returning logic
        pass

    elif choice == '5':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")
