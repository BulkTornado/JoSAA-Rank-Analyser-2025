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

CSV_FILE = "JoSAA_Round_6_Result.csv"
DB_FILE = "JoSAA_Seat_Allotment.db"

# Connect to SQLite
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Round_6(
    institute_name TEXT,
    academic_program TEXT,
    quota TEXT,
    seat_type TEXT,
    gender TEXT,
    opening_rank INT,
    closing_rank INT
);
""")

# Read CSV and prepare data
rows_to_insert = []

with open(CSV_FILE, 'r', newline='') as f:
    reader = csv.reader(f, delimiter='\t')

    for row in reader:
        # Strip whitespace
        row = [col.strip() for col in row]

        # Convert last two columns to int
        row[-2] = int(row[-2])
        row[-1] = int(row[-1])

        rows_to_insert.append(tuple(row))

# Insert into DB
cursor.executemany("""
INSERT INTO Round_6
VALUES (?, ?, ?, ?, ?, ?, ?)
""", rows_to_insert)

conn.commit()
conn.close()

print(f"Number of rows inserted: {len(rows_to_insert)}")
