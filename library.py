class Library:

    def _init_(self):
        self.load_books()
        self.load_issued()

    def load_books(self):
        try:
            f = open("library_books.txt", "r")
            self.books = f.readlines()
            f.close()
        except:
            f = open("library_books.txt", "w")
            f.close()
            self.books = []

    def load_issued(self):
        try:
            f = open("issued.txt", "r")
            self.issued = f.readlines()
            f.close()
        except:
            f = open("issued.txt", "w")
            f.close()
            self.issued = []
    def add_book(self):
        bid = input("Enter Book ID: ")
        name = input("Enter Book Name: ")
        author = input("Enter Author: ")

        line = bid + "," + name + "," + author + "\n"

        f = open("library_books.txt", "a")
        f.write(line)
        f.close()

        print("Book Added!")
        self.load_books()

    
    def display_available(self):
        print("\n--- Available Books ---")
        for b in self.books:
            if b not in self.issued:   
                print(b, end="")

    
    def issue_book(self):
        stu = input("Student Name: ")
        bid = input("Enter Book ID to Issue: ")

        found_line = None

        
        for b in self.books:
            if bid + "," in b:   
                found_line = b
                break

        if found_line is None:
            print("Book Not Found!")
            return

        if found_line in self.issued:
            print("Book Already Issued!")
            return

        issue_line = stu + ":" + found_line

        f = open("issued.txt", "a")
        f.write(issue_line)
        f.close()

        print("Book Issued!")
        self.load_issued()

    
    def return_book(self):
        stu = input("Student Name: ")
        bid = input("Enter Book ID to Return: ")

        remove_line = None

        for i in self.issued:
            if stu + ":" in i and bid + "," in i:
                remove_line = i
                break

        if remove_line is None:
            print("No Such Issued Record!")
            return

        new_data = ""
        for i in self.issued:
            if i != remove_line:
                new_data += i

        f = open("issued.txt", "w")
        f.write(new_data)
        f.close()

        print("Book Returned!")
        self.load_issued()


lib = Library()

while True:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. Display Available Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    ch = input("Enter Choice: ")

    if ch == "1":
        lib.add_book()
    elif ch == "2":
        lib.display_available()
    elif ch == "3":
        lib.issue_book()
    elif ch == "4":
        lib.return_book()
    elif ch == "5":
        break
    else:
        print("Invalid Choice!")