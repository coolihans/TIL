
def quick_sort(array):
    N = len(array)
    if N <= 1:
        return array
    mid = N // 2
    lefts = []
    rights = []
    rest = array[:mid] + array[mid+1:]
    for n in rest:
        if array[mid] > n:
            rights.append(n)
        elif array[mid] < n:
            lefts.append(n)

    sorted_left = quick_sort(lefts)
    sorted_right = quick_sort(rights)

    return sorted_left + [array[mid]] + sorted_right


numbers = [6, 2, 3, 4, 5, 1]
print(quick_sort(numbers))
