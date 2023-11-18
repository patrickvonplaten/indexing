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

def merge_and_sort_entries(entries1, entries2):
    merged_entries = {**entries1, **entries2}

    for key in merged_entries:
        if key in entries1 and key in entries2:
            merged_entries[key].extend(entries1[key])

    sorted_entries = dict(sorted(merged_entries.items()))

    return sorted_entries

def write_merged_file(merged_entries, filename):
    with open(filename, 'w') as file:
        count = 1
        for key, values in merged_entries.items():
            file.write(f"{count}. {key}\n")
            for value in values:
                file.write(f"    {value}\n")
            count += 1

# Read and process both files
entries_file1 = read_and_process_file('./index.txt')
entries_file2 = read_and_process_file('./index_2.txt')

# Merge and sort the entries
merged_entries = merge_and_sort_entries(entries_file1, entries_file2)

# Write the merged entries to a new file
write_merged_file(merged_entries, 'merged_file.txt')

print("Merging complete. Check 'merged_file.txt'.")
