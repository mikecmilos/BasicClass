class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price


class Periodical(Publication):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher


class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        self.author = author
        self.pages = pages


class Magazzine(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, period, publisher)


class Newspaper(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, period, publisher)


b1 = Book("Brawe New World", "Aldous Huxlet", 311, 29.0)
n1 = Newspaper("NY Times", "New York Time Company", 6.0, "Daily")
m1 = Magazzine("Scientific American", "Springer Nature", 5.99, "Monthly")

print(b1.author)
print(n1.publisher)
print(b1.price, m1.price, n1.price)
