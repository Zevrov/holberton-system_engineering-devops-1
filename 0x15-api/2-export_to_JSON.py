#!/usr/bin/python3
"""The API gather data for employee
"""
from json import dump
from requests import get
from sys import argv


def gather_data_json(employee_id):
    """Use REST API, for a given employee ID,
    returns information about his/her TODO list progress
    and saves it into a json format
    Args:
        employee_id: id for each employee
    """
    json = get("https://jsonplaceholder.typicode.com/users/{}"
               .format(employee_id)).json()
    username = json["username"]
    user_infos = []
    for arg in get("https://jsonplaceholder.typicode.com/todos/").json():
        if arg["userId"] == employee_id:
            dict_info = {}
            dict_info["task"] = arg["title"]
            dict_info["completed"] = arg["completed"]
            dict_info["username"] = username
            user_infos.append(dict_info)
    user_dict = {str(employee_id): user_infos}
    with open("{}.json".format(employee_id), 'w') as f:
        dump(user_dict, f)


if __name__ == "__main__":
    gather_data_json(int(argv[1]))
