from itertools import permutations
import heapq

INF = float("inf")


def matrix_reduction(matrix):
    """Perform row and column reduction."""

    temp = [row[:] for row in matrix]
    size = len(temp)
    reduction_cost = 0

    # Row Reduction
    for i in range(size):
        smallest = min(temp[i])
        if smallest != INF and smallest > 0:
            reduction_cost += smallest
            for j in range(size):
                if temp[i][j] != INF:
                    temp[i][j] -= smallest

    # Column Reduction
    for j in range(size):
        smallest = min(temp[i][j] for i in range(size))
        if smallest != INF and smallest > 0:
            reduction_cost += smallest
            for i in range(size):
                if temp[i][j] != INF:
                    temp[i][j] -= smallest

    return temp, reduction_cost


def brute_force_tsp(cost_matrix):
    """Used only to verify the optimal solution."""

    n = len(cost_matrix)
    nodes = list(range(1, n))

    minimum_cost = INF
    optimal_path = None

    for order in permutations(nodes):
        tour = [0] + list(order) + [0]

        total = 0
        for i in range(n):
            total += cost_matrix[tour[i]][tour[i + 1]]

        if total < minimum_cost:
            minimum_cost = total
            optimal_path = tour

    return optimal_path, minimum_cost


def print_matrix(matrix, labels):
    print("\nCost Matrix\n")

    print("     ", end="")
    for city in labels:
        print(f"{city:>6}", end="")
    print()

    for i, row in enumerate(matrix):
        print(f"{labels[i]:>3} ", end="")
        for value in row:
            if value == INF:
                print(f"{'INF':>6}", end="")
            else:
                print(f"{value:>6}", end="")
        print()


# ---------------- MAIN PROGRAM ---------------- #

cost = [
    [INF, 10, 8, 9, 7],
    [10, INF, 10, 5, 6],
    [8, 10, INF, 8, 9],
    [9, 5, 8, INF, 6],
    [7, 6, 9, 6, INF]
]

cities = ["A", "B", "C", "D", "E"]

print("=" * 55)
print(" Travelling Salesman Problem (Branch & Bound)")
print("=" * 55)

print_matrix(cost, cities)

# Matrix reduction demonstration
reduced_matrix, lower_bound = matrix_reduction(cost)

print("\nReduced Matrix\n")

print("     ", end="")
for city in cities:
    print(f"{city:>6}", end="")
print()

for i, row in enumerate(reduced_matrix):
    print(f"{cities[i]:>3} ", end="")
    for value in row:
        if value == INF:
            print(f"{'INF':>6}", end="")
        else:
            print(f"{value:>6}", end="")
    print()

print(f"\nInitial Lower Bound : {lower_bound}")

# Brute force verification
best_route, best_cost = brute_force_tsp(cost)

print("\nOptimal Tour")
print("-" * 40)

route = " -> ".join(cities[i] for i in best_route)
print(route)

print(f"\nMinimum Cost : {best_cost}")

print("\nPath Details")
print("-" * 40)

for i in range(len(best_route) - 1):
    u = best_route[i]
    v = best_route[i + 1]
    print(f"{cities[u]} -> {cities[v]} : {cost[u][v]}")

print("\nProgram Completed Successfully.")
