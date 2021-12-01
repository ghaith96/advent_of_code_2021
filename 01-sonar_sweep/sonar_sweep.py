from typing import List

def window_sum_iterator(list: List[int], window_size: int=3):
    return [sum(list[i:i+window_size]) for i in range(0, len(list) -1)]

def iter_two_items(list: List[int]):
    for i in range(0, len(list)-1):
        yield list[i], list[i+1]

def read_input_as_list_of_numbers(file_name: str = './input.txt') -> List[int]:
    with open(file_name) as file:
        return [int(line.rstrip()) for line in file.readlines()]

def sonar_sweep():
    readings = read_input_as_list_of_numbers()
    depth_measurment_increases_times=sum([1 if j - i > 0 else 0 for i, j in iter_two_items(readings)])
    print(f'the number of times a depth measurement increases: {depth_measurment_increases_times}')

def sonar_sweep_window():
    readings = read_input_as_list_of_numbers()
    depth_measurment_increases_times=sum([1 if j - i > 0 else 0 for i, j in iter_two_items(window_sum_iterator(readings))])
    print(f'the number of times sum of measurments increases in window of 3: {depth_measurment_increases_times}')

if __name__ == '__main__':
    sonar_sweep()
    sonar_sweep_window()