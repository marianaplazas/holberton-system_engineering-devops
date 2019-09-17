#!/usr/bin/python3
"""
python script to export to csv
"""
import csv
import requests
import sys


if __name__ == "__main__":
    usr_id = sys.argv[1]
    todo_list = requests.get(
        "https://jsonplaceholder.typicode.com/todos").json()
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(
        usr_id)).json()
    username = user.get("username")
    with open('{}.csv'.format(usr_id), 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='"', quoting=csv.QUOTE_ALL)
        for task in todo_list:
            if task.get("userId") == int(usr_id):
                spamwriter.writerow([usr_id, username, task.get("completed"),
                                     task.get("title")])
