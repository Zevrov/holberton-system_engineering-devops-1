#!/usr/bin/python3
"""The API gather data for employee
"""
from json import dump
from requests import get


def gather_all_data_json():
    """Use REST API and returns information about his/her
    TODO list progress and saves it into a json format
    """
    user_dict = {}
    for i in range(1, 11):
        json = get("https://jsonplaceholder.typicode.com/users/{}"
                   .format(i)).json()
        username = json["username"]
        user_infos = []
        for arg in get("https://jsonplaceholder.typicode.com/todos/").json():
            if arg["userId"] == i:
                dict_info = {}
                dict_info["username"] = username
                dict_info["task"] = arg["title"]
                dict_info["completed"] = arg["completed"]
                user_infos.append(dict_info)
        user_dict[str(i)] = user_infos
    with open("todo_all_employees.json", 'w') as f:
        dump(user_dict, f)


if __name__ == "__main__":
    gather_all_data_json()
