import re

def add(numbers: str) -> int:
    return 0

def add(numbers: str) -> int:
    if not numbers:
        return 0
    num_list = map(int, numbers.split(","))
    return sum(num_list)

def add(numbers: str) -> int:
    if not numbers:
        return 0

    # Check for custom delimiter
    if numbers.startswith("//"):
        delimiter, numbers = numbers[2:].split("\n", 1)
        numbers = numbers.replace(delimiter, ",")
    else:
        numbers = numbers.replace("\n", ",")

    num_list = map(int, numbers.split(","))
    return sum(num_list)