class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks
    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books:
            print(" *" + book)
    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You've been issued the book named {bookName}. Please return the book within 30 days.")
            self.books.remove(bookName)
            return True
        else:
            print(f"Sorry! The book named {bookName} is either issued to someone else or not available in the library right now. Please try after sometime.\nThank You!")
            return False
    def returnBook(self, bookName):
        self.books.append(bookName)
        print(f"Thank you for returning the book named {bookName}. Hope you enjoyed reading it.")

class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book which you want to borrow: ")
        return self.book
    def returnBook(self):
        self.book = input("Enter the name of the book you want to return/donate: ")
        return self.book
if __name__ == '__main__':
    centralLibrary = Library(["Django", "Think Python", "DSA", "Machine Learning"])
    student = Student()
    while(True):
        welcomeMsg = '''*****Welcome to the Central Library*****
        1. List of All Books
        2. Request Book
        3. Return/Donate Book
        4. Exit Library'''
        print(welcomeMsg)
        try:
            choice = int(input("Enter Your Choice: "))
            if choice == 1:
                centralLibrary.displayAvailableBooks()
            elif choice == 2:
                centralLibrary.borrowBook(student.requestBook())
            elif choice == 3:
                centralLibrary.returnBook(student.returnBook())
            elif choice == 4:
                print("Thank you for choosing the Central Library. Have a great day ahead!")
                exit()
            else:
                print("Invalid choice!")
        except Exception as e:
            print("Invalid Choice! Please enter the valid choice between 1 to 4.")