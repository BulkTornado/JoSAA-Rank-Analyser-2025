import os
import csv
import re

seat_type = "ALL"
CSV_FILE = "JoSAA_Round_{num}_Result_{seat}.csv"

# matches digits followed by P at end
pattern = re.compile(r'^(\d+)P$')

for i in range(1, 7):
    fp = CSV_FILE.format(num=i, seat=seat_type)
    temp_fp = fp + ".tmp"

    with open(fp, 'r', newline='') as infile, open(temp_fp, 'w', newline='') as outfile:
        reader = csv.reader(infile, delimiter='\t')
        writer = csv.writer(outfile, delimiter='\t')

        for row in reader:
            row = [col.strip() for col in row]

            # fix last two columns only
            for idx in [-2, -1]:
                match = pattern.match(row[idx])
                if match:
                    row[idx] = match.group(1)

            writer.writerow(row)

    # overwrite original file
    os.replace(temp_fp, fp)

    print(f"Fixed P-suffix in Round {i}")

