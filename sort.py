#!/usr/bin/env python3
def read_and_process_file(filename):
    with open(filename, 'r') as file:
        content = file.readlines()

    entries = {}
    current_key = None

    for line in content:
        if line.strip() and not line.startswith(" "):
            # Remove original numbering and trim
            current_key = ' '.join(line.strip().split(' ')[1:])
            entries[current_key] = []
        elif current_key:
            entries[current_key].append(line.strip())

    return entries

def write_sorted_file(entries, filename):
    with open(filename, 'w') as file:
        count = 1
        for key in sorted(entries.keys()):
            file.write(f"{count}. {key}\n")
            for value in entries[key]:
                file.write(f"    {value}\n")
            count += 1

# Read and process the file
entries = read_and_process_file('./sorted_file.txt')

# Write the sorted entries to a new file
write_sorted_file(entries, 'sorted_file.txt')

print("Sorting complete. Check 'sorted_file.txt'.")
