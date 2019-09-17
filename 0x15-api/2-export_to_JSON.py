#!/usr/bin/python3
"""
JSON format
"""
import json
import requests
import sys


if __name__ == "__main__":
    root = "https://jsonplaceholder.typicode.com"
    users = requests.get(root + "/users", params={"id": sys.argv[1]})
    for names in users.json():
        usr_id = names.get('id')
        todo = requests.get(root + "/todos", params={"userId": usr_id})
        csv_arr = []
        for tasks in todo.json():
            csv_arr.append({"task": tasks.get("title"),
                            "completed": str(tasks.get("completed")),
                            "username": names.get("name")})
        with open(sys.argv[1] + ".json", 'a') as f:
            f.write(json.dumps({"2": csv_arr}))
