def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    pivot = numbers[0]
    left, right = [], []
    center = [pivot]

    for number in numbers[1:]:
        if number < pivot:
            left.append(number)
        elif number > pivot:
            right.append(number)
        else:
            center.append(number)

    return quick_sort(left) + center + quick_sort(right)


numbers = [7, 5, 4, 1, 2, 10, 3, 7, 6, 9, 8]

print(quick_sort(numbers))
