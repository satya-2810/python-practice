def add_student(students):
    roll = input("Enter roll number:").strip()
    if not roll:
        print("Roll number cannot be blank")
        return
    name = input("Enter name:").strip()
    if not name:
        print("Name cannot be empty")
        return
    grade = input("Enter grade:").strip()
    if not grade:
        print("Grade cannot be empty")
        return
    try:
        mark = int(input("Enter the marks:"))
        if mark > 100 or mark < 0:
            print("Marks must be between 0 and 100")
            return
    except ValueError:
        print("Mark must be a number")
        return
    students.append({"roll": roll, "name": name, "grade": grade, "marks": mark})
    print("Student Records Added")

def display_students(students):
    if not students:
        print("No Student Recorded yet")
    else:
        print(f"{'Roll':<5} {'Name':<15} {'Grade':<5} {'marks':<5}")
        
        for row in students:
            print(f"{row['roll']:<5} {row['name']:<15} {row['grade']:<5} {row['marks']:<5}")    
    
def search_student(students):
    if not students:
        print("No Students Recorded yet")
    else:
        req_roll = input("Enter the roll number of the student")
        if not req_roll:
            print("This field cannot be empty")
            return
        found=False
        for student in students:
            if req_roll==student['roll']:
                print(f"{'Roll':<5} {'Name':<15} {'Grade':<5} {'marks':<5}")
                print(f"{student['roll']:<5} {student['name']:<15} {student['grade']:<5} {student['marks']:<5}")
                found=True
        if not found:
            print("Student not Found!")

def update_marks(students):
    if not students:
        print("No Students Recorded yet")
    else:
        roll_to_update = input("Enter the roll number of the student you want to update the marks of: ")
        found = False
        for student in students:
            if roll_to_update == student["roll"]:
                found = True
                try: 
                    updated_mark = int(input("Enter the updated mark: "))
                    if updated_mark > 100 or updated_mark < 0:
                        print("Marks must be between 0 and 100")
                        return
                except ValueError:
                    print("Input must be a number")
                    return
                student["marks"] = updated_mark
                print("Student Mark Updated Successfully")
                break
        if not found:
            print("No Student Found!")
        
    
def delete_record(students):
    if not students:
        print("No Students Recorded yet")
    else:
        roll_to_delete = input("Enter the roll number of the student you want to delete: ")
        found = False
        for index, student in enumerate(students):
            if roll_to_delete == student["roll"]:
                found = True
                students.pop(index)
                print("Student Record Deleted Successfully")
                break
        if not found:
            print("No Student Found!")

students = []
while True:
    try:
        choice = int(input("""
                            Choose the operation: 
                            1. Add Student Record
                            2. Display Students Records
                            3. Search a Student
                            4. Update Marks of a Student
                            5. Delete a Student Record
                            6. Quit
                           """))
        if choice==1:
            add_student(students)
        elif choice==2:
            display_students(students)
        elif choice==3:
            search_student(students)
        elif choice==4:
            update_marks(students)
        elif choice==5:
            delete_record(students)
        elif choice==6:
            break
        else:
            print("Invalid Input: Enter a number between 1 to 6")   
    except ValueError:
        print("Invalid Input: Input must be a number")