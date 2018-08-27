#!/usr/bin/python3
"""The API gather data for employee
"""
from requests import get
from sys import argv


def gather_data(employee_id):
    """Use REST API, for a given employee ID,
    returns information about his/her TODO list progress
    Args:
        employee_id: id for each employee
    Return:
        returns information about employee todo list
    """
    json = get("https://jsonplaceholder.typicode.com/users/{}"
               .format(employee_id)).json()
    name = json["name"]
    total_task = 0
    completed = 0
    tasks = []
    for arg in get("https://jsonplaceholder.typicode.com/todos/").json():
        if arg["userId"] == employee_id:
            total_task += 1
            if arg["completed"]:
                completed += 1
                tasks.append(arg["title"])
    print("Employee {} is done with tasks({}/{}):".format(name, total_task,
                                                          completed))
    for task in tasks:
        print("\t {}".format(task))


if __name__ == "__main__":
    gather_data(int(argv[1]))
