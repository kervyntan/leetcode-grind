# Unique Paths
# Count number of unique paths from start point (top left) to ending point (bottom right)
# Single path may move along 0s, and can't visit the same cell more than once
grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 0]
]

ROWS = len(grid)
COLS = len(grid[0])

def dfs(matrix: list[list], row: int, col : int, visited : set):
    # base cases for recursion
    # scenarios where you would stop counting the path as a unique path
    # 1. row/col goes out of bounds of array index (negatively index-wise)
    # 2. you are traversing to a spot in the matrix that you have already visited
    # 3. You hit a spot in the matrix where value is 1
    # 4. Goes out of array positively
    # in these cases, stop the recursion and return 0, because the unique path can't be from here
    if (row < 0 or col < 0) or (row > ROWS - 1 or col > COLS - 1) or ( (row, col) in visited ) or ( matrix[row][col] == 1 ):
        return 0

    # if row == ROWS - 1, col == COLS - 1
    # reached the bottom right, means you found a unique path
    if row == ROWS - 1 and col == COLS - 1:
        return 1
    
    # add to visited
    visited.add((row, col))

    # number of unique paths
    count = 0
    
    # recurse on the 4 different paths you can take from a single position
    # wishful think and step through debugger

    # add to the existing count when recursive call returns 
    # if it returns 1, means it hits the outcome while fulfilling constraints in first base case

    # 1. Move to the down
    count += dfs(matrix, row + 1, col, visited)

    # 2. Move up
    count += dfs(matrix, row - 1, col, visited)

    # 3. Move left
    count += dfs(matrix, row, col - 1, visited)

    # 4. Move right
    count += dfs(matrix, row, col + 1, visited)

    # Remove from visited at the end of the recursive calls returning
    # to allow for backtracking
    visited.remove((row, col))

    return count

print(dfs(grid, 0, 0, set()))
