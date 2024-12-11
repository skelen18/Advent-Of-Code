from collections import Counter

def split_number(number):
    str_num = str(number)
    mid = len(str_num) // 2
    left = int(str_num[:mid])
    right = int(str_num[mid:])
    return left, right

def simulate_stones(stones, blinks):
    stone_counts = Counter(stones)
    for _ in range(blinks):
        new_counts = Counter()
        for stone, count in stone_counts.items():
            if stone == 0:
                new_counts[1] += count
            elif len(str(stone)) % 2 == 0:
                left, right = split_number(stone)
                new_counts[left] += count
                new_counts[right] += count
            else:
                new_counts[stone * 2024] += count
        stone_counts = new_counts
    
    return sum(stone_counts.values())

input_stones = [5, 89749, 6061, 43, 867, 1965860, 0, 206250]
blinks = 75

result = simulate_stones(input_stones, blinks)
print("result:", result)


