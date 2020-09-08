"""
Script file: parse.py
Created on: September 8, 2020
Last modified on: September 8, 2020

Comments:
    Main script to analyze the input JSON file and generate two files.
    - watchers.json
    - managers.json
    Each should contain a dictionary with the manager/watcher in the key, and a list of projects in the value.
    The projects in the list should be ordered by priority - from most priority to least priority.
    Remember here that a lower number means a higher priority.
"""

import os
import json


def create_dir(path):
    """
    create new folder
    if the folder is already existing, this means the data is ready
    in this case skip it
    :param path: directory path
    :return: none
    """
    if not os.path.exists(path):
        os.makedirs(path)


def read_raw_data(filename):
    """
    Read raw data from a sample file
    :param filename: path to the sample data file
    :return: output data
    """
    with open(filename) as json_file:
        data = json.load(json_file)
    return data


def save_json(data, filename):
    """
    Write json data to a given file.
    :param data: json data
    :param filename: path to save file
    :return: none
    """
    # check the output path
    dir_path = os.path.dirname(filename)
    create_dir(dir_path)

    # write json to a file
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)


def update_data(output, project, key='managers'):
    """
    Update output dictionary
    :param output: dictionary
    :param project: dictionary
    :param key: key name {'managers', 'watchers'}
    :return: none
    """
    for i, name in enumerate(project[key]):
        temp = {
            'name': project['name'],
            'priority': project['priority']
        }

        # extend data
        if name in output:
            output[name].append(temp)
        else:
            output[name] = [temp]

        # sort data
        output[name] = sorted(output[name], key=lambda k: k['priority'], reverse=False)


def remove_priority(data):
    """
    Remove priority key in the output dictionary
    :param data: dictionary
    :return: none
    """
    for key in data.keys():
        temp = []
        for item in data[key]:
            temp.append(item['name'])
        data[key] = temp


def parse_data(data):
    """
    Parse the json data to get the list of managers, watchers
    Each element is a dictionary format with project names sorted by priority
    :param data: list of dictionaries
    :return: none
    """
    # initialize dictionaries
    watchers = {}
    managers = {}

    # analyze the data, each project is a dictionary
    for project in data:
        update_data(managers, project, 'managers')
        update_data(watchers, project, 'watchers')

    # generate output dictionary
    remove_priority(managers)
    remove_priority(watchers)

    # save data to json files
    save_json(managers, 'result/managers.json')
    save_json(watchers, 'result/watchers.json')


def run(filename='source/sample.json'):
    """
    Main script to run
    :param filename: input JSON filename
    :return: none
    """
    json_data = read_raw_data(filename)
    parse_data(json_data)


if __name__ == '__main__':
    run('source/source_file_2.json')
