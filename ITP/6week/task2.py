class Book:
    title = ''
    author = ''
    year = 0000
    available = True

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def checkout(self):
        if self.available:
            self.available = False
            print(f'You have checked out "{self.title}" by {self.author}.')
        else:
            print(f'Sorry, "{self.title}" is currently unavailable.')

    def return_book(self):
        self.available = True
        print(f'You have returned "{self.title}" by {self.author}.')

    def book_age(self):
        return 2026 - self.year

    def __str__(self):
        return f'"{self.title}" by {self.author}, {self.year} [{"Available" if self.available else 'Checked out'}]'


b = Book('Clean Code', 'Robert Martin', 2008)
print(b)
b.checkout()
print(b)
b.checkout()
b.return_book()
print(b.book_age())