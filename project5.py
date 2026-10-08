print("***Employee Management System***")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
         return self.age

    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.get_age())

class Employee(Person):
    def __init__(self, name, age, employee_id = None, salary = 0):
        super().__init__(name, age)
        self.__employee_id = employee_id
        self.__salary = salary


    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.get_age())
        print("Employee ID: ", self.get_employee_id())
        print("Salary: ", self.get_salary())

    def __del__(self):
        print("Employee object deleted.")

class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display(self):
        print("Manager Details: ")
        print("Name: ", self.name)
        print("Age: ", self.get_age())
        print("Employee ID: ", self.get_employee_id())
        print("Salary: ", self.get_salary())
        print("Department: ", self.department)


class Developer(Employee):
    def __init__(self, name, age, employee_id, salary, programming_language):
         super().__init__(name, age, employee_id, salary)
         self.programming_language = programming_language

    def display(self):
        print("Developer Details: ")
        print("Name: ", self.name)
        print("Age: ", self.get_age())
        print("Employee ID: ", self.get_employee_id())
        print("Salary: ", self.get_salary())
        print("Programming Language: ", self.programming_language)

person = None
employee = None
manager = None
developer = None
        
while True:
      print("\n---Choose an operation---: ")
      print("1. Create a person")
      print("2. Create an Employee")
      print("3. Create a manager")
      print("4. Create a Developer")
      print("5. Show Details")
      print("6. Exit")

      choice = int(input("\nEnter your choice: "))

      if choice == 1:
          name = input("\nEnter Name: ")
          age = int(input("Enter Age: "))

          person = Person(name, age)
          person.display()

          print(f"\nPerson created with name: {name} and age: {age}")

      elif choice == 2:
           name = input("\nEnter Name: ")
           age = int(input("Enter Age: "))
           employee_id = input("Enter Employee_id: ")
           salary = float(input("Enter Salary: "))

           while salary < 0:
               print("Salary cannot be negative.")
               salary = float(input("Enter your Salary again: "))

           employee = Employee( name, age, employee_id, salary)

           print(f"\nEmployee created with name: {name}, age: {age}, ID: {employee_id}, and salary: $ {salary}.")

      elif choice == 3:
          name = input("\nEnter Name: ")
          age = int(input("Enter Age:" ))
          employee_id = input("Enter Employee ID: ")
          salary = float(input("Enter Salary: "))
          department = input("Enter Department: ")

          manager = Manager(name, age, employee_id, salary, department)
        
          print(f"\nManager created with name: {name}, age: {age},  ID: {employee_id}, salary: $ {salary}, and department: {department}.")
          
      elif choice == 4:
          name = input("\nEnter Name: ")
          age = int(input("Enter Age: "))
          employee_id = input("Enter Employee ID: ")
          salary = float(input("Enter Salary: "))
          programming_language = input("Enter Programming Language: ")

          developer = Developer(name, age, employee_id, salary, programming_language)
          print(f"\nDeveloper created with name: {name}, age: {age}, ID: {employee_id}, salary: ${salary}, and programming language: {programming_language}.")

      elif choice == 5:
          print("\nChoose details to show: ")
          print("\n1. Person")
          print("2. Employee")
          print("3. Manager")
          print("4. Developer")
          print("\nClass Relationship:")
          print("Employee is subclass of Person:", issubclass(Employee, Person))
          print("Manager is subclass of Employee:", issubclass(Manager, Employee))
          print("Developer is subclass of Employee:", issubclass(Developer, Employee))

          detail_choice = int(input("\nEnter your choice: "))

          if detail_choice == 1:
             if person:
                 person.display()
             else:
                 print("Person not created yet.")

          elif detail_choice == 2:
              if employee:
                  employee.display()
              else:
                  print("Employee not created yet.")

          elif detail_choice == 3:
              if manager:
                  manager.display()
              else:
                  print("Manager not created yet.")

          elif detail_choice == 4:
              if developer:
                  developer.display()
              else:
                  print("Developer not created yet.")
                      

      elif choice == 6:
            print("\nExiting the system All resources have been freed.")
            print("\nGoodbye!")
            break
                       
        






        
