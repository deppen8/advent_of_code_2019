from typing import List


def calculate_module(mass: int):
    total = 0
    value = (mass // 3) - 2
    while value >= 0:
        total += value
        value = (value // 3) - 2
    return total


def total_fuel(values_list: List[str]):
    total = 0
    for mass in values_list:
        total += calculate_module(int(mass))
    return total


def test_calculate_module():
    assert calculate_module(1969) == 966
    assert calculate_module(14) == 2
    assert calculate_module(100756) == 50346


with open("input.txt", "r") as f:
    print(total_fuel(f.readlines()))
