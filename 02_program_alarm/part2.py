from typing import List
import csv
import itertools


def read_csv_file(filename: str) -> List[int]:
    with open(filename, "r") as f:
        str_lst = list(csv.reader(f))[0]
        return [int(code) for code in str_lst]


def restore_program(input_array: List[int]) -> List[int]:
    intcode = input_array.copy()
    i = 0
    while intcode[i] != 99:
        if intcode[i] == 1:
            val1 = intcode[intcode[i + 1]]
            val2 = intcode[intcode[i + 2]]
            intcode[intcode[i + 3]] = val1 + val2
            i += 4
        elif intcode[i] == 2:
            val1 = intcode[intcode[i + 1]]
            val2 = intcode[intcode[i + 2]]
            intcode[intcode[i + 3]] = val1 * val2
            i += 4
    return intcode[0]


def replace_values(input_array, idx1val, idx2val):
    input_array[1] = idx1val
    input_array[2] = idx2val
    return input_array


inputs = read_csv_file("input.csv")
combos = list(itertools.combinations_with_replacement(range(100), r=2))
for pair in combos:
    new_array = replace_values(inputs, pair[0], pair[1])
    if restore_program(new_array) == 19690720:
        print(100 * pair[0] + pair[1])
