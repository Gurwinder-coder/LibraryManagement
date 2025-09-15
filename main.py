## Library Management System 

from students import *
from books import *

manager= students_data()
BookManager= books()

while True:
    print("-"*59)
    print("\t\t\tMain Menu")
    print("-"*59)
    print("""\t1. add a new student 
        2. remove student. 
        3. view all students 
        4. add new book
        5. remove book
        6. view all books 
        7. issue a book 
        8. return a book 
        9. view issued books """)
    print("\n")

    choice = int(input("enter your choice (1-9): "))
    if choice not in range (1,10):
        print("Please enter correct choice.")
        break 
    
    match choice:
        case 1:
            stuid = (input("enter student id: "))
            stuname  = input("enter student name: ")
            manager.add_student(stuid, stuname)  

        case 2:
            manager.remove_student()

        case 3:
            manager.display_all_students()
        
        case 4:
            id = input("enter book id: ")
            name = input("enter the name of book: ")
            BookManager.add_books(id,name)

        case 5:
            BookManager.remove_book()

        case 6:
            BookManager.view_all_books()

        case 7:
            stuid = input("enter student id: ")
            id = input("enter book id: ")
            BookManager.issue_book(stuid, id)

        case 8:
            BookManager.return_book()

        case 9:
            BookManager.view_issued_books()
