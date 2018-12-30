def find_pair(numbers, k):
    index_list = [False] * k
    if len(numbers) < 2:
        return False

    for number in numbers:
        if k - number - 1 == 0:
            continue

        if index_list[k - number - 1]:
            return True
        
        index_list[ number - 1] = True
    return False
