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
            # Ensure a colon before the page numbers
            line = line.strip()
            if ',' in line:
                parts = line.rsplit(',', 1)
                line = f"{parts[0]}: {parts[1]}"
            elif ':' not in line:
                line = f"{line}:"
            entries[current_key].append(line)

    return entries

def write_sorted_file(entries, filename):
    with open(filename, 'w') as file:
        count = 1
        for key in sorted(entries.keys()):
            file.write(f"{count}. {key}\n")
            for value in sorted(entries[key]):
                file.write(f"    {value}\n")
            count += 1

# Read and process the file
entries = read_and_process_file('input_file.txt')

# Write the sorted entries to a new file
write_sorted_file(entries, 'sorted_file.txt')

print("Sorting complete. Check 'sorted_file.txt'.")
