import os

def load_input(file_name="input.txt"):
    script_dir = os.path.dirname(__file__)
    infile = os.path.join(script_dir, file_name)
    try:
        with open(infile, "r") as file:
            return [list(map(int, line.strip())) for line in file.readlines()]
    except FileNotFoundError:
        exit(1)

def find_trailheads(grid):
    trailheads = []
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 0:
                trailheads.append((row, col))
    return trailheads

def dfs(grid, x, y, memo):
    if (x, y) in memo:
        return memo[(x, y)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    total_paths = 0 
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if (
            0 <= nx < len(grid) and
            0 <= ny < len(grid[0]) and
            grid[nx][ny] == grid[x][y] + 1
        ):
            total_paths += dfs(grid, nx, ny, memo)
    total_paths = max(total_paths, 1 if grid[x][y] == 9 else total_paths)
    memo[(x, y)] = total_paths
    return total_paths

def calculate_total_rating(grid):
    trailheads = find_trailheads(grid)
    memo = {}
    total_rating = sum(dfs(grid, x, y, memo) for x, y in trailheads)
    return total_rating

if __name__ == "__main__":
    grid = load_input()
    total_rating = calculate_total_rating(grid)
    print("result:", total_rating)
