import csv
import re
import os

seat_type = "ALL"
CSV_FILE = "JoSAA_Round_{num}_Result_{seat}.csv"

# matches integer with .0
pattern = re.compile(r'^(\d+)\.0$')

for i in range(1, 7):
    fp = CSV_FILE.format(num=i, seat=seat_type)
    temp_fp = fp + ".tmp"

    with open(fp, 'r', newline='') as infile, open(temp_fp, 'w', newline='') as outfile:
        reader = csv.reader(infile, delimiter='\t')
        writer = csv.writer(outfile, delimiter='\t')

        for row in reader:
            row = [col.strip() for col in row]

            for idx in [-2, -1]:
                match = pattern.match(row[idx])
                if match:
                    row[idx] = match.group(1)

            writer.writerow(row)

    os.replace(temp_fp, fp)

    print(f"Fixed trailing .0 in Round {i}")

