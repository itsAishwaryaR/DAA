def matrix_chain_order(dimensions):
    """
    Matrix Chain Multiplication using Dynamic Programming
    Returns:
        cost_table  -> Minimum multiplication cost
        split_table -> Stores optimal split positions
    """

    total = len(dimensions) - 1

    cost_table = [[0] * (total + 1) for _ in range(total + 1)]
    split_table = [[0] * (total + 1) for _ in range(total + 1)]

    for length in range(2, total + 1):
        for start in range(1, total - length + 2):
            end = start + length - 1
            cost_table[start][end] = float("inf")

            for split in range(start, end):
                current_cost = (
                    cost_table[start][split]
                    + cost_table[split + 1][end]
                    + dimensions[start - 1] * dimensions[split] * dimensions[end]
                )

                if current_cost < cost_table[start][end]:
                    cost_table[start][end] = current_cost
                    split_table[start][end] = split

    return cost_table, split_table


def print_optimal_parens(split_table, left, right):
    if left == right:
        return f"A{left}"

    divide = split_table[left][right]

    left_part = print_optimal_parens(split_table, left, divide)
    right_part = print_optimal_parens(split_table, divide + 1, right)

    return f"({left_part} x {right_part})"


def display_dp_table(cost_table, size):
    print("\nDP Cost Matrix:")

    print(f"{'':6}", end="")
    for col in range(1, size + 1):
        print(f"A{col:<8}", end="")
    print()

    for row in range(1, size + 1):
        print(f"A{row:<5}", end="")
        for col in range(1, size + 1):
            if col < row:
                print(f"{'---':>9}", end="")
            else:
                print(f"{cost_table[row][col]:>9}", end="")
        print()


# Main Program

dimensions = [10, 30, 5, 60, 10]
matrix_count = len(dimensions) - 1

print("Matrix Dimensions:")
for i in range(matrix_count):
    print(f"A{i+1}: {dimensions[i]} x {dimensions[i+1]}")

cost, split = matrix_chain_order(dimensions)

print("\nMinimum Scalar Multiplications:", cost[1][matrix_count])
print("Optimal Parenthesization:",
      print_optimal_parens(split, 1, matrix_count))

display_dp_table(cost, matrix_count)