#!/usr/bin/python3
"""
python script to export to csv
"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        user = argv[1]
        api_url = "https://jsonplaceholder.typicode.com/"
        req_user = requests.get("{}users/{}".format(api_url, user))
        username = req_user.json().get("username")
        all_tasks = requests.get(
            "{}todos?userId={}".format(
                api_url, user)).json()
        with open("{}.csv".format(user), "w") as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for task in all_tasks:
                writer.writerow(
                    (task.get("userId"),
                     username,
                     task.get("completed"),
                        task.get("title")))
