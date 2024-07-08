import pandas as pd
import numpy as np
from datetime import datetime

tasks = pd.DataFrame(columns=['Task', 'Deadline', 'Priority', 'Status'])

def add_task():
    global tasks
    task = input("Enter the task: ")
    deadline = input("Enter the deadline (YYYY-MM-DD): ")
    priority = input("Enter the priority (High/Medium/Low): ")
    new_task = pd.DataFrame({'Task': [task], 'Deadline': [deadline], 'Priority': [priority], 'Status': ['Pending']})
    tasks = pd.concat([tasks, new_task], ignore_index=True)
    print("Task added successfully!")

def complete_task():
    global tasks
    task_to_complete = input("Enter the task to mark as complete: ")
    if task_to_complete in tasks['Task'].values:
        tasks.loc[tasks['Task'] == task_to_complete, 'Status'] = 'Completed'
        print("Task marked as completed!")
    else:
        print("Task not found.")

def view_tasks():
    global tasks
    if tasks.empty:
        print("No tasks found.")
    else:
        print("\nAll Tasks:")
        print(tasks.to_string(index=False))

def view_pending_tasks():
    global tasks
    if tasks.empty:
        print("No tasks found.")
    else:
        pending_tasks = tasks[tasks['Status'] == 'Pending']
        if pending_tasks.empty:
            print("No pending tasks.")
        else:
            print("\nPending Tasks:")
            print(pending_tasks.to_string(index=False))

def prioritize_tasks():
    global tasks
    if tasks.empty:
        print("No tasks found.")
    else:
        tasks['Deadline'] = pd.to_datetime(tasks['Deadline'])
        tasks.sort_values(by=['Priority', 'Deadline'], ascending=[True, True], inplace=True)
        print("Tasks prioritized successfully!")

def main_menu():
    while True:
        print("\nTask Manager Menu")
        print("1. Add a task")
        print("2. Complete a task")
        print("3. View all tasks")
        print("4. View pending tasks")
        print("5. Prioritize tasks")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            complete_task()
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            view_pending_tasks()
        elif choice == '5':
            prioritize_tasks()
        elif choice == '6':
            print("Exiting the Task Manager. Stay productive!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
main_menu()
