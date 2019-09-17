#!/usr/bin/python3
"""
 create a dictionary of dictionaries
"""
import json
import requests
import sys


if __name__ == "__main__":
    req = requests.get("https://jsonplaceholder.typicode.com/todos")
    data = req.json()

    req2 = requests.get("https://jsonplaceholder.typicode.com/users")
    users = req2.json()
    json_data = {}
    task_value = {}
    for user in users:
        json_data[user.get("id")] = []

    with open('todo_all_employees.json', 'w') as outfile:
        for task in data:
            req3 = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                                .format(task.get("userId")))
            specific_user = req3.json()
            username = specific_user.get("username")
            task_value["username"] = username
            task_value["task"] = task.get("title")
            task_value["completed"] = task.get("completed")
            value = json_data.get(task.get("userId"))
            value.append(task_value)
            task_value = {}
        json.dump(json_data, outfile)
