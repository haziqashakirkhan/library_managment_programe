books = []
issued_books = []


def add_book():
    book_id = input("Enter Book ID: ")
    name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")
    quantity = int(input("Enter Quantity: "))

    book = {
        "id": book_id,
        "name": name,
        "author": author,
        "quantity": quantity
    }

    books.append(book)

    print("yayy!!Book Added Successfully!\n")

def display_books():

    if len(books) == 0:
        print("oops!No books available.\n")
        return

    print("\nBooks List:")

    for book in books:
        print("Book ID:", book["id"])
        print("Book Name:", book["name"])
        print("Author:", book["author"])
        print("Quantity:", book["quantity"])
        print("-------------------")



def issue_book():

    student = input("Enter Student Name: ")
    book_id = input("Enter Book ID: ")

    for book in books:

        if book["id"] == book_id:

            if book["quantity"] > 0:

                book["quantity"] -= 1

                issued_books.append({
                    "student": student,
                    "book": book["name"]
                })

                print("Book Issued Successfully!\n""happy reading\n")

            else:
                print("SORRY!\n","Book Not Available!\n")

            return

    print("Book ID Not Found!\n")

def return_book():

    book_id = input("Enter Book ID to Return: ")

    for book in books:

        if book["id"] == book_id:

            book["quantity"] += 1

            print("Book Received Successfully!\n")
            return

    print("oops!! Book ID Not Found!\n")


def search_book():

    search = input("Enter Book Name: ")

    for book in books:

        if book["name"].lower() == search.lower():

            print("\nBook Found")
            print("Book ID:", book["id"])
            print("Author:", book["author"])
            print("Quantity:", book["quantity"])
            return

    print("Book Not Found!\n")


def report():

    print("\nTotal Books:", len(books))
    print("Issued Books:", len(issued_books))

    total_quantity = 0

    for book in books:
        total_quantity += book["quantity"]

    print("Available Books:", total_quantity)
    print()


# -------- MAIN MENU --------
while True:

    print("===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Search Book")
    print("6. Report")
    print("7. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        display_books()

    elif choice == "3":
        issue_book()

    elif choice == "4":
        return_book()

    elif choice == "5":
        search_book()

    elif choice == "6":
        report()

    elif choice == "7":
        print("Program Closed\nbyyeeeeeeeeeeeeee")
        break

    else:
        print("Invalid Choice!\ntry again")