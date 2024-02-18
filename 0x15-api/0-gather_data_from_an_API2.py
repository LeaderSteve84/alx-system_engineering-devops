#!/home/stephen_adah/.pyenv/versions/3.8.12/envs/my_project_env_3.8.12/bin/python3
import requests
import sys

def fetch_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/users"
    todo_url = f"{base_url}/{employee_id}/todos"
    try:
        response = requests.get(todo_url)
        response.raise_for_status()
        todos = response.json()

        user_response = requests.get(f"{base_url}/{employee_id}")
        user = user_response.json()
        employee_name = user.get("name")

        completed_tasks = [task for task in todos if task["completed"]]
        total_tasks = len(todos)

        print(f"Employee {employee_name} is done with tasks ({len(completed_tasks)}/{total_tasks}):")
        print(f"{employee_name}:", len(completed_tasks), total_tasks)
        for task in completed_tasks:
            print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_employee_todo_progress(employee_id)
