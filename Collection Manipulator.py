students={}
while True:
    print("Select an option:")
    print("Display all Students")
    print("Update Student Information")
    print("Delete Student")
    print("Display Subject Offered")
    print("Exit")

    choice= int(input("Enter your Choice:"))
    match choice:
        case 1:
            stud_id= int(input("Student id:"))
            name= input("Name:")
            age= int(input("Age:"))
            grade= input("Grade:")
            dob= int(input("Date of Birth:"))
            subjects: input("Subjects (coma-separated):")


            students[stud_id]={
                "name": name,
                "age": age,
                "grade": grade,
                "date_of_birth": dob,
                "subjects": subjects
            }

            print("Students added succesfully!")
            print()       

        case 2:
              print("---Display all students---")
              for sid, i in students.items():
               print(
            "Student ID:", sid,
            "| Name:", i["Name"],
            "| Age:", i["Age"],
            "| Grade:", i["Grade"],
            "| Date_of_birth:", i["Date_of_birth"],
            "| Subjects:", i["Subjects"]
                    )
              print()


        case 3:
            while True:
                sid= int(input("Enter student id for update:"))

                if sid in students:
                    print("Enter the details.")

                    students[sid]["Name"]= input("Enter the Name:")
                    students[sid]["Age"]= input("Enter the Age:")
                    students[sid]["Grade"]= input("Enter the Grade:")
                    students[sid]["Date_of_birth"]= input("Enter the Date_of_birth:")
                    students[sid]["Subjects"]= input("enter the Subjects:")

                    print("Student imformation update successfully!")
                    break
                else:
                    print("Student not found!")

        case 4:
            sid = int(input("Enter student id for Delete:"))

            if sid in students:
                students.pop(sid)
                print("Student record delete succesfully!")
            else:
                print("Student not found!")

        case 5:
            print("---Display Subjects Offered---")
            subject= ["English", "Maths", "Gujarati", "Sanskrit"]

            for i in subject:
                print(i)

            print()

        case 6:
            print("Exit")
            break                                   



                

                      
                

                         


            


    
