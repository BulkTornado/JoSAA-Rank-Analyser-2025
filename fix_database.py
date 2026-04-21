"""
all rounds are separate table.
this will be run once and then never again.
after running, all rounds data will be merged in a single table.
"""

import csv
import sqlite3

DB_FILE = "JoSAA_Seat_Allotment.db"

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

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

for i in range(1,7):
    cursor.execute(f"SELECT * FROM Round_{i}")
    _ = cursor.fetchall()
    cursor.executemany(f"""
        INSERT INTO JoSAA_Seat_Allotment
        VALUES ({i}, ?, ?, ?, ?, ?, ?, ?)
        """, _)
    conn.commit()
    print(f"Data from table Round_{i} added successfully.")

print("Script finished")
