def is_safe(position, current_row, current_col):
    for r in range(current_row):
        placed_col = position[r]

        if placed_col == current_col:
            return False

        if abs(current_row - r) == abs(current_col - placed_col):
            return False

    return True


def solve_n_queens(size):
    position = [-1] * size
    answers = []
    backtracks = [0]

    def place_queen(row):
        if row == size:
            answers.append(position[:])
            return

        for col in range(size):
            if is_safe(position, row, col):
                position[row] = col
                place_queen(row + 1)

                position[row] = -1
                backtracks[0] += 1

    place_queen(0)
    return answers, backtracks[0]


def display_board(solution, size):
    print("+" + "---+" * size)

    for row in range(size):
        print("|", end="")
        for col in range(size):
            if solution[row] == col:
                print(" Q |", end="")
            else:
                print(" . |", end="")
        print()
        print("+" + "---+" * size)


# Main Program

for n in [4, 6, 8]:
    result, count = solve_n_queens(n)

    print(f"\nN = {n}")
    print(f"Solutions = {len(result)}")
    print(f"Backtracks = {count}")

    if n == 4:
        print("\nAll Solutions for N = 4")
        for index, sol in enumerate(result, start=1):
            print(f"\nSolution {index}: {sol}")
            display_board(sol, n)