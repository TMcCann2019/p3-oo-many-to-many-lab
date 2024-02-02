class Author:
    all_authors = []

    def __init__(self, name):
        self.name = name
        self.contracts_list = []
        self.all_authors.append(self)

    def contracts(self):
        return [contract for contract in Contract.all_contracts if contract.author == self]
    
    def books(self):
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book) or not isinstance(date, str) or not isinstance(royalties, int):
            raise Exception("Invalid input for contract")
        contract = Contract(self, book, date, royalties)
        self.contracts_list.append(contract)
        return contract
    
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])
    pass


class Book:
    all_books = []

    def __init__(self, title):
        self.title = title
        self.all_books.append(self)

    def contracts(self):
        return [contract for contract in Contract.all_contracts if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in Contract.all_contracts if contract.book == self]
    pass


class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Invalid input for author")
        else:
            self.author = author
        if not isinstance(book, Book):
            raise Exception("Invalid input for book")
        else:
            self.book = book
        if not isinstance(date, str):
            raise Exception("Invalid input for date")
        else:
            self.date = date
        if not isinstance(royalties, int):
            raise Exception("Invalid input for royalties")
        else:
            self.royalties = royalties
        self.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all_contracts if contract.date == date]
    
    def __str__(self):
        return f"{self.author.name} signed a contract for {self.book.title} on {self.date} with {self.royalties} royalties"
    
    def __repr__(self):
        return self.__str__()
    
# author1 = Author("Name 1")
# book1 = Book("Title 1")
# book2 = Book("Title 2")
# book3 = Book("Title 3")
# author2 = Author("Name 2")
# book4 = Book("Title 4")
# contract1 = Contract(author1, book1, "02/01/2001", 10)
# contract2 = Contract(author1, book2, "01/01/2001", 20)
# contract3 = Contract(author1, book3, "03/01/2001", 30)
# contract4 = Contract(author2, book4, "01/01/2001", 40)

# print(Contract.contracts_by_date("01/01/2001"))