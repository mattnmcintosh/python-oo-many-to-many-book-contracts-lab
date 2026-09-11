class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return list({contract.book for contract in self.contracts()})

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return list({contract.author for contract in self.contracts()})


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value
        else:
            raise Exception("Author must be an instance of the Author class")

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if isinstance(value, Book):
            self._book = value
        else:
            raise Exception("Book must be an instance of the Book class")

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if isinstance(value, str):
            self._date = value
        else:
            raise Exception("Date must be a string")

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        # Explicit check for bool because Python treats bool as a subclass of int,
        # which would otherwise allow True/False to pass an isinstance(value, int) check.
        if isinstance(value, int) and not isinstance(value, bool):
            self._royalties = value
        else:
            raise Exception("Royalties must be an integer")

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]