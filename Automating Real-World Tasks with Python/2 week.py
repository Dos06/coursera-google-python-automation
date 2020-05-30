#! /usr/bin/env python3
import os
import json
import requests

address = '34.72.152.50'
folder = '/data/feedback/'
url = 'http://' + address + '/feedback/'

for files in os.listdir(folder):
    files_path = folder + files
    dictionary = {}
    keys = ['title', 'name', 'date', 'feedback']
    with open(files_path) as txtfile:
        x = 0
        for line in txtfile:
            dictionary[keys[x]] = line.rstrip('\n')
            x += 1
        response = requests.post(url, json=dictionary)
        print(response.status_code)
