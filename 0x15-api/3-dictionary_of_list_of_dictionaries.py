#!/usr/bin/python3
"""
export data in the JSON format.
"""
import json
import requests
import sys


if __name__ == "__main__":
    URL = 'https://jsonplaceholder.typicode.com/users'

    response = requests.get(URL)
    users = response.json()

    users_dict = {}
    for user in users:
        user_id = user.get('id')
        user_name = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        url = url + '/todos/'
        response = requests.get(url)

        tasks = response.json()
        users_dict[user_id] = []
        for task in tasks:
            COMPLETED_TASK_STATUS = task.get('completed')
            TASK_TITLE =task.get('title')
            users_dict[user_id].append({
                "task": TASK_TITLE,
                "completed": COMPLETED_TASK_STATUS,
                "username": user_name
            })
    with open('todo_all_employees.json', 'w') as f:
            json.dump(users_dict, f)
