import random

count = 0

def find_min_max(data, left, right):
    global count

    # Only one element
    if left == right:
        return data[left], data[left]

    # Two elements
    if right == left + 1:
        count += 1
        if data[left] < data[right]:
            return data[left], data[right]
        else:
            return data[right], data[left]

    # Divide
    middle = (left + right) // 2

    min1, max1 = find_min_max(data, left, middle)
    min2, max2 = find_min_max(data, middle + 1, right)

    # Combine
    count += 1
    minimum = min1 if min1 < min2 else min2

    count += 1
    maximum = max1 if max1 > max2 else max2

    return minimum, maximum


def normal_method(data):
    minimum = maximum = data[0]
    comparisons = 0

    for value in data[1:]:
        comparisons += 1
        if value < minimum:
            minimum = value

        comparisons += 1
        if value > maximum:
            maximum = value

    return minimum, maximum, comparisons


# Different Example Array
numbers = [18, 7, 25, 3, 14, 9, 30, 11]

count = 0
mn, mx = find_min_max(numbers, 0, len(numbers) - 1)
dc_comp = count

_, _, naive_comp = normal_method(numbers)

print("Array:", numbers)
print("Minimum:", mn)
print("Maximum:", mx)
print("Divide & Conquer Comparisons:", dc_comp)
print("Naive Comparisons:", naive_comp)

print("\nPerformance Comparison")
print("-" * 40)
print(f"{'Size':<10}{'D&C':<10}{'Naive':<10}{'Formula'}")

for n in [10, 100, 1000, 10000]:
    arr = [random.randint(1, 10000) for _ in range(n)]

    count = 0
    find_min_max(arr, 0, len(arr) - 1)
    dc = count

    _, _, naive = normal_method(arr)

    formula = (3 * n) // 2 - 2

    print(f"{n:<10}{dc:<10}{naive:<10}{formula}")