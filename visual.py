# python file to visualise the data collected

import matplotlib.pyplot as plt
import numpy as np

data_list = []

leeds_temps = []
leeds_humidities = []
leeds_pressures = []
leeds_iaqscores = []
leeds_iaqpercents = []
leeds_eco2 = []

# leeds_locations = []

tod_temps = []
tod_humidities = []
tod_pressures = []
tod_iaqscores = []
tod_iaqpercents = []
tod_eco2 = []
tod_locations = []

with open('DataStorageFileLeeds.csv', 'r') as my_file:
    f_data = my_file.readlines()

    stripped_data = []

    for line in f_data:
        if line[0] != ',':
            stripped_data.append(line.strip().split(','))

    for i in stripped_data:
        leeds_temps.append(float(i[0]))
        leeds_humidities.append(float(i[1]))
        leeds_pressures.append(float(i[2]))
        leeds_iaqscores.append(float(i[3]))
        leeds_iaqpercents.append(float(i[4]))
        leeds_eco2.append(float(i[5]))


with open('DataStorageFileTod.csv', 'r') as my_file:
    f_data = my_file.readlines()

    stripped_data = []

    for line in f_data:
        if line[0] != ',':
            stripped_data.append(line.strip().split(','))

    for i in stripped_data:
        tod_temps.append(float(i[0]))
        tod_humidities.append(float(i[1]))
        tod_pressures.append(float(i[2]))
        tod_iaqscores.append(float(i[3]))
        tod_iaqpercents.append(float(i[4]))
        tod_eco2.append(float(i[5]))
    
    for x in range(0, len(stripped_data), 3):
        tod_locations.append(stripped_data[x])

print(tod_locations)

def find_avgs(my_list):
    averages = []
    for x in range(0, len(my_list), 3):
        total = my_list[x] + my_list[x+1] + my_list[x+2]
        averages.append(float(f'{(total/3):.2f}'))
    return averages

tod_temp_avgs = find_avgs(tod_temps)
leeds_temp_avgs = find_avgs(leeds_temps)

tod_humidity_avgs = find_avgs(tod_humidities)
leeds_humidity_avgs = find_avgs(leeds_humidities)

tod_pressure_avgs = find_avgs(tod_pressures)
leeds_pressure_avgs = find_avgs(leeds_pressures)

tod_iaqscore_avgs = find_avgs(tod_iaqscores)
leeds_iaqscore_avgs = find_avgs(leeds_iaqscores)

tod_iaqpercent_avgs = find_avgs(tod_iaqpercents)
leeds_iaqpercent_avgs = find_avgs(leeds_iaqpercents)

tod_eco2_avgs = find_avgs(tod_eco2)
leeds_eco2_avgs = find_avgs(leeds_eco2)

leeds_locations = ['Bragg Building', 'Student Union', 'Morrisons']

x_axis = np.arange(len(leeds_locations)) 
# numpy arange function makes x axis values depending on num vals on x axis

def leeds_graph_gen(leeds_data, ylabel_name, title):
    x_axis = np.arange(len(leeds_locations))
    inside_data = leeds_data[::2]
    outside_data = leeds_data[1::2]

    plt.bar(x_axis-0.2, inside_data, 0.4, label='Inside')
    plt.bar(x_axis+0.2, outside_data, 0.4, label='Outside')

    plt.xticks(x_axis, leeds_locations)
    plt.xlabel('Locations', weight='bold')
    plt.ylabel(ylabel_name, weight='bold')
    plt.title(title, weight='bold')

    plt.legend()
    plt.show()


eco2_comparison_locations = ['Bragg Building (L)', 'Student Union (L)', 'Morrisons (L)', 'Tod Park Outside (T)', 'Alfie\'s House (T)', 'Outside THS New Block (T)']
eco2_comparison_data = [513, 327, 341, 281, 403, 317]

def eco2_graph_gen(data):

    x_axis = np.arange(len(eco2_comparison_locations))

    plt.barh(x_axis, data, 0.4)

    plt.yticks(x_axis, eco2_comparison_locations)
    plt.ylabel('Locations')
    plt.xlabel('eCO2 Values (ppm)', weight='bold')
    plt.title('eCO2, Tod vs Leeds', weight='bold')

    plt.legend()
    plt.show()

eco2_graph_gen(eco2_comparison_data)

# leeds_graph_gen(leeds_temp_avgs, 'Temperature (Celsius)', 'Temperatures Around Leeds')
# leeds_graph_gen(leeds_pressure_avgs, 'Pressure (Pa)', 'Pressure Around Leeds')
# leeds_graph_gen(leeds_humidity_avgs, 'Humidity (%)', 'Humidity Around Leeds')
# leeds_graph_gen(leeds_iaqscore_avgs, 'IAQ Score', 'IAQ Scores Around Leeds') # note iaqscore this ranges from 0-351

# leeds_graph_gen(leeds_eco2_avgs, 'eCO2 Value', 'eCO2 Values Around Leeds')










'''
print('Leeds')
print(f'Temperatures: {leeds_temps}')
print(f'Humidities: {leeds_humidities}')
print(f'Pressures: {leeds_pressures}')
print(f'IAQ Scores: {leeds_iaqscores}')
print(f'IAQ Percents: {leeds_iaqpercents}')
print(f'eCO2: {leeds_eco2}\n')

print('Tod')
print(f'Temperatures: {tod_temps}')
print(f'Humidities: {tod_humidities}')
print(f'Pressures: {tod_pressures}')
print(f'IAQ Scores: {tod_iaqscores}')
print(f'IAQ Percents: {tod_iaqpercents}')
print(f'eCO2: {tod_eco2}')
'''