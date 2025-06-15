import json
import os

# === File Handling ===
FILE_NAME = 'books.json'

def load_books():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return []

def save_books(book_list):
    with open(FILE_NAME, 'w') as file:
        json.dump(book_list, file, indent=4)

# === Core Functionalities ===

def add_book():
    new_book = {
        "title": input("Enter Book Title: "),
        "author": input("Enter Author Name: "),
        "isbn": input("Enter ISBN Number: "),
        "status": "available"
    }
    books = load_books()
    books.append(new_book)
    save_books(books)
    print("\n✅ Book added successfully!\n")

def display_books():
    books = load_books()
    if not books:
        print("\n⚠️ No books found.\n")
        return
    print("\n📚 Book List:")
    for idx, book in enumerate(books, 1):
        print(f"{idx}. Title: {book['title']} | Author: {book['author']} | ISBN: {book['isbn']} | Status: {book['status']}")
    print()

def issue_book():
    isbn = input("Enter ISBN to issue: ")
    books = load_books()
    for book in books:
        if book['isbn'] == isbn and book['status'] == 'available':
            book['status'] = 'issued'
            save_books(books)
            print("\n📦 Book issued successfully!\n")
            return
    print("\n❌ Book not available or already issued.\n")

def return_book():
    isbn = input("Enter ISBN to return: ")
    books = load_books()
    for book in books:
        if book['isbn'] == isbn and book['status'] == 'issued':
            book['status'] = 'available'
            save_books(books)
            print("\n✅ Book returned successfully!\n")
            return
    print("\n❌ Book not found or not issued.\n")

def search_book():
    keyword = input("Search by Title or ISBN: ").strip().lower()
    books = load_books()
    found = False
    for book in books:
        if keyword == book['title'].lower() or keyword == book['isbn'].lower():
            print(f"\n🔍 Book Found: Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Status: {book['status']}\n")
            found = True
    if not found:
        print("\n❌ No matching book found.\n")

# === Menu ===

def main():
    while True:
        print("======== Library Management System ========\n")
        print("1. Add a New Book")
        print("2. Display All Books")
        print("3. Issue a Book")
        print("4. Return a Book")
        print("5. Search for a Book")
        print("6. Exit")
        choice = input("\nChoose an option (1-6): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            display_books()
        elif choice == '3':
            issue_book()
        elif choice == '4':
            return_book()
        elif choice == '5':
            search_book()
        elif choice == '6':
            print("\n👋 Exiting the system. Goodbye!\n")
            break
        else:
            print("\n⚠️ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
