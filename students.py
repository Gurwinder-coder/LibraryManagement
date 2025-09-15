import json
import os 


class students_data:
    def __init__(self):
        self.all_students= {}
        self.load_data()
    
    def save_data(self):
        with open("all_students_file.json", "w") as f:
            json.dump(self.all_students, f, indent=4)
        
    def load_data(self):
        if os.path.exists("all_students_file.json"):
            with open("all_students_file.json", "r") as f:
                self.all_students = json.load(f)


    ## 1. for adding a student in dictionary
    def add_student(self, student_id, name):
        
        if student_id in self.all_students:
            print("Student id already present, please enter different id.")
            return False
        
        self.all_students[student_id]=name
        self.save_data()
        print(f'student {name} successfully added with id {student_id}')
        return True
    
    ## 2. for removing a student from dictionary 
    def remove_student(self):
        stuid = input("enter student id: ")
        if stuid not in self.all_students:
            print("student not found!!!")
            return False
        name = self.all_students.pop(stuid)
        self.save_data()
        print(f"student {name} removed successfully....")

    ## 3. for displaying all students in dictionary
    def display_all_students(self):
        self.save_data()
        if not self.all_students:
            print("No student added yet.")
            return False
        for student_id, name in self.all_students.items():
            print(f"id= {student_id} name= {name}")
        return True