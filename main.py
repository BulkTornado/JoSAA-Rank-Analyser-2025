import sqlite3

"""
SELECT round, institute_name, academic_program, quota, seat_type, gender, opening_rank, closing_rank FROM JoSAA_Seat_Allotment WHERE quota = 'OS' AND 291402 BETWEEN (opening_rank-10000) AND (closing_rank+10000) ORDER BY seat_type, round;

SELECT round, institute_name, academic_program, quota, seat_type, gender, opening_rank, closing_rank FROM JoSAA_Seat_Allotment WHERE 291402 BETWEEN (opening_rank-10000) AND (closing_rank+10000) ORDER BY seat_type, round;

SELECT DISTINCT(academic_program) FROM JoSAA_Seat_Allotment ORDER BY academic_program;

SELECT * FROM JoSAA_Seat_Allotment
WHERE
	round = 1 AND
	gender != 'Female-only (including Supernumerary)'
	AND quota NOT IN ('LA', 'JK')
	AND 291402 BETWEEN (opening_rank-10000) AND (closing_rank+10000)
	AND (
		institute_name LIKE '%West Bengal%'
		OR institute_name LIKE '%Patna$'
		OR institute_name LIKE '%Bihar%'
		OR institute_name LIKE '%Ranchi%'
	)
ORDER BY seat_type, round;

SELECT * FROM JoSAA_Seat_Allotment
WHERE
        round = 2 AND
        gender != 'Female-only (including Supernumerary)'
        AND quota NOT IN ('LA', 'JK')
        AND 291402 BETWEEN (opening_rank-10000) AND (closing_rank+10000)
        AND (
                institute_name LIKE '%West Bengal%'
                OR institute_name LIKE '%Patna$'
                OR institute_name LIKE '%Bihar%'
                OR institute_name LIKE '%Ranchi%'
        )
ORDER BY seat_type, round;

SELECT * FROM JoSAA_Seat_Allotment
WHERE
        round = 3 AND
        gender != 'Female-only (including Supernumerary)'
        AND quota NOT IN ('LA', 'JK')
        AND 291402 BETWEEN (opening_rank-10000) AND (closing_rank+10000)
        AND (
                institute_name LIKE '%West Bengal%'
                OR institute_name LIKE '%Patna$'
                OR institute_name LIKE '%Bihar%'
                OR institute_name LIKE '%Ranchi%'
        )
ORDER BY seat_type, round;

SELECT * FROM JoSAA_Seat_Allotment
WHERE
        round = 4 AND
        gender != 'Female-only (including Supernumerary)'
        AND quota NOT IN ('LA', 'JK')
        AND 291402 BETWEEN (opening_rank-10000) AND (closing_rank+10000)
        AND (
                institute_name LIKE '%West Bengal%'
                OR institute_name LIKE '%Patna$'
                OR institute_name LIKE '%Bihar%'
                OR institute_name LIKE '%Ranchi%'
        )
ORDER BY seat_type, round;

SELECT * FROM JoSAA_Seat_Allotment
WHERE
        round = 5 AND
        gender != 'Female-only (including Supernumerary)'
        AND quota NOT IN ('LA', 'JK')
        AND 291402 BETWEEN (opening_rank-10000) AND (closing_rank+10000)
        AND (
                institute_name LIKE '%West Bengal%'
                OR institute_name LIKE '%Patna$'
                OR institute_name LIKE '%Bihar%'
                OR institute_name LIKE '%Ranchi%'
        )
ORDER BY seat_type, round;

SELECT * FROM JoSAA_Seat_Allotment
WHERE
        round = 6 AND
        gender != 'Female-only (including Supernumerary)'
        AND quota NOT IN ('LA', 'JK')
        AND 291402 BETWEEN (opening_rank-10000) AND (closing_rank+10000)
        AND (
                institute_name LIKE '%West Bengal%'
                OR institute_name LIKE '%Patna$'
                OR institute_name LIKE '%Bihar%'
                OR institute_name LIKE '%Ranchi%'
        )
ORDER BY seat_type, round;

	AND academic_program IN ('')

7.68440

291402
"""

def check_in_range():
	delta_marks = 0

	try:
		current_rank = int(input("Enter your current JEE MAINS rank: "))
	except Exception as error:
		print(f"Error: {error}")
		print("Failed to get user's rank. Stopping script")
		return
	
	while True:
        ...
		user_input = input("\nContinue to check in the next +-100 range or STOP? (y/N) ").strip().lower()
		if user_input == 'n':
			print("Stopping...")
			break
		elif user_input == 'y':
			delta_marks += 100
			continue
		else:
			print("Invalid input. Stopping operation.")
			break

def main():
    print("Hello from josaa-rank-analyser-2025!")


if __name__ == "__main__":
    main()
