#!/usr/bin/python3
"""
export data in the CSV format..
"""
import csv
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    else:
        user_id = sys.argv[1]
        user_url = 'https://jsonplaceholder.typicode.com/users/' + user_id
        response = requests.get(user_url)
        user_name = response.json().get('username')
        task_url = user_url + '/todos'
        response = requests.get(task_url)
        tasks = response.json()

        dict_data = {user_id: []}
        for task in tasks:
            COMPLETED_TASK_STATUS = task.get('completed')
            TASK_TITLE = task.get('title')
            dict_data[user_id].append({
                "task": TASK_TITLE,
                "completed": COMPLETED_TASK_STATUS,
                "username": user_name})

        with open('{}.json'.format(user_id), 'w') as f:
            json.dump(dict_data, f)
