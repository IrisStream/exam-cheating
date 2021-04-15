import pandas as pd 
import numpy as np 
import json 

with open('Dataset.json') as json_file:
    provinces = json.load(json_file)
data = {}
for province in provinces:
    data[province['province']] = pd.read_csv(province['file'])
    data[province['province']].set_index('SBD')
    data[province['province']]['KHỐI D'] = data[province['province']]['KHỐI D'].replace(['#VALUE!'], '')
    data[province['province']].to_csv(province['file'])