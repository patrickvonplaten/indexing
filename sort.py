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

def sort_numbers_in_line(line):
    parts = line.rsplit(':', 1)
    if len(parts) < 2:
        return line  # No colon found, return original line

    # Split the part after the last colon and attempt to sort if they are numbers
    number_parts = parts[1].split(',')
    sorted_parts = []
    for part in number_parts:
        try:
            # Attempt to convert each part to an integer for sorting
            num = int(part.split('-')[0].strip())
            sorted_parts.append(part.strip())  # Strip spaces from each part
        except ValueError:
            # Part is not a number, return the original line
            return line

    sorted_parts.sort(key=lambda x: int(x.split('-')[0].strip()))
    return f"{parts[0]}: {', '.join(sorted_parts)}"  # Single space after comma

def should_sort(sub_entries):
    # Check if any sub-entry starts with 'See also' or 'see also'
    for entry in sub_entries:
        if entry.lower().startswith('see also'):
            return False
    return True

def write_sorted_file(entries, filename):
    with open(filename, 'w') as file:
        count = 1
        for key in sorted(entries.keys()):
            file.write(f"{count}. {key}\n")
            # Check if sub-entries should be sorted
            if should_sort(entries[key]):
                sub_entries = sorted(entries[key])
            else:
                sub_entries = entries[key]

            for value in sub_entries:
                if not value.lower().startswith('see also'):
                    value = sort_numbers_in_line(value)
                file.write(f"    {value}\n")
            count += 1

# Read and process the file
entries = read_and_process_file('input_file.txt')

# Write the sorted entries to a new file
write_sorted_file(entries, 'sorted_file.txt')

print("Sorting complete. Check 'sorted_file.txt'.")
