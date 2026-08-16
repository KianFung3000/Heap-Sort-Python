import csv
from DSAHeapEntry import DSAHeapEntry
from DSAHeap import heap_sort

def load_csv(filename):
    entries = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:  # Assuming the first column is priority, second is value
                priority = int(row[0])
                value = row[1]
                entry = DSAHeapEntry(priority, value)
                entries.append(entry)
    return entries

def save_csv(filename, sorted_entries):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for entry in sorted_entries:
            writer.writerow([entry.get_priority(), entry.get_value()])

# Example usage (you can remove this part later)
if __name__ == "__main__":
    # Load entries from a CSV file and display them
    entries = load_csv("RandomNames7000(1).csv")
    print("Loaded entries:")
    for entry in entries:
        print(entry)

    # Assuming we want to sort and save these entries
    sorted_entries = heap_sort(entries)
    save_csv("SortedNames.csv", sorted_entries)
