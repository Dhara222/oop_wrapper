<div align="center">

# 👨‍💼 EMPLOYEE MANAGEMENT SYSTEM

### 🐍 Python OOP Mini Project

<p>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/OOP-Inheritance%20%7C%20Encapsulation-7C3AED?style=for-the-badge">
  <img src="https://img.shields.io/badge/Project-Mini%20Project-0EA5E9?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Completed-16A34A?style=for-the-badge">
</p>

**A menu-driven Python application for creating and displaying Person, Employee, Manager, and Developer details using Object-Oriented Programming.**

</div>

---

## 📑 Table of Contents

- [📌 About the Project](#-about-the-project)
- [✨ Features](#-features)
- [🏗️ Class Hierarchy](#️-class-hierarchy)
- [🔄 Program Flowchart](#-program-flowchart)
- [🧠 OOP Concepts Used](#-oop-concepts-used)
- [🖥️ Actual Program Output](#️-actual-program-output)
- [📸 Screenshots](#-screenshots)
- [🎬 Project Demo Video](#-project-demo-video)
- [🛠️ Technologies Used](#️-technologies-used)
- [📁 Project Structure](#-project-structure)
- [🚀 Future Improvements](#-future-improvements)
- [🎯 Learning Outcomes](#-learning-outcomes)
- [👩‍💻 Author](#-author)

---

## 📌 About the Project

The **Employee Management System** is a beginner-friendly, menu-driven Python application created to practise the fundamentals of **Object-Oriented Programming (OOP)**.

The application allows users to create four types of objects and display their details:

- 👤 **Person** — name and age
- 👨‍💼 **Employee** — name, age, employee ID, and salary
- 🧑‍💼 **Manager** — employee details and department
- 👩‍💻 **Developer** — employee details and programming language

The project demonstrates how inheritance can be used to share common properties and methods between classes.

---

## ✨ Features

| Feature | Description |
|---|---|
| 👤 Create Person | Accepts and displays a person's name and age |
| 👨‍💼 Create Employee | Stores name, age, employee ID, and salary |
| 🧑‍💼 Create Manager | Includes the manager's department |
| 👩‍💻 Create Developer | Includes the developer's programming language |
| 📋 Show Details | Displays details for a previously created object |
| 🔗 Class Relationship | Checks inheritance using `issubclass()` |
| 💰 Salary Validation | Rejects negative salary for regular Employee creation |
| 🔁 Interactive Menu | Repeats until the user selects Exit |

--- 
## 🏗️ Class Hierarchy

<div align="center">

```text
             ┌──────────────┐
             │    PERSON    │
             │  Name, Age   │
             └──────┬───────┘
                    │
                    ▼
             ┌──────────────┐
             │   EMPLOYEE   │
             │ ID, Salary   │
             └──────┬───────┘
                    │
              ┌─────┴─────┐
              ▼           ▼
       ┌────────────┐ ┌────────────┐
       │  MANAGER   │ │  DEVELOPER │
       │ Department │ │ Programming│
       │            │ │  Language  │
       └────────────┘ └────────────┘
```

</div>

### 🔗 Inheritance Relationship

- `Employee` inherits from `Person`.
- `Manager` inherits from `Employee`.
- `Developer` inherits from `Employee`.

```text
Person
  └── Employee
       ├── Manager
       └── Developer
```

- `Employee` inherits from `Person`.
- `Manager` inherits from `Employee`.
- `Developer` inherits from `Employee`.

---
## 🔄 Program Flowchart

<div align="center">

```text
          ┌──────────────┐
          │    START     │
          └──────┬───────┘
                 ▼
          ┌──────────────┐
     ┌───►│  MAIN MENU   │◄─────────────────┐
     │    └──────┬───────┘                  │
     │           ▼                          │
     │    ┌──────────────┐                  │
     │    │ Choose Option│                  │
     │    └──────┬───────┘                  │
     │           │                          │
     │    ┌──────┼────────┬────────┐        │
     │    ▼      ▼        ▼        ▼        │
     │ Person Employee Manager Developer    │
     │    │      │        │        │        │
     │    └──────┴────────┴────────┘        │
     │                 │                    │
     │                 ▼                    │
     │          ┌──────────────┐            │
     │          │ Show Details │────────────┘
     │          └──────────────┘
     │
     │     Choose Exit (Option 6)
     │                 │
     │                 ▼
     │          ┌──────────────┐
     └──────────│     EXIT     │
                └──────────────┘
```

</div>

### 📋 Menu Options

| Option | Operation |
|---:|---|
| 1 | Create a Person |
| 2 | Create an Employee |
| 3 | Create a Manager |
| 4 | Create a Developer |
| 5 | Show Details and Class Relationships |
| 6 | Exit |

---

## 🧠 OOP Concepts Used — Explained

This project is designed to practise the main building blocks of **Object-Oriented Programming (OOP)**. OOP organizes code using classes and objects, making programs easier to structure, reuse, and maintain.

### 1. 🧱 Classes and Objects

A **class** is a blueprint that defines the data and behaviour an object can have. An **object** is an instance created from that class.

In this project, `Person`, `Employee`, `Manager`, and `Developer` are classes. For example, when the user enters a person's name and age, the program creates an object:

```python
person = Person(name, age)
```

Here, `person` refers to an object created from the `Person` class.

### 2. 🧬 Inheritance

**Inheritance** allows a child class to reuse attributes and methods from a parent class.

```python
class Employee(Person):
    ...

class Manager(Employee):
    ...

class Developer(Employee):
    ...
```

- `Employee` inherits the `name`, `age`, and methods from `Person`.
- `Manager` inherits employee functionality and adds `department`.
- `Developer` inherits employee functionality and adds `programming_language`.

**Why it is useful:** Shared functionality can be defined once in a parent class instead of being repeated in every class.

### 3. 🔒 Encapsulation

**Encapsulation** groups data and related methods inside a class. In Python, a double underscore prefix triggers name mangling, which helps prevent accidental direct access to attributes.

```python
self.__employee_id = employee_id
self.__salary = salary
```

The `Employee` class uses `__employee_id` and `__salary` as private-style attributes. The class provides getter and setter methods to access or update these values.

**Why it is useful:** It encourages data to be handled through a class's methods instead of being changed without a clear interface.

### 4. 🔁 Polymorphism and Method Overriding

**Polymorphism** means that the same operation can behave differently for different object types. In this project, each employee-related class provides its own version of `display()`.

```python
def display(self):
    print("Employee Details")
```

`Manager` and `Developer` override `display()` to show their own additional fields, such as department or programming language.

**Why it is useful:** The same method name can present class-specific information.

### 5. 🏗️ Constructor: `__init__()`

A **constructor** is the initializer that runs when an object is created. In Python, `__init__()` assigns the starting values of an object's attributes.

```python
def __init__(self, name, age):
    self.name = name
    self.age = age
```

For example, the `Person` constructor stores a person's name and age when `Person(name, age)` is called.

### 6. 🧱 The `super()` Function

`super()` lets a child class call methods from its parent class. Here, it is used to initialize the inherited attributes before adding class-specific attributes.

```python
super().__init__(name, age)
```

For example, `Manager` calls the `Employee` constructor, which in turn calls the `Person` constructor. This avoids rewriting the same initialization logic.

### 7. 🔑 Getters and Setters

**Getters** return attribute values, while **setters** update them.

Examples from the `Employee` class:

```python
def get_salary(self):
    return self.__salary

def set_salary(self, salary):
    self.__salary = salary
```

The getter reads the salary, and the setter changes it. In this current project, the setter does not validate the new salary value.

### 8. 🗑️ Destructor: `__del__()`

The `Employee` class defines `__del__()`:

```python
def __del__(self):
    print("Employee object deleted.")
```

Python may call this method when an object is being finalized. **Its exact timing is not guaranteed**, so it should not be treated as a reliable way to manage important resources.

### 9. 🔗 The `issubclass()` Function

`issubclass()` checks whether one class inherits from another class.

```python
issubclass(Employee, Person)
issubclass(Manager, Employee)
issubclass(Developer, Employee)
```

The program prints `True` for these relationships because each child class inherits from the class checked.

### 📋 OOP Concept Summary

| Concept | Meaning | Project Example |
|---|---|---|
| **Class** | Blueprint for creating objects | `Person`, `Employee` |
| **Object** | Instance of a class | `person = Person(name, age)` |
| **Inheritance** | Reusing a parent class's functionality | `class Employee(Person)` |
| **Encapsulation** | Keeping data and methods together and controlling access through methods | `__salary`, `get_salary()` |
| **Polymorphism** | Same operation can have different behaviours | Different `display()` implementations |
| **Method Overriding** | Child class replaces an inherited method implementation | `Manager.display()` |
| **Constructor** | Initializes an object | `__init__()` |
| **`super()`** | Calls parent-class functionality | `super().__init__(...)` |
| **Getter / Setter** | Reads or updates an attribute through methods | `get_salary()`, `set_salary()` |
| **Destructor** | Finalization hook for an object | `__del__()` |
| **`issubclass()`** | Tests class inheritance | Class relationship checks |

> **Important distinction:** Encapsulation, inheritance, and polymorphism are OOP principles. `__init__()`, `super()`, getters/setters, `__del__()`, and `issubclass()` are Python features or techniques used in this project to implement or demonstrate related behaviour.

---

## 🖥️ Actual Program Output

> **The output below uses the exact names, inputs, values, and text you provided.**

```text
***Employee Management System***

---Choose an operation---: 
1. Create a person
2. Create an Employee
3. Create a manager
4. Create a Developer
5. Show Details
6. Exit

Enter your choice: 1

Enter Name: nipa
Enter Age: 25
Name:  nipa
Age:  25

Person created with name: nipa and age: 25

---Choose an operation---: 
1. Create a person
2. Create an Employee
3. Create a manager
4. Create a Developer
5. Show Details
6. Exit

Enter your choice: 2

Enter Name: khushi
Enter Age: 20
Enter Employee_id: E123
Enter Salary: 200000

Employee created with name: khushi, age: 20, ID: E123, and salary: $ 200000.0.

---Choose an operation---: 
1. Create a person
2. Create an Employee
3. Create a manager
4. Create a Developer
5. Show Details
6. Exit

Enter your choice: 3

Enter Name: dhara
Enter Age:19
Enter Employee ID: E234
Enter Salary: 600000
Enter Department: IT

Manager created with name: dhara, age: 19,  ID: E234, salary: $ 600000.0, and department: IT.

---Choose an operation---: 
1. Create a person
2. Create an Employee
3. Create a manager
4. Create a Developer
5. Show Details
6. Exit

Enter your choice: 4

Enter Name: aary
Enter Age: 21
Enter Employee ID: E345
Enter Salary: 300000
Enter Programming Language: Python

Developer created with name: aary, age: 21, ID: E345, salary: $300000.0, and programming language: Python.

---Choose an operation---: 
1. Create a person
2. Create an Employee
3. Create a manager
4. Create a Developer
5. Show Details
6. Exit

Enter your choice: 5

Choose details to show: 

1. Person
2. Employee
3. Manager
4. Developer

Class Relationship:
Employee is subclass of Person: True
Manager is subclass of Employee: True
Developer is subclass of Employee: True

Enter your choice: 3
Manager Details: 
Name:  dhara
Age:  19
Employee ID:  E234
Salary:  600000.0
Department:  IT

---Choose an operation---: 
1. Create a person
2. Create an Employee
3. Create a manager
4. Create a Developer
5. Show Details
6. Exit

Enter your choice: 6

Exiting the system All resources have been freed.

Goodbye!
```

---

<div align="center">

### 🖼️ Project Output Screenshot
(<img width="437" height="1931" alt="5ss" src="https://github.com/user-attachments/assets/a419714f-69b2-4284-a098-e6163cdbd4cf" />)

</div>

---

## 🎬 Project Demo Video

<div align="center">

### ▶️ Watch the Project Demo

**Video Link:** `ADD_YOUR_PROJECT_VIDEO_LINK_HERE`

</div>

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| 🐍 **Python 3** | Main programming language |
| 🧱 **Object-Oriented Programming** | Organizes the program using classes and inheritance |
| 💻 **Console / Terminal** | Provides menu-based interaction |
| 🐙 **GitHub** | Stores the source code and project documentation |

---
---

## 📁 Project Structure

```text
Employee-Management-System/
│
├── employee_management.py
├── README.md
└── screenshots/
    └── output.png
```

---

## 🚀 Future Improvements

- 🗄️ Add database support using SQLite or MySQL.
- 👥 Manage multiple employees in a collection.
- 🔍 Search employees by name or ID.
- ✏️ Add update and delete functionality.
- 🆔 Validate unique employee IDs.
- 💰 Validate salary for every employee type.
- 📊 Generate employee summaries and reports.
- 🖥️ Create a graphical interface using Tkinter.

---

## 🎯 Learning Outcomes

By building this project, I practised:

- Creating classes and objects in Python.
- Applying inheritance to reuse code.
- Understanding encapsulation with private attributes.
- Overriding methods in child classes.
- Using constructors and `super()`.
- Creating getter and setter methods.
- Checking class relationships with `issubclass()`.
- Building a menu-driven console program.
- Accepting and converting user input.

---

## 📌 Project Information

| Detail | Information |
|---|---|
| **Project Name** | Employee Management System |
| **Programming Language** | Python |
| **Project Type** | OOP Mini Project |
| **Level** | Beginner |
| **Interface** | Console Based |
| **Main Concepts** | Classes, Inheritance, Encapsulation, Method Overriding |

---

<div align="center">

## 👩‍💻 Author

### **DHARA**

*Python • Object-Oriented Programming • Learning by Building*

---

⭐ **If you find this project useful, consider starring the repository!**

**Made with Python 🐍**

</div>
