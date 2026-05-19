#docstring- vincent
import sqlite3
DATABASE = 'reportscore'
db=sqlite3.connect(DATABASE)
cursor = db.cursor()
def print_all_score():
    cursor.execute('SELECT * FROM subject_score')
    results = cursor.fetchall()
    print(f"{'WEEK':<17}{'WEEK AVARAGE TOTAL':<31}{'DVC':<11}{'DGT':<11}{'ENG':<11}{'MAT':<11}{'SCI':<11}{'ADP':<11}")
    for score in results:
        print(f"Week: {score[1]:<10} week avarage total: {score[8]:<10} dvc: {score[2]:<5} dgt: {score[3]:<5} eng: {score[4]:<5} mat: {score[5]:<5} sci: {score[6]:<5} adp: {score[7]:<5}")

def print_all_score_by_avarage_total():
    cursor.execute('SELECT * FROM subject_score ORDER BY avarage_total DESC')
    results = cursor.fetchall()
    for score in results:
        print(f"Week: {score[1]:<10} week avarage total: {score[8]:<10} dvc: {score[2]:<5} dgt: {score[3]:<5} eng: {score[4]:<5} mat: {score[5]:<5} sci: {score[6]:<5} adp: {score[7]:<5}")

header = (f"{'WEEK':<17}{'DVC':<11}{'DGT':<11}{'ENG':<11}{'MAT':<11}{'SCI':<11}{'ADP':<11}{'WEEK AVARAGE TOTAL':<31}")
line = ("="*107)


print(line)
print("Welcome to the report score program\nThis program will show you the score of each subject for each week and the avarage total for each week\nYou can choose to sort the data by week avarage total or by subject\nThe data is stored in a database and can be updated by the user")
print("\n1. All data weekly\n2. Sort by week avarge\n3. Sort select by subject\n4. Insert data\n5. Delete data\n6. Update data\n7. Exit")
print(line)
user_input = input("What order? ")
while True:
    if user_input == ("") or user_input == (" "):
        print("Thats was not a valid input. Try again")
        user_input = input("What order? ")
    try:
        if user_input == "1":
            print_all_score()
            break
        elif user_input == "2":
            print_all_score_by_avarage_total()
            break
        elif user_input == "3":
            input_subject = input("What subject(dvc/dgt/eng/mat/sci/adp)? ")
            if input_subject in ["dvc", "dgt", "eng", "mat", "sci", "adp"]:
                cursor.execute(f'SELECT * FROM subject_score ORDER BY {input_subject} DESC')
                results = cursor.fetchall()
                print(header)
                print(line)
                for score in results:
                    print(f"Week: {score[1]:<10} dvc: {score[2]:<5} dgt: {score[3]:<5} eng: {score[4]:<5} mat: {score[5]:<5} sci: {score[6]:<5} adp: {score[7]:<5} week avarage total: {score[8]:<10} ")
                break
        elif user_input == "4":
            week = input("Week: ")
            dvc = input("DVC: ")
            dgt = input("DGT: ")
            eng = input("ENG: ")
            mat = input("MAT: ")
            sci = input("SCI: ")
            adp = input("ADP: ")
            avarage_total = (int(dvc) + int(dgt) + int(eng) + int(mat) + int(sci) + int(adp)) / 6
            cursor.execute('INSERT INTO subject_score (week, dvc, dgt, eng, mat, sci, adp, avarage_total) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (week, dvc, dgt, eng, mat, sci, adp, avarage_total))
            db.commit()
            print("Data inserted successfully")
        elif user_input == "5":
            week = input("Week: ")
            cursor.execute('DELETE FROM subject_score WHERE week = ?', (week,))
            db.commit()
            print("Data deleted successfully")
        elif user_input == "6":
            week = input("Week: ")
            dvc = input("DVC: ")
            dgt = input("DGT: ")
            eng = input("ENG: ")
            mat = input("MAT: ")
            sci = input("SCI: ")
            adp = input("ADP: ")
            avarage_total = (int(dvc) + int(dgt) + int(eng) + int(mat) + int(sci) + int(adp)) / 6
            cursor.execute('UPDATE subject_score SET dvc = ?, dgt = ?, eng = ?, mat = ?, sci = ?, adp = ?, avarage_total = ? WHERE week = ?', (dvc, dgt, eng, mat, sci, adp, avarage_total, week))
            db.commit()
            print("Data updated successfully")
        elif user_input == "7":
            print("Goodbye!")
            break
        else:
            print("Thats was not a valid input. Try again")
            user_input = input("What order? ")
    except ValueError:
        pass
if __name__ == "__main__":
    pass