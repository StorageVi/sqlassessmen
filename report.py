#docstring- vincent
import sqlite3
DATABASE = 'reportscore'
db=sqlite3.connect(DATABASE)
cursor = db.cursor()

def print_all_score():
    cursor.execute('SELECT * FROM subject_score')
    results = cursor.fetchall()
    #loop through
    print(f"{'WEEK':<17}{'WEEK AVARAGE TOTAL':<31}{'DVC':<11}{'DGT':<11}{'ENG':<11}{'MAT':<11}{'SCI':<11}{'ADP':<11}")
    for score in results:
        print(f"Week: {score[1]:<10} week avarage total: {score[8]:<10} dvc: {score[2]:<5} dgt: {score[3]:<5} eng: {score[4]:<5} mat: {score[5]:<5} sci: {score[6]:<5} adp: {score[7]:<5}")

def print_all_score_by_avarage_total():
    cursor.execute('SELECT * FROM subject_score ORDER BY avarage_total DESC')
    results = cursor.fetchall()
    for score in results:
        print(f"Week: {score[1]:<10} week avarage total: {score[8]:<10} dvc: {score[2]:<5} dgt: {score[3]:<5} eng: {score[4]:<5} mat: {score[5]:<5} sci: {score[6]:<5} adp: {score[7]:<5}")

header = (f"{'WEEK':<17}{'WEEK AVARAGE TOTAL':<31}{'DVC':<11}{'DGT':<11}{'ENG':<11}{'MAT':<11}{'SCI':<11}{'ADP':<11}")
print("\n1. All data weekly\n2. Sort by week avarge\n3. Sort by DVC\n4. Sort by DGT\n5. Sort by ENG\n6. Sort by MAT\n7. Sort by SCI\n8. Sort by ADP\n9. Exit")
user_input = int(input("What order? "))
while True:
    if user_input == ("") or user_input == (" "):
        print("Invalid Input.")
    try:
        if user_input == 1:
            print_all_score()
            break
        elif user_input == 2:
            print_all_score_by_avarage_total()
            break
        elif user_input == 3:
            cursor.execute('SELECT * FROM subject_score ORDER BY dvc DESC')
            results = cursor.fetchall()
            print(header)
            for score in results:
                print(f"Week {score[1]:<10} dvc: {score[2]:<5} dgt: {score[3]:<5} eng: {score[4]:<5} mat: {score[5]:<5} sci: {score[6]:<5} adp: {score[7]:<5} week avarage total: {score[8]:<10} ")
            break
        elif user_input == 4:
            cursor.execute('SELECT * FROM subject_score ORDER BY dgt DESC')
            results = cursor.fetchall()
            for score in results:
                print(f"Week {score[1]:<10} dvc: {score[2]:<5} dgt: {score[3]:<5} eng: {score[4]:<5} mat: {score[5]:<5} sci: {score[6]:<5} adp: {score[7]:<5} week avarage total: {score[8]:<10} ")
            break
        elif user_input == 5:
            cursor.execute('SELECT * FROM subject_score ORDER BY eng DESC')
            results = cursor.fetchall()
            for score in results:
                print(f"Week {score[1]:<10} dvc: {score[2]:<5} dgt: {score[3]:<5} eng: {score[4]:<5} mat: {score[5]:<5} sci: {score[6]:<5} adp: {score[7]:<5} week avarage total: {score[8]:<10} ")
            break
        elif user_input == 6:
            cursor.execute('SELECT * FROM subject_score ORDER BY mat DESC')
            results = cursor.fetchall()
            for score in results:
                print(f"Week {score[1]:<10} dvc: {score[2]:<5} dgt: {score[3]:<5} eng: {score[4]:<5} mat: {score[5]:<5} sci: {score[6]:<5} adp: {score[7]:<5} week avarage total: {score[8]:<10} ")
            break
        elif user_input == 7:
            cursor.execute('SELECT * FROM subject_score ORDER BY sci DESC')
            results = cursor.fetchall()
            for score in results:
                print(f"Week {score[1]:<10} dvc: {score[2]:<5} dgt: {score[3]:<5} eng: {score[4]:<5} mat: {score[5]:<5} sci: {score[6]:<5} adp: {score[7]:<5} week avarage total: {score[8]:<10} ")
            break
        elif user_input == 8:
            cursor.execute('SELECT * FROM subject_score ORDER BY adp DESC')
            results = cursor.fetchall()
            for score in results:
                print(f"Week {score[1]:<10} dvc: {score[2]:<5} dgt: {score[3]:<5} eng: {score[4]:<5} mat: {score[5]:<5} sci: {score[6]:<5} adp: {score[7]:<5} week avarage total: {score[8]:<10} ")
            break
        else:
            print("Thats was not a valid input. Try again")
            break
    except ValueError:
        pass
if __name__ == "__main__":
    pass