from collections import Counter


INPUT_RANGE = range(388888, 800000)


def has_zero_one_two(num: str):
    if any(digit in num for digit in ["0", "1", "2"]):
        return True
    return False


def has_consecutive_numbers_and_increases(num: str):
    for i in range(5):
        if num[i] > num[i + 1]:
            return False
    if any(num[i] == num[i + 1] for i in range(5)):
        return True


possibilities = []
for n in INPUT_RANGE:
    s = str(n)
    if not has_zero_one_two(s) and has_consecutive_numbers_and_increases(s):
        possibilities.append(int(s))

# print(len(possibilities))

new_possibilities = []
for value in possibilities:
    s = str(value)
    if 2 in Counter(s).values():
        new_possibilities.append(s)

print(len(new_possibilities))
