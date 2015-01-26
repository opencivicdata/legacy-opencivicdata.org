import csv


unique = []
dup = []
fields = ['division', 'jurisdiction', 'name']

with open('active-jurisdictions.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    seen = set()
    rows = [x for x in reader]

    for row in rows[::-1]:
        key = row['jurisdiction']
        if key not in seen:
            seen.add(key)
            unique.append(row)
        else:
            dup.append(row)

with open('active-jurisdictions.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    for row in unique[::-1]:
        writer.writerow(row)

with open('dups_removed.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    for row in dup[::-1]:
        try:
            writer.writerow(row)
        except ValueError:
            # Due to unquoted commas, some names spill into an extra field
            pass

print(
        "{} duplicates found and removed".format(len(dup)) +
        "\nSee dups_removed.csv file for a full list"
        )
