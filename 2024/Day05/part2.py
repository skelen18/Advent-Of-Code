import os

def parse_input(file_path):
    with open(file_path, 'r') as file:
        input_text = file.read()
    rules_text, updates_text = input_text.strip().split("\n\n")
    rules = [tuple(map(int, line.split('|'))) for line in rules_text.splitlines()]
    updates = [list(map(int, line.split(','))) for line in updates_text.splitlines()]
    return rules, updates

def is_valid_update(update, rules):
    for a, b in rules:
        if a in update and b in update:
            if update.index(a) > update.index(b):
                return False
    return True

def fix_update(update, rules):
    dependencies = {page: [] for page in update}
    for a, b in rules:
        if a in update and b in update:
            dependencies[b].append(a)
    sorted_update = []
    while dependencies:
        free_pages = [page for page, deps in dependencies.items() if not deps]
        if not free_pages:
            raise ValueError("Cyclic dependency detected!")
        free_pages.sort()
        for page in free_pages:
            sorted_update.append(page)
            del dependencies[page]
        for deps in dependencies.values():
            deps[:] = [dep for dep in deps if dep not in free_pages]
    return sorted_update

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "input.txt")  #input
    
    rules, updates = parse_input(file_path)
    invalid_updates = []
    for update in updates:
        if not is_valid_update(update, rules):
            invalid_updates.append(update)
    
    fixed_updates = [fix_update(update, rules) for update in invalid_updates]
    middle_pages = [update[len(update) // 2] for update in fixed_updates]
    result = sum(middle_pages)
    print("REsult:", result)
    input("\nPress Enter to end...") 

if __name__ == "__main__":
    main()
