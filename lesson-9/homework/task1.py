class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.status = "Available"
    def __str__(self):
        return f"'{self.title}' by {self.author}, status: {self.status}"

class Member:
    def __init__(self,name):
        self.name =name
        self.borrowed_books = 0
    def __str__(self):
        return f"Member: {self.name}, Borrowed Books: {self.borrowed_books}"
    
class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def adding_books(self, book: Book):
        if book.title in self.books:
            print(f"'{book.title}' already exists in the library.\n")
        else:
            self.books[book.title] = book
            print("A new book added successfully!\n")

    def adding_member(self, member: Member):
        if member.name in self.members:
            print(f"Member '{member.name}' already exists.\n")
        else:
            self.members[member.name] = member
            print("A new member added successfully!\n")

    def rules(self,book:Book,member: Member):
        try:
            if member.name not in self.members.keys():
                raise Exception('Member Not Found!\n')
            elif self.members[member.name].borrowed_books >=3:
                raise Exception('Member Limit Exceeded!\n')
            elif book.title not in self.books.keys():
                raise Exception('Book Not Found!\n')
            elif book.author != self.books[book.title].author:  
                raise Exception('Author Mismatch!\n') 
            elif self.books[book.title].status == 'Borrowed':
                raise Exception('Book Already Borrowed!\n')

        except Exception as error:
            print(error) 
            return False
        else:
            return True

    def borrowing_books(self):
        member_name = input("Enter your name: ")
        book_title = input("Enter Book's title you want to borrow: ")
        book_author = input("Enter Book's author you want to borrow: ")
        book_to_borrow = Book(book_title,book_author)
        borrower = Member(member_name)
        if self.rules(book_to_borrow, borrower):
            self.books[book_title].status = 'Borrowed'
            self.members[member_name].borrowed_books += 1
            print("A book has been successfully borrowed!\n")

    def returning_books(self):
        member_name = input("Enter your name: ")
        book_title = input("Enter Book's title you want to return: ")
        book_author = input("Enter Book's author you want to return: ")
        if book_title in self.books and member_name in self.members:
            self.books[book_title].status = 'Available'
            self.members[member_name].borrowed_books -= 1
            print("A book has been successfully returned!\n")
    def run(self):
        while True:
            print("Welcome to the Library App!\n")
            print("1. Add a new book.")
            print("2. Add a new member.")
            print("3. Borrowing books.")
            print("4. Returning books.")
            print("5. Exit.")    
            option = input("Choose Option: ")
            if option == '1':
                new_title = input("Enter Title: ")
                new_author = input("Enter Author: ")
                new_book = Book(new_title,new_author)
                self.adding_books(new_book)
            elif option == '2':
                new_name = input("Enter name: ")
                new_member = Member(new_name)
                self.adding_member(new_member)
            elif option == '3':
                self.borrowing_books()
            elif option == '4':
                self.returning_books()
            elif option == '5':
                print("Good Bye!")
                break
            else:
                print("Invalid choice!")
            
if __name__ == "__main__":
    app = Library()
    app.run()








