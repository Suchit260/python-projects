class Book:
    def __init__(self, author, title, year, availability = True):
        self.author = author
        self.title = title
        self.year = year
        self.availability = availability
    
    def __str__(self):
        return (f"Book: {self.title}, "
                f"Author: {self.author}, "
                f"{'Available' if self.availability else 'Unavailable'}")

    def borrow(self):
        if self.availability == True:
            print("You can borrow")
        else:
            print("Already taken")

    def returning(self):
        if self.availability == False:
            print("You need to return")
        else:
            print("Already returned")
    

book1 = Book("Doyle", "Sherlock Holmes", 1892)
print(book1)