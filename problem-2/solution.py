def product_array(numbers):
    total_product = 1
    for number in numbers:
        total_product = total_product * number
    return [total_product/number for number in numbers]
    