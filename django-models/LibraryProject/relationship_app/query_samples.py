from relationship_app.models import Author, Book, Library, Librarian

author1 = Author.objects.create(name = 'Jane Austen')
author1.save()
author2 = Author.objects.create(name = 'Tarik Aden')
author2.save()
author3 = Author.objects.create(name = 'Chinua Chebe')
author3.save()
book1 = Book.objects.create(name = "Pride and Prejudice", author = author1 )
book1.save()
book2 = Book.objects.create(name = "Things fall apart", author = author2)
book2.save()
book3 = Book.objects.create(name = 'We will meet again', author = author3)
book3.save()
library1 = Library.objects.create(name = "Nairobi", books = [book1, book2, book3] )
library1.save()
librarian1 = Librarian.objects.create(name = "Tarik", library = library1)
librarian1.save()

books = Book.objects.filter(author = author1)
print(books)

for book in books:
    print(book)

librarian = Library.objects.get(Librarian = librarian1)
print(librarian)





