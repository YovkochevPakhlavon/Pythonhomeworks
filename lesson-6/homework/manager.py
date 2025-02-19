print('1. Add new employee record')
print('2. View all employee records')
print("3. Search for an employee by Employee ID")
print("4. Update an employee's information")
print("5. Delete an employee record")
print("6. Exit")

option=int(input("Choose the option by writing the corresponding number(1-6) for options:"))

if option == 1: #1. Add new employee record
    ID_employee=input("Employee ID: ")
    name=input("Name: ")
    position=input("Position: ")
    salary=input("Salary: ")

    file = open('employees.txt',mode='a')
    file.write(f"{ID_employee}, ")
    file.write(f"{name}, ")
    file.write(f"{position}, ")
    file.write(f"{salary}\n")
    file.close()

elif option == 2: #2. View all employee records
    file = open('employees.txt',mode='r')
    print(file.read())
    file.close()

elif option == 3: #3. Search for an employee by Employee ID
    choosen_ID=input("Please enter Employee ID: ")
    file = open('employees.txt',mode='r')
    lines = file.readlines()
    file.close()
    data=[]
    for line in lines:
        if line != '\n':
            data.append(tuple(line.strip().split(', ')))
    for i in range(len(data)):
        if choosen_ID == data[i][0]:
            print('---------------------')
            print(f"Employee ID: {data[i][0]}")
            print(f"Name: {data[i][1]}")
            print(f"Position: {data[i][2]}")
            print(f"Salary: {data[i][3]}")
            break
    else:
        print("There is no one with the given Employee ID")

elif option == 4: #4. Update an employee's information
    choosen_ID=input("Enter Employee ID you want to update: ")
    update_ID=input("Enter the updated ID: ")
    update_name=input("Enter the updated name: ")
    update_position=input("Enter the updated position: ")
    update_salary=input("Enter the updated salary: ")
    
    file = open('employees.txt',mode='r')
    lines = file.readlines()
    file.close()
    updated_lines = []
    found =False
    for line in lines:
        data = line.strip().split(', ')
        if data[0] == choosen_ID:
            updated_line = f"{update_ID}, {update_name}, {update_position}, {update_salary}\n"
            updated_lines.append(updated_line)
            found = True
        else:
            updated_lines.append(line)
        
    if found:
        file=open('employees.txt','w')
        file.writelines(updated_lines)
        file.close()
        print("Employee details updated successfully!")
    else:
        print("Employee not found.")

elif option == 5: #5. Delete an employee record
    choosen_ID=input("Enter Employee ID you want to delete: ")
    file = open('employees.txt',mode='r')
    lines = file.readlines()
    file.close()
    updated_lines = []
    found =False
    for line in lines:
        data = line.strip().split(', ')
        if data[0] == choosen_ID:
            found = True
        else:
            updated_lines.append(line)
    
    if found:
        file=open('employees.txt','w')
        file.writelines(updated_lines)
        file.close()
        print("Employee details deleted successfully!")
    else:
        print("Employee not found.")

elif option == 6: #6. Exit"
    print("Thank you for using our program!")

else:
    print("There is no option for your request.")




