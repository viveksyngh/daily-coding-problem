def find_pair(numbers, k):
    number_map = {}
    if len(numbers) < 2:
        return False

    for number in numbers:
        if k - number - 1 == 0:
            continue

        if number_map.get(k - number, False):
            return True
        
        number_map[number] = True
    return False
