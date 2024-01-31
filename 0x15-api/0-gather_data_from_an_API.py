#!/usr/bin/python3
"""
using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import re
import requests
import sys

URL = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    else:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            response = requests.get('{}/users/{}'.format(URL, id)).json()
            task_response = requests.get('{}/todos'.format(URL)).json()
            name_employee = response.get('name')
            tasks = list(filter(lambda x: x.get('userId') == id, task_response))
            completed_tasks = list(filter(lambda x: x.get('completed'), tasks))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    name_employee,
                    len(completed_tasks),
                    len(tasks)
                )
            )
            if len(completed_tasks) > 0:
                for task in completed_tasks:
                    print('\t {}'.format(task.get('title')))
