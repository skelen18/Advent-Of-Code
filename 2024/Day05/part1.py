import os

def parse_input(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    rules_section, updates_section = text.strip().split("\n\n")
    rules = [tuple(map(int, line.split("|"))) for line in rules_section.splitlines()]
    updates = [list(map(int, line.split(","))) for line in updates_section.splitlines()]
    return rules, updates

def is_valid_update(update, rules):
    for x, y in rules:
        if x in update and y in update:
            if update.index(x) > update.index(y):
                return False
    return True

def process_updates(rules, updates):
    valid_updates = []
    for update in updates:
        if is_valid_update(update, rules):
            valid_updates.append(update)
    return valid_updates

def calculate_middle_sum(valid_updates):
    middle_sum = 0
    for update in valid_updates:
        middle_index = len(update) // 2
        middle_sum += update[middle_index]
    return middle_sum

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "input.txt") # input 
    
    rules, updates = parse_input(file_path)
    valid_updates = process_updates(rules, updates)
    result = calculate_middle_sum(valid_updates)
    print("Result:", result)
    
    input("\nPress Enter to end...")  

if __name__ == "__main__":
    main()
