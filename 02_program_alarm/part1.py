from typing import List
import csv


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
    return intcode


def test_program():
    assert restore_program([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
    assert restore_program([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
    assert restore_program([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
    assert restore_program([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]


inputs = read_csv_file("input_mod.csv")
print(restore_program(inputs)[0])
