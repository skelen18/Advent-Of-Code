import os
from collections import deque

script_dir = os.path.dirname(__file__)
infile = os.path.join(script_dir, "input.txt")

try:
    with open(infile, "r") as file:
        D = file.read().strip()
except FileNotFoundError:
    exit(1)

def solve_part1():
    A = deque([])
    SPACE = deque([])
    file_id = 0
    FINAL = []
    pos = 0

    for i, c in enumerate(D):
        if i % 2 == 0: 
            for _ in range(int(c)):
                FINAL.append(file_id)
                A.append((pos, 1, file_id))
                pos += 1
            file_id += 1
        else:  
            SPACE.append((pos, int(c)))
            for _ in range(int(c)):
                FINAL.append(None)
                pos += 1
    for (pos, sz, file_id) in reversed(A):
        for space_i, (space_pos, space_sz) in enumerate(SPACE):
            if space_pos < pos and sz <= space_sz:
                for i in range(sz):
                    assert FINAL[pos + i] == file_id, f'{FINAL[pos + i]=}'
                    FINAL[pos + i] = None
                    FINAL[space_pos + i] = file_id
                SPACE[space_i] = (space_pos + sz, space_sz - sz)
                break
    ans = 0
    for i, c in enumerate(FINAL):
        if c is not None:
            ans += i * c
    return ans

p1 = solve_part1()
print(p1)
