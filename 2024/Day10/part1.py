import os
from collections import deque

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

def bfs(grid, start):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([start])
    visited = set()
    visited.add(start)
    score = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < len(grid) and  
                0 <= ny < len(grid[0]) and
                (nx, ny) not in visited and  
                grid[nx][ny] == grid[x][y] + 1  
            ):
                visited.add((nx, ny))
                queue.append((nx, ny))
                if grid[nx][ny] == 9:
                    score += 1
    return score

def calculate_total_score(grid):
    trailheads = find_trailheads(grid)
    total_score = sum(bfs(grid, trailhead) for trailhead in trailheads)
    return total_score

if __name__ == "__main__":
    grid = load_input()
    total_score = calculate_total_score(grid)
    print("Result:", total_score)
