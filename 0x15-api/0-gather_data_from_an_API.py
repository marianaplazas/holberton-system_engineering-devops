#!/usr/bin/python3
"""
Gets the completed todo list of an employeed with the id
"""
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    users = requests.get(url + "/users", params={"id": sys.argv[1]}).json()
    for names in users:
        user_id = names.get('id')
        todo_list = requests.get(root + "/todos", params={"userId": user_id}).json()
        task_complete = 0
        tasks= []
        for task in todo_list():
            if tasks.get('completed') is True:
                task_complete += 1
                tasks_array.append(tasks.get('title'))
        print("Employee {:s} is done with tasks({:d}/{:d}):\n\t {}".
              format(names.get('name'), task_complete,
                     len(todo_list), "\n\t ".join(tasks)))
