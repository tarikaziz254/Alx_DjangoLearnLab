from relationship_app.models import Author, Book, Library, Librarian

#query all books by specific author
author = Author.objects.create(name = 'Jane Austen')
books_by_author = Book.objects.filter(author = author)
print('Book by Jane Austen')
for book in books_by_author:
    print(book.title)

#list all books in library
library = Library.objects.get(name = 'Nairobi')
books_in_library = library.books.all()
for book in books_in_library:
    print(book.title)

#retrieve the librarian for a library
librarian = Librarian.objects.get(library = library )
print("librarian of Nairobi", librarian.name)