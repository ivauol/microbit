# python file to visualise the data collected

import matplotlib as plt
import numpy as np

data_list = []

temps = []
humidities = []
pressures = []
iaqscores = []
iaqpercents = []
eco2 = []

with open('sample.csv', 'r') as my_file:
    f_data = my_file.readlines()

    stripped_data = []

    for line in f_data:
        if line[0] != ',':
            stripped_data.append(line.strip().split(','))

    print(stripped_data)

    for i in stripped_data:
        temps.append(i[0])
        humidities.append(i[1])
        pressures.append(i[2])
        iaqscores.append(i[3])
        iaqpercents.append(i[4])
        eco2.append(i[5])

print(temps)
print(humidities)
print(pressures)
print(iaqscores)
print(iaqpercents)
print(eco2)


