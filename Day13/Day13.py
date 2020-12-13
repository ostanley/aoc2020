import math
import numpy as np

def part1(file):
    with open(file, 'r') as f:
        target_time = int(f.readline().strip())
        bus_list = [int(n.strip()) for n in f.readline().split(',') if n != 'x']

    delay = max(bus_list)+1
    min_bus = 0
    for bus in bus_list:
        if math.ceil(target_time/bus)*bus-target_time < delay:
            delay = math.ceil(target_time/bus)*bus-target_time
            min_bus = bus

    print(f'The fastest bus is: {min_bus} with {delay} and their product is {min_bus*delay}')


def search_for_time(buses_to_time, sorted_bus_list):
    solved = False
    for i in range(100*sorted_bus_list[0]):
        arr_time = []
        for b in sorted_bus_list:
            if b == sorted_bus_list[0] and len(sorted_bus_list)==2:
                buses_to_time[b][1] += 1
            elif b == sorted_bus_list[0]:
                buses_to_time[b][1] += np.prod(sorted_bus_list[1:-1])
            else:
                buses_to_time[b][1] = math.floor((buses_to_time[sorted_bus_list[0]][1]*sorted_bus_list[0] -
                                                  buses_to_time[sorted_bus_list[0]][0] + buses_to_time[b][0])/b)
            arr_time.append(buses_to_time[b][1]*b - buses_to_time[b][0])
        if len(set(arr_time)) == 1:
            solved = True
            break
    return buses_to_time, solved, arr_time

def part2(file):
    with open(file, 'r') as f:
        f.readline()
        bus_list = [n.strip() for n in f.readline().split(',')]

    buses_to_time = {}
    max_bus = 0
    for bus in bus_list:
        if bus != 'x':
            buses_to_time[int(bus)] = [bus_list.index(bus), 0]
            if max_bus < int(bus):
                max_bus = int(bus)

    sorted_bus_list = list(buses_to_time.keys())
    sorted_bus_list.sort()
    sorted_bus_list.reverse()

    for buses in range(len(sorted_bus_list)+1):
        if len(sorted_bus_list[:buses]) >= 2:
            small_bus_list = {k:v for k,v in buses_to_time.items() if k in sorted_bus_list[:buses]}
            small_bus_list, success, arr_time = search_for_time(small_bus_list, sorted_bus_list[:buses])
            if not success:
                print(f'Level {buses} did not converge')
                break
            for k,v in buses_to_time.items():
                if k in small_bus_list.keys():
                    buses_to_time[k]=small_bus_list[k]
    print(f'Convergence at {arr_time[0]}')


if __name__ == "__main__":
    file = 'Day13input.txt'
    part1(file)
    part2(file)
