#docstring- vincent
import sqlite3
DATABASE = 'reportscore'
db=sqlite3.connect(DATABASE)
cursor = db.cursor()
def print_all_score():
    cursor.execute('SELECT * FROM subject_score')
    results = cursor.fetchall()
    #loop through
    print(f"{'WEEK':<16} {'WEEK AVARAGE TOTAL':<30} {'DVC':<10} {'DGT':<10} {'ENG':<10} {'MAT':<10} {'SCI':<10} {'ADP':<10}")
    for score in results:
        print(f"Week: {score[1]:<10} week avarage total: {score[8]:<10} dvc: {score[2]:<5} dgt: {score[3]:<5} eng: {score[4]:<5} mat: {score[5]:<5} sci: {score[6]:<5} adp: {score[7]:<5}")
def print_all_score_by_avarage_total():
    cursor.execute('SELECT * FROM subject_score ORDER BY avarage_total DESC')



print("\n1. All data weekly\n2. Sort by week avarge\n5. Exit")
user_input = int(input("What order? "))
while True:
    if user_input == ("") or user_input == (" "):
        print("Invalid Input.")
    try
        if user_input == 1:
            print_all_score()
            break
        elif user_input == "4":
            pass
        elif user_input == "5":
            break
        else:
            print("Thats was not a valid input. Try again")
            break
    except ValueError:

