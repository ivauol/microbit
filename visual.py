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

tod_temps = []
tod_humidities = []
tod_pressures = []
tod_iaqscores = []
tod_iaqpercents = []
tod_eco2 = []

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

def find_avgs(my_list):
    averages = []
    for x in range(0, len(my_list), 3):
        total = my_list[x] + my_list[x+1] + my_list[x+2]
        averages.append(float(f'{(total/3):.2f}'))
    return averages

tod_temp_avgs = find_avgs(tod_temps)
leeds_temp_avgs = find_avgs(leeds_temps)

print(leeds_temp_avgs)

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

l_temp_in = [leeds_temp_avgs[0], leeds_temp_avgs[2], leeds_temp_avgs[4]]
l_temp_out = [leeds_temp_avgs[1], leeds_temp_avgs[3], leeds_temp_avgs[5]]

l_pres_in = [leeds_pressure_avgs[0], leeds_pressure_avgs[2], leeds_pressure_avgs[4]]
l_pres_out = [leeds_pressure_avgs[1], leeds_pressure_avgs[3], leeds_pressure_avgs[5]]

x_axis = np.arange(len(leeds_locations)) 
# numpy arange function makes x axis values depending on num vals on x axis

def leeds_graph_gen(leeds_data, ylabel_name, title):
    x_axis = np.arange(len(leeds_locations))
    inside_data = leeds_data[::2]
    print(inside_data)
    outside_data = leeds_data[1::2]

    plt.bar(x_axis-0.2, inside_data, 0.4, label='Inside')
    plt.bar(x_axis+0.2, outside_data, 0.4, label='Outside')

    plt.xticks(x_axis, leeds_locations)
    plt.xlabel('Locations', weight='bold')
    plt.ylabel(f'{ylabel_name}', weight='bold')
    plt.title(f'{title}', weight='bold')

    plt.legend()
    plt.show()


leeds_graph_gen(leeds_temp_avgs, 'Temperature (Celsius)', 'Temperatures Around Leeds')

# plt.bar(x_axis-0.2, l_temp_in, 0.4, label='Inside')
# plt.bar(x_axis+0.2, l_temp_out, 0.4, label='Outside')

'''
plt.xticks(x_axis, leeds_locations)
plt.xlabel('Locations')
plt.ylabel('Temperature (Celsius)')
plt.title('Temperatures Around Leeds')
plt.legend()
plt.show()
'''
















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