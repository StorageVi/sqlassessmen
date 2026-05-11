#docstring- vincent
import sqlite3
DATABASE = 'reportscore'
def print_all_score():
    db=sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT * FROM subject_score'
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through
    print(f"{'Week':<10} {'WEEK AVARAGE TOTAL':<10} {'DVC':<5} {'DGT':<5} {'ENG':<5} {'MAT':<5} {'SCI':<5} {'ADP':<5}")
    for score in results:
        print(f"Week: {score[1]:<10} week avarage total: {score[8]:<10} dvc: {score[2]:<5} dgt: {score[3]:<5} eng: {score[4]:<5} mat:{score[5]:<5} sci: {score[6]:<5} adp: {score[7]:<5}")
    #loop finish here
    db.close()

print_all_score()
order_by = input('Order by what? ')