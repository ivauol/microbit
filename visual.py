# python file to visualise the data collected

import matplotlib as plt
import numpy as np

data_list = []

# temp.csv currently holds older data from a previous task to be able to test code

with open('temp.csv', 'r') as my_file:
    f_data = my_file.readlines()
    for line in my_file:
        data_list.append(f_data.readline)

    # print(f_data)    

    stripped_data = []

    for line in f_data:
        if line[0] != ',':
            stripped_data.append(line.strip().split(','))

    # print(stripped_data)

