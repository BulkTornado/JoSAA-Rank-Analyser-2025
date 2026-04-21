"""
import sys
import csv

with open('temp.csv', 'r', newline='\n') as f:
    reader = csv.reader(f, delimiter='\t')
    _ = list(reader)
    print(len(_))
    for i in _[-10:]:
        print(i)
sys.exit()
"""

import csv
import sqlite3

seat_type = "ALL"

CSV_FILE = "JoSAA_Round_{num}_Result_{seat}.csv"
DB_FILE = "JoSAA_Seat_Allotment.db"

# Connect to SQLite
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS JoSAA_Seat_Allotment(
    round INT,
    institute_name TEXT,
    academic_program TEXT,
    quota TEXT,
    seat_type TEXT,
    gender TEXT,
    opening_rank INT,
    closing_rank INT
);
""")
conn.commit()

for i in range(1, 7):
    # Read CSV and prepare data
    rows_to_insert = []
    fp = CSV_FILE.format(num=i, seat=seat_type)
    with open(fp, 'r', newline='') as f:
        reader = csv.reader(f, delimiter='\t')

        for row in reader:
            # Strip whitespace
            row = [col.strip() for col in row]

            # Convert last two columns to int            
            row[-2] = int(row[-2])
            row[-1] = int(row[-1])
                                   
            rows_to_insert.append(tuple(row))

    # Insert into DB
    cursor.executemany(f"""
    INSERT INTO JoSAA_Seat_Allotment
    VALUES ({i}, ?, ?, ?, ?, ?, ?, ?)
    """, rows_to_insert)


    conn.commit()

    print(f"Round {i}: {len(rows_to_insert)} rows inserted")

conn.close()

