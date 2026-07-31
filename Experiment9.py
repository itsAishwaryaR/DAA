# Bin Packing Approximation Algorithms

def first_fit(items, capacity=1.0):
    free_space = []
    bins = []

    for value in items:
        allocated = False

        for i in range(len(free_space)):
            if free_space[i] >= value:
                bins[i].append(value)
                free_space[i] -= value
                allocated = True
                break

        if not allocated:
            bins.append([value])
            free_space.append(capacity - value)

    return bins


def first_fit_decreasing(items, capacity=1.0):
    sorted_items = sorted(items, reverse=True)
    return first_fit(sorted_items, capacity)


def best_fit_decreasing(items, capacity=1.0):
    sorted_items = sorted(items, reverse=True)

    bins = []
    free_space = []

    for value in sorted_items:
        best_bin = -1
        least_space = float("inf")

        for i in range(len(free_space)):
            remaining = free_space[i] - value

            if remaining >= 0 and remaining < least_space:
                least_space = remaining
                best_bin = i

        if best_bin == -1:
            bins.append([value])
            free_space.append(capacity - value)
        else:
            bins[best_bin].append(value)
            free_space[best_bin] -= value

    return bins


def show_result(title, packing):
    print(f"\n{title}")
    print("-" * 45)

    for i, b in enumerate(packing, start=1):
        total = sum(b)
        graph = "#" * int(total * 20)

        print(f"Bin {i}: {b}")
        print(f"Used = {total:.1f} | {graph}")

    print(f"Total Bins Used = {len(packing)}")


# Driver Program
items = [0.5, 0.7, 0.3, 0.9, 0.2, 0.6, 0.8, 0.4, 0.1, 0.5]
capacity = 1.0

lower_bound = int(-(-sum(items) // capacity))

print("Items           :", items)
print("Bin Capacity    :", capacity)
print("Total Item Size :", round(sum(items), 2))
print("Lower Bound     :", lower_bound)

ff = first_fit(items, capacity)
ffd = first_fit_decreasing(items, capacity)
bfd = best_fit_decreasing(items, capacity)

show_result("First Fit (FF)", ff)
show_result("First Fit Decreasing (FFD)", ffd)
show_result("Best Fit Decreasing (BFD)", bfd)

print("\nSummary")
print("-" * 25)
print(f"Lower Bound : {lower_bound}")
print(f"FF  Bins    : {len(ff)}")
print(f"FFD Bins    : {len(ffd)}")
print(f"BFD Bins    : {len(bfd)}")
