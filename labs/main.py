def list_average(numbers):
    # TODO: use a for loop to calculate the average of `numbers`, rounded to 2 decimal places
    total = 0
    count = 0
    if not numbers:
        return 0
    for number in numbers:
        total += number
        count += 1

    return round (total / count, 2)