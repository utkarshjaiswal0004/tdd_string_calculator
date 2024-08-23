def add(numbers: str) -> int:
    return 0

def add(numbers: str) -> int:
    if not numbers:
        return 0
    num_list = map(int, numbers.split(","))
    return sum(num_list)