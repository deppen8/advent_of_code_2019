from typing import List


def calculate_module(mass: int):
    return (mass // 3) - 2


def total_fuel(values_list: List[str]):
    total = 0
    for mass in values_list:
        total += calculate_module(int(mass))
    return total


with open("input.txt", "r") as f:
    print(total_fuel(f.readlines()))

assert calculate_module(12) == 2
assert calculate_module(14) == 2
assert calculate_module(1969) == 654
assert calculate_module(100756) == 33583
