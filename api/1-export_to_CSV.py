#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee """
import csv
import json
import requests
import sys


if __name__ == "__main__":
    def export_employee_todo_csv(employee_id):
    """Make a GET request to the API endpoint"""
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')

    if response.status_code == 200:
        todos = response.json()

 
        task_data = []
        for task in todos:
            task_data.append([
                task['userId'],
                task['username'],
                str(task['completed']),
                task['title']
            ])

        
        file_name = f"{employee_id}.csv"

       
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            writer.writerows(task_data)

        print(f"TODO list exported to {file_name} successfully.")

    else:
        print(f"Failed to retrieve TODO list for employee {employee_id}.")


employee_id = int(input("Enter the employee ID: "))
export_employee_todo_csv(employee_id)
