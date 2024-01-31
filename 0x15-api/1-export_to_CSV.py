#!/usr/bin/python3
"""
export data in the CSV format..
"""
import csv
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    else:
        user = sys.argv[1]
        user_url = 'https://jsonplaceholder.typicode.com/users/' + user
        response = requests.get(user_url)
        user_name = response.json().get('username')
        task = user_url + '/todos'
        response = requests.get(task)
        tasks = response.json()

        with open('{}.csv'.format(user), 'w') as csvfile:
            for task in tasks:
                completed = task.get('completed')
                task_title = task.get('title')
                csvfile.write('"{}","{}","{}","{}"\n'.format(
                    user, user_name, completed, task_title))
