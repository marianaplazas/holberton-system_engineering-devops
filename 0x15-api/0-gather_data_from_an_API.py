#!/usr/bin/python3
"""
Gets the completed todo list of an employed with the id
"""
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    users = requests.get(url + "/users", params={"id": sys.argv[1]})
    for names in users.json():
        usr_id = names.get('id')
        todo_list = requests.get(url + "/todos", params={"userId": usr_id})
        task_complete = 0
        tasks = []
        for task in todo_list.json():
            if task.get('completed') is True:
                task_complete += 1
                tasks.append(task.get('title'))
        print("Employee {:s} is done with tasks({:d}/{:d}):\n\t {}".
              format(names.get('name'), task_complete,
                     len(todo_list.json()), "\n\t ".join(tasks)))
