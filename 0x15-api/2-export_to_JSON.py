#!/usr/bin/python3
"""
convert to JSON format
"""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    users = requests.get(url + "/users", params={"id": sys.argv[1]})
    for names in users.json():
        usr_id = names.get('id')
        todo_list = requests.get(url + "/todos", params={"userId": usr_id})
        csv_arr = []
        for tasks in todo_list.json():
            csv_arr.append({"task": tasks.get("title"),
                            "completed": str(tasks.get("completed")),
                            "username": names.get("name")})
        with open(sys.argv[1] + ".json", 'a') as f:
            f.write(json.dumps({"2": csv_arr}))
