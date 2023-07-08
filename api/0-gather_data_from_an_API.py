
#!/usr/bin/python3
# Module to gather data from an API

"""Module to gather data from an API"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        user_id = sys.argv[1]
        url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)

        response = requests.get(url)
        if response.status_code == 200:
            user = response.json()
            todos_response = requests.get('{}/todos'.format(url))
            if todos_response.status_code == 200:
                todos = todos_response.json()
                done_tasks = [task for task in todos if task.get('completed') is True]
                total_tasks = len(todos)
                print("Employee {} is done with tasks({}/{}):"
                      .format(user.get('name'), len(done_tasks), total_tasks))
                for task in done_tasks:
                    print("\t {}".format(task.get('title')))
        else:
            print("User not found.")
    else:
        print("Usage: ./0-gather_data_from_an_API.py <employee ID>")
