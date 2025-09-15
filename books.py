from datetime import datetime 
from students import students_data
import json
import os


class books:
    def __init__(self):
        self.all_books= {}
        self.issued_books={}
        self.load_data()
        self.student_obj= students_data()

    
    def save_data(self):
        with open("all_books.json","w") as f:
            json.dump(self.all_books,f,indent=4)
        with open("issued_books.json","w") as f:
            json.dump(self.issued_books,f,indent=4)
    

    def load_data(self):
        if os.path.exists("all_books.json"):
            with open("all_books.json", "r") as f:
                self.all_books= json.load(f)
        if os.path.exists("issued_books.json"):
            with open("issued_books.json","r") as f:
                self.issued_books= json.load(f)


    def add_books(self, book_id, book_name):
        if book_id in self.all_books:
            print(f"book id {book_id} already exists.......")
            return False
        self.all_books[book_id] = book_name
        self.save_data()
        print(f"{book_name} successfully added with id {book_id}")
        return True
    

    def remove_book(self):
        BookId= input("enter the book ID: ")
        if BookId not in self.all_books:
            print(f"{BookId} does not found, please enter correct Book ID.")
            return False
        book = self.all_books.pop(BookId)
        self.save_data()
        print(f"{book} removed successfully......")


    def view_all_books(self):
        if not self.all_books:
            print("No books added yet.....")
            return False
        print("..........All Books.......")
        for bookid, name in self.all_books.items():
            print(f"ID= {bookid} name= {name}")
        return True
        
        
    def issue_book(self, student_id, book_id):
        if book_id in self.issued_books:
            print(f"{book_id} already issued.")
            return False
        elif book_id not in self.all_books:
            print("Book is not available.")
            return False
        elif student_id not in self.student_obj.all_students:
            print("student id is not added yet..")
            return False
        date = datetime.now().strftime("%d/%m/%y, %H:%M:%S")
        student_name = self.student_obj.all_students.get(student_id, "Unknown Student")
        self.issued_books[book_id]= {
            'student_id':student_id,
            'student_name':student_name,
            'book_id':book_id,
            'issued_date':date,
            'return_date':None
        }
        self.save_data()
        
        print(f"book: {self.all_books[book_id]} issued to {student_name} with id:{self.issued_books[book_id]['student_id']}  on date: {date}")

    
    def return_book(self):
        id = input("enter the ID of the book: ")
        if id not in self.issued_books:
            print("please enter correct book ID.....")
            return False
        returned_date = datetime.now().strftime("%d/%m/%y, %H:%M:%S")
        self.issued_books[id]['return_date']= [returned_date]
        student_id = self.issued_books[id]['student_id']
        print(f"book {id} returned by student {student_id} on date {returned_date}")
        del self.issued_books[id]
        self.save_data()
        return True
    

    def view_issued_books(self):
        if not self.issued_books:
            print("No book is issued yet.......")
            return False
        for bookID, detais in self.issued_books.items():
            print(f"""book ID: {bookID}
                student ID: {detais['student_id']}
                issued date: {detais['issued_date']}
                returned date: {detais['return_date']}""")
        return True