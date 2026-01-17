class person:
    def __init__(self,name= None, age= None):
        self.name= name
        self.age= age
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Employee(person):
    def __init__(self, employee_id=None, name=None, age=None, salary=None):
        super().__init__(name,age)
        self.__employee_id= employee_id
        self.__salary= salary

    @property
    def employee_id(self):
        return self.__employee_id
    @employee_id.setter
    def employee_id(self, new_id):
        self.__employee_id= new_id

    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, new_salary):
        self.__salary= new_salary

    def display(self):
        super().display()
        print("Employee ID:", self.__employee_id)
        print("Salary:", self.__salary)

class Manager(Employee):
    def __init__(self, employee_id=None, name=None, age=None, salary=None, department=None):
        super().__init__(employee_id, name, age, salary)
        self.department=department

    def display(self):
        super().display()
        print("Department:", self.department)

class Developer(Employee):
    def __init__(self, employee_id=None, name=None, salary=None, programming_language=None):
        super().__init__(employee_id, name, age, salary)
        self.programming_language=programming_language

    def display(self):
        super().display()
        print("Programming Language:", self.programming_language)

persons= []
employees= []
managers= []
developers= []
print("---Python OOP Project: Employee Management System---")

while True:
    print("\n Choose an Operation:")
    print("1.Create a Person")
    print("2.Create an Employee")
    print("3.Create a Manager")
    print("4.Show Details")
    print("5.Exit")

    choice = int(input("Enter your choice:"))
    match choice:

        case 1:
            name= input("Enter Name:")
            age= int(input("Enter Age:"))
            persons.append(person(name, age))
            print("Person added successfully.")

        case 2:
            name= input("Enter Name:")
            age= int(input("Enter Age:"))
            emp_id= input("Enter Employee ID:")
            salary= float(input("Enter Salary:"))
            employees.append(Employee(emp_id,name,age,salary))
            print("Employee added successfully")

        case 3:
            name= input("Enter Name:")
            age= int(input("Enter Age:"))
            emp_id= input("Enter Employee ID:")
            salary= float(input("Enter Salary:"))
            department= input("Enter Department:")
            managers.append(Manager(emp_id,name,age,salary,department))
            print("Manager added successfully")
        
        case 4:
            name= input("Enter Name:")
            age= int(input("Enter Age:"))
            emp_id= input("Enter Employee ID:")
            salary= float(input("Enter Salary:"))
            language= input("Enter Programming Language:")
            developers.append(Developer(emp_id,name,age,salary,language))
            print("Developer added successfully")

        case 5:
            print("n\Show Redords:")
            print("1.Persons")
            print("2.Employees")
            print("3.Managers")
            print("4.Developers")
            print("5.Show all")
            print("6.Subclass check")

            sub_choice= int(input("Enter your choice:"))

            match sub_choice:

                case 1:
                    if persons:
                        for p in persons:
                            p.display()
                            print("-"*20)
                    else:
                        print("No Person record found!")

                case 2:
                    if employees:
                        for e in employees:
                            e.display()
                            print("-"*20)
                    else:
                        print("No Employee record found!")

                case 3:
                    if managers:
                        for m in managers:
                            m.display()
                            print("-"*20)
                    else:
                        print("No Manager record found!")

                case 4:
                    if developers:
                        for d in developers:
                            d.display()
                            print("-"*20)
                    else:
                        print("No Developer record found!")

                case 5:
                    for p in persons:
                        p.display()
                        print("-" * 20)

                    for e in employees:
                        e.display()
                        print("-" * 20)

                    for m in managers:
                        m.display()
                        print("-" * 20)

                    for d in developers:
                        d.display()
                        print("-" * 20)

                case 6:
                    print("Is Manager subclass of Employee?", issubclass(Manager,Employee))
                    print("Is Developer subclass of Employee?", issubclass(Developer,Employee))

                case _:
                    print("Invalid Option!")

        case 6:
                    print("Exiting the system. Goodbye!")
                    break

        case _:
                    print("Invalid choice. Try again.")

                    


