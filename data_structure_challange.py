library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book(name,author):
    if (name, author) in library:
        print('You cannot add a duplicate book!')
    else:
        library.append((name,author))

    print(library)

def remove_book(name,author):
    try:
        library.pop(library.index((name,author)))
    except:
        print(f'The book "{name}" does not exist in the library, please try')
    else:
        print(f'The book "{name}" has been removed from the Library')

def view_books():
    for item in library:
        title, author = item
        print(f"{title} by: {author}")

def main():
    while True:
        option = input('''\n\t\t  What would you like to do?
                       1. Add a book
                       2. Remove a book
                       3. View all books''')
        if option == '1' or option == '2':
            name = input(f'What is the name of the book you want to {'add' if option == '1' else 'remove'}?')
            author = input("Who's the author of this book?")
            if option == '1':
                add_book(name,author)
            else:
                remove_book(name,author)
        elif option == '3':
            view_books()
        else:
            print("That is not a vlaid option, please try again.")
        
if __name__ == "__main__":
    main()