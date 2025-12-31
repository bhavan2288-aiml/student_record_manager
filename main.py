students={}
def add_student():
    name=input("enter the name of student:")
    marks=input("enter the marks:")
    students[name]=marks
    print("student added successfully!\n")
def view_students():
    if not students:
        print("no record found.\n")
    else:
        for name,marks in students.items():
            print(f"{name}:{marks}\n")
def delete_students():
    name=input("enter the name of student:")
    if name in students:
        del students[name]
        print("deleted student successfully!\n")
    else:
        print("no record found\n")
def save_to_file(students):
    with open("students.txt","w") as file:
        for name,marks in students.items():
            file.write(f"{name},{marks}\n")
    print("data saved to file.\n")
def load_from_file():
    students={}
    try:
        with open("students.txt","r") as file:
            for line in file:
                name,marks=line.strip().split(",")
                students[name]=int(marks)
    except FileNotFoundError:
        pass
    return students
students=load_from_file()
while True:
    print("1.add student")
    print("2.view student")
    print("3.delete student")
    print("4.save & exit")
    choice=int(input("enter an option:"))
    if choice==1:
        add_student()
    elif choice==2:
        view_students()
    elif choice==3:
        delete_students()
    elif choice==4:
        save_to_file(students)
        print("goodbye!")
        break
    else:
        print("invalid choice\n")

    
