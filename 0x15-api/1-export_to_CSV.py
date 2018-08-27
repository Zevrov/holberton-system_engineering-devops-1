#!/usr/bin/python3
"""The API gather data for employee
"""
from csv import DictWriter
from requests import get
from sys import argv


def gather_data_csv(employee_id):
    """Use REST API, for a given employee ID,
    returns information about his/her TODO list progress
    and saves it into a csv format
    Args:
        employee_id: id for each employee
    """
    json = get("https://jsonplaceholder.typicode.com/users/{}"
               .format(employee_id)).json()
    name = json["username"]
    fieldname = ["userId", "username", "completed", "title"]
    with open("{}.csv".format(employee_id), 'w') as f:
        writer = DictWriter(f, fieldnames=fieldname)
        writer.writeheader()
        for arg in get("https://jsonplaceholder.typicode.com/todos/").json():
            if arg["userId"] == employee_id:
                del arg["id"]
                arg["username"] = name
                writer.writerow(arg)


if __name__ == "__main__":
    gather_data_csv(int(argv[1]))
