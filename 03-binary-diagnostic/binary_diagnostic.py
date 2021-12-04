from operator import le, ge


def read_input_file(file_name='./input.txt'):
    with open(file_name) as file:
        return [line.rstrip() for line in file.readlines()]


def get_index_char_freq(readings):
    freq = {}
    for reading in readings:
        chars = list(reading)
        for i, char in enumerate(chars):
            if i in freq:
                if char in freq[i]:
                    freq[i][char] += 1
                else:
                    freq[i][char] = 1
            else:
                freq[i] = {}
                freq[i][char] = 1
    return freq


def get_each_index_freq_char(freq, comparer):
    max_decoded = []
    is_lt = comparer(1, 2)
    for char_freqs in freq.values():
        max_freq = float('inf') if is_lt else float('-inf')
        max_freq_key = ''
        for key, value in char_freqs.items():
            if comparer(value, max_freq):
                max_freq = value
                max_freq_key = key
        max_decoded.append(max_freq_key)
    return max_decoded


def get_oxygen_generator_ratings(readings):
    filtered_readings = readings.copy()
    index_max_freq_char = get_each_index_freq_char(
        get_index_char_freq(filtered_readings), ge)
    index = 0
    while len(filtered_readings) > 1:
        filtered_readings = [
            reading for reading in filtered_readings if reading[index] == index_max_freq_char[index]]
        index_max_freq_char = get_each_index_freq_char(
            get_index_char_freq(filtered_readings), ge)
        index += 1
    return filtered_readings[0]


def get_co2_scrubber_rating(readings):
    filtered_readings = readings.copy()
    index_min_freq_char = get_each_index_freq_char(
        get_index_char_freq(filtered_readings), le)
    index = 0
    while len(filtered_readings) > 1:
        filtered_readings = [
            reading for reading in filtered_readings if reading[index] == index_min_freq_char[index]]
        index_min_freq_char = get_each_index_freq_char(
            get_index_char_freq(filtered_readings), le)
        index += 1
    return filtered_readings[0]


def binary_diagnostic():
    readings = read_input_file()
    freq = get_index_char_freq(readings)
    gamma_rate = int(''.join(get_each_index_freq_char(freq, ge)), 2)
    epsilon_rate = int(''.join(get_each_index_freq_char(freq, le)), 2)
    power_consumption = gamma_rate * epsilon_rate
    oxygen_generator_ratings = int(get_oxygen_generator_ratings(readings), 2)
    co2_scrubber_rating = int(get_co2_scrubber_rating(readings), 2)
    life_support_rating = oxygen_generator_ratings * co2_scrubber_rating
    return (gamma_rate, epsilon_rate, power_consumption, oxygen_generator_ratings, co2_scrubber_rating, life_support_rating)


if __name__ == "__main__":
    binary_diagnostic()
    (gamme_rate, epsilon_rate, power_consumption, oxygen_generator_ratings,
     co2_scrubber_rating, life_support_rating) = binary_diagnostic()
    print(
        f'gamme rate: {gamme_rate}, epsilon rate: {epsilon_rate}, power consumption: {power_consumption}')
    print(
        f'oxygen generator ratings: {oxygen_generator_ratings}, co2 scrubber rating: {co2_scrubber_rating}, life support rating: {life_support_rating}')
