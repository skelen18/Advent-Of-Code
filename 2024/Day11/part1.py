def split_number(number):
    str_num = str(number)
    mid = len(str_num) // 2
    left = int(str_num[:mid])
    right = int(str_num[mid:])
    return left, right

def evolve_stones(stones, blinks):
    for _ in range(blinks):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                left, right = split_number(stone)
                new_stones.extend([left, right])
            else:
                new_stones.append(stone * 2024)
        stones = new_stones
    return stones

def count_stones_after_blinks(initial_stones, blinks):
    stones = evolve_stones(initial_stones, blinks)
    return len(stones)

input_stones = [5, 89749, 6061, 43, 867, 1965860, 0, 206250]
blinks = 25

result = count_stones_after_blinks(input_stones, blinks)
print("result:", result)

