from Small_Projects.Library_management_sytem.data import Book, Library

library = Library()

book1 = Book("Helsreach", "Adam Dembski- Bowden", "00001", 2, 20)
book2 = Book("Assasinorum: Kingmaker", "Robert Rath", "00002", 5, 30)

library.add_book(book1)
library.add_book(book2)

library.checkout_book("00001")
library.display_books()

library.return_book("00001")

library.display_books()
