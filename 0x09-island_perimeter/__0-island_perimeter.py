def island_perimeter(grid):
    perimeter = 0
    if type(grid) is not list:
        return 0
    for i, row in enumerate(grid):
        for j, element in enumerate(row):
            if element == 1:
                # check left
                if j != 0:
                    perimeter += 1 if row[j - 1] == 0 else 0
                # check right
                if j != len(row) - 1:
                    perimeter += 1 if row[j + 1] == 0 else 0
                # check up
                if i != 0:
                    perimeter += 1 if grid[i - 1][j] == 0 else 0
                #  check down
                if i != len(grid) - 1:
                    perimeter += 1 if grid[i + 1][j] == 0 else 0
    return perimeter


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]
    print(island_perimeter(grid))
