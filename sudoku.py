import random as rd

def check_valid(grid, row, col, num):
    valid = True
    for x in range(9):
        if grid[x][col] == num:
            valid = False
    for y in range(9):
        if grid[row][y] == num:
            valid = False

    row_sec = row // 3
    col_sec = col // 3

    for i in range(3):
        for j in range(3):
            if grid[row_sec*3 + i][col_sec*3 + j] == num:
                valid = False

    return valid


def gridprint(grid):
    for i in range(len(grid) + 1):
        if i % 3 == 0:
            print(" -" * (len((grid[0])) + 7))
        if i == 9:
            break
        for j in range(len(grid[i]) + 1):
            if (j) % 3 == 0:
                print(" | ", end=" ")
            if j == 9:
                break
            print(grid[i][j], end=" ")
        print()


def sudoku():
    grid = [["_" for x in range(9)] for y in range(9)]

    print("Welcome to sudoku puzzle creator!")
    inp1 = input("Write the hardness level you want. Hard(h), normal(n) or easy(e): ").lower().strip()
    while inp1:
        if inp1 == "h":
            hardness = 12
            break
        elif inp1 == "n":
            hardness = 17
            break
        elif inp1 == "e":
            hardness = 20
            break
        else:
            inp1 = input("Invalid character. Please use \"h\", \"n\" or \"e\": ").lower().strip()


    for i in range(hardness):
        row = rd.randrange(9)
        col = rd.randrange(9)
        num = rd.randrange(1,10)
        while not check_valid(grid, row, col, num) or grid[row][col] != "_":
            row = rd.randrange(9)
            col = rd.randrange(9)
            num = rd.randrange(1,10)
        grid[row][col] = num

    gridprint(grid)
    print(grid)


sudoku()