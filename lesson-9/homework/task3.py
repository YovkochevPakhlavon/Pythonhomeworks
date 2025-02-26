import json
import csv

# 1. Create a JSON file named `tasks.json` with the following structure:
data =    [
       {"id": 1, "task": "Do laundry", "completed": False, "priority": 3},
       {"id": 2, "task": "Buy groceries", "completed": True, "priority": 2},
       {"id": 3, "task": "Finish homework", "completed": False, "priority": 1}
]
with open('tasks.json','w') as file:
    json.dump(data, file, indent=4)  # Write JSON with indentation

# Load the tasks from `tasks.json`:
def load_tasks():
    with open('tasks.json','r') as file:
        data = json.load(file)
        return data
def display_tasks():
        data = load_tasks()
        for i in range(len(data)):            
            print(f"ID: {data[i]['id']}")
            print(f"Task Name: {data[i]['task']}")
            print(f"Completed Status: {data[i]['completed']}")
            print(f"Priority: {data[i]['priority']}")
            print("-----------------")
     
def save_changes():
    new_data = [
        {"id": 1, "task": "Do laundry", "completed": False, "priority": 3},
       {"id": 2, "task": "Buy groceries", "completed": True, "priority": 2},
       {"id": 3, "task": "Finish homework", "completed": True, "priority": 1}
          ] # Modified task data
    with open('tasks.json','w') as file:
        json.dump(new_data, file, indent=4)  # Write JSON with indentation

def stats():
     data = load_tasks()
     number_of_tasks = len(data)
     completed_tasks = 0
     pending_tasks = 0
     for i in range(len(data)):
        if data[i]['completed']:
            completed_tasks += 1
        else:
            pending_tasks += 1
     total_priority = 0
     for i in range(len(data)):
         total_priority += int(data[i]["priority"])
    
     average_priority = total_priority / number_of_tasks
     print("Stats about data:")
     print(f"Number of Tasks: {number_of_tasks}")
     print(f"Number of Completed Tasks: {completed_tasks}")
     print(f"Number of Pending Tasks: {pending_tasks}")
     print(f"Average priority: {average_priority}")

def convert_json_csv():
    data = load_tasks()
    with open('tasks.csv','w') as file:
        fieldnames = ['id', 'task', 'completed','priority']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

save_changes()
display_tasks()
stats()
convert_json_csv()