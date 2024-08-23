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

    if numbers.startswith("//"):
        delimiter, numbers = numbers[2:].split("\n", 1)
        numbers = numbers.replace(delimiter, ",")
    else:
        numbers = numbers.replace("\n", ",")

    num_list = list(map(int, numbers.split(",")))

    # Check for negative numbers
    negatives = [num for num in num_list if num < 0]
    if negatives:
        raise ValueError(f"negative numbers not allowed: {', '.join(map(str, negatives))}")

    return sum(num_list)