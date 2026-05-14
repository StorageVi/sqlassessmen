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
user_input = input("What order? \n1(all data weekly), \n2(sort by week avarge) \n5(exit) )")
while True:
    if user_input == "1":
        print_all_score()
        pass
    if user_input == "4":
        pass
    if user_input == "5":
        break
    else:
        print("Thats was not a valid input try again")

