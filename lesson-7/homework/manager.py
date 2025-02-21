class Employee:
    def __init__(self,ID,name,position,salary):
        self.ID = ID
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.ID}, {self.name}, {self.position}, {self.salary}"

class EmployeeManager:
    file_name = "employees.txt"
    def add_employee(self, employee: Employee):
        with open(self.file_name, "a") as file:
            file.write(f"{employee.ID}, {employee.name}, {employee.position}, {employee.salary}\n")
        print(f"Employee {employee.ID} added successfully!")
    def search_employee(self, emp_id):
        with open(self.file_name, "r") as file:
            found = False
            for line in file:
                ID, name, position, salary = line.strip().split(", ")
                if ID == emp_id:
                    print(Employee(ID, name, position, salary))
                    found = True
                    break
        if found == False:
            print("There is no such employee with the given ID!")       
            
    def view_all_employees(self):
        print("Employee records: ")
        with open(self.file_name, "r") as file:
            for line in file:
                    print(line.strip())
    def update_info(self, emp_id):
        employees = []  # Temporary list to store updated records
        found = False   # Flag to check if employee is found

        with open(self.file_name, "r") as file:
            for line in file:
                ID, name, position, salary = line.strip().split(", ")
                if ID == emp_id:
                # Employee found, ask for new details
                    new_name = input("Enter new name: ")
                    new_position = input("Enter new position: ")
                    new_salary = input("Enter new salary: ")
                    employees.append(f"{ID}, {new_name}, {new_position}, {new_salary}\n")
                    found = True
                else:
                    employees.append(line)  # Keep unchanged lines

        if not found:
            return "Employee not found!"

        # Rewrite the file with updated data
        with open(self.file_name, "w") as file:
            file.writelines(employees)

        return f"Employee {emp_id} updated successfully!"
    def delete_employee(self, emp_id):
        employees = []  # Temporary list to store remaining records
        found = False   # Flag to check if employee is found

        with open(self.file_name, "r") as file:
            for line in file:
                ID, name, position, salary = line.strip().split(", ")
                if ID == emp_id:
                    found = True  # Skip this line (delete employee)
                else:
                    employees.append(line)  # Keep all other records

        if not found:
            return "Employee not found!"

        # Rewrite the file without the deleted employee
        with open(self.file_name, "w") as file:
            file.writelines(employees)

        return f"Employee {emp_id} deleted successfully!"

print("Welcome to the Employee Records Manager!")
print('1. Add new employee record')
print('2. View all employee records')
print("3. Search for an employee by Employee ID")
print("4. Update an employee's information")
print("5. Delete an employee record")
print("6. Exit")

option = 1
result = EmployeeManager()
while option != 6:
    option=int(input("Choose the option by writing the corresponding number(1-6) for options:"))
    if option == 1:
        ID = input("Enter ID: ")
        name = input("Enter name: ")
        position = input("Enter position: ")
        salary = input("Enter salary: ")  
        new_employee = Employee(ID,name,position,salary)
        result.add_employee(new_employee)
    elif option == 2:
        result.view_all_employees()
    elif option == 3:
        emp_id = input("Enter Employee ID: ")
        result.search_employee(emp_id)
    elif option == 4:
        emp_id = input("Enter Employee ID: ")
        print(result.update_info(emp_id))
    elif option == 5:
        emp_id = input("Enter Employee ID: ")
        print(result.delete_employee(emp_id))
    elif option == 6:
        print("Thank you! Bye!")
        break
    else:
        print("You gave wrong symbol! Please enter correct options(1-6)")           







