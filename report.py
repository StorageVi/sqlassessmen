#docstring- vincent
import sqlite3
import sys
DATABASE = 'reportscore'
db=sqlite3.connect(DATABASE)
cursor = db.cursor()
results = cursor.fetchall()
def print_all_score():
    cursor.execute('SELECT * FROM subject_score ORDER BY week_id DESC')
    results = cursor.fetchall()
    print(f"{'WEEK':<17}{'WEEK AVARAGE TOTAL':<31}{'DVC':<11}{'DGT':<11}{'ENG':<11}{'MAT':<11}{'SCI':<11}{'ADP':<11}")
    for score in results:
        print(f"Week: {score[1]:<10} week avarage total: {score[8]:<10} dvc: {score[2]:<5} dgt: {score[3]:<5} eng: {score[4]:<5} mat: {score[5]:<5} sci: {score[6]:<5} adp: {score[7]:<5}")
    return results

def print_all_score_by_avarage_total():
    cursor.execute('SELECT * FROM subject_score ORDER BY avarage_total DESC')
    results = cursor.fetchall()
    print(f"{'WEEK':<17}{'WEEK AVARAGE TOTAL':<31}{'DVC':<11}{'DGT':<11}{'ENG':<11}{'MAT':<11}{'SCI':<11}{'ADP':<11}")
    for score in results:
        print(f"Week: {score[1]:<10} week avarage total: {score[8]:<10} dvc: {score[2]:<5} dgt: {score[3]:<5} eng: {score[4]:<5} mat: {score[5]:<5} sci: {score[6]:<5} adp: {score[7]:<5}")
    return results

header = (f"{'WEEK':<17}{'DVC':<11}{'DGT':<11}{'ENG':<11}{'MAT':<11}{'SCI':<11}{'ADP':<11}{'WEEK AVARAGE TOTAL':<31}")
line = ("="*107)

print(line)
print("Welcome to the report score program\nThis program will show you the score of each subject for each week and the avarage total for each week\nYou can choose to sort the data by week avarage total or by subject\nThe data is stored in a database and can be updated by the user")
print("\n1. All data weekly\n2. Sort by week avarge\n3. Sort select by subject\n4. Insert new data\n5. Delete data\n6. Update data\n7. Replace data\n8. Exit")
print(line)
while True:
    try:
        user_input = int(input("Input command number? "))
        if len(str(user_input)) == 0 or str(user_input).isspace() or 8 < user_input > 0:
            print("Thats was not a valid input. Try again")
            user_input = int(input("Input command number? "))
    except ValueError:
        print("Thats was not a valid input.")
        continue
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        sys.exit()
    if user_input == 1:
        print_all_score()
    elif user_input == 2:
        print_all_score_by_avarage_total()
    elif user_input == 3:
        input_subject = input("What subject(dvc/dgt/eng/mat/sci/adp)? ")
        if input_subject in ["dvc", "dgt", "eng", "mat", "sci", "adp"]:
            print("nothing")
    elif user_input == 4:
        week = input("Week: ")
        dvc = input("DVC: ")
        dgt = input("DGT: ")
        eng = input("ENG: ")
        mat = input("MAT: ")
        sci = input("SCI: ")
        adp = input("ADP: ")
        avarage_total = (int(dvc) + int(dgt) + int(eng) + int(mat) + int(sci) + int(adp)) / 6
        cursor.execute('INSERT INTO subject_score (weekfortnight, dvc, dgt, eng, mat, sci, adp, avarage_total) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (week, dvc, dgt, eng, mat, sci, adp, avarage_total))
        db.commit()
        print("Data inserted successfully")
    elif user_input == 5:
        week = input("Week: ")
        print("Are you sure you want to delete the data? (yes/no)")
        confirm = input().lower()
        if confirm == "yes":
            cursor.execute('DELETE FROM subject_score WHERE weekfortnight = ?', (week,))
            db.commit()
            print("Data deleted successfully")
        else:
            print("Delete cancelled.")
    elif user_input == 6:
        week = input("Week: ")
        dvc = input("DVC: ")
        dgt = input("DGT: ")
        eng = input("ENG: ")
        mat = input("MAT: ")
        sci = input("SCI: ")
        adp = input("ADP: ")
        avarage_total = (int(dvc) + int(dgt) + int(eng) + int(mat) + int(sci) + int(adp)) / 6
        print("Are you sure you want to update the data? (yes/no)")
        confirm = input().lower()
        if confirm == "yes":
            cursor.execute('UPDATE subject_score SET dvc = ?, dgt = ?, eng = ?, mat = ?, sci = ?, adp = ?, avarage_total = ? WHERE weekfortnight = ?', (dvc, dgt, eng, mat, sci, adp, avarage_total, week))
            db.commit()
            print("Data updated successfully")
        else:
            print("Update cancelled.")
    elif user_input == 7:
        print("Replace data...")
        cursor.execute('SELECT * FROM subject_score')
        results = cursor.fetchall()
        week = input("Replaced original week: ")
        new_week = input("New week: ")
        new_dvc = input("New DVC: ")
        new_dgt = input("New DGT: ")
        new_eng = input("New ENG: ")
        new_mat = input("New MAT: ")
        new_sci = input("New SCI: ")
        new_adp = input("New ADP: ")
        new_avarage_total = (int(new_dvc) + int(new_dgt) + int(new_eng) + int(new_mat) + int(new_sci) + int(new_adp)) / 6
        for score in results:
            if score[1] == week:
                cursor.execute('DELETE FROM subject_score WHERE weekfortnight = ?', (week,))
                cursor.execute('INSERT INTO subject_score (weekfortnight, dvc, dgt, eng, mat, sci, adp, avarage_total) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (new_week, new_dvc, new_dgt, new_eng, new_mat, new_sci, new_adp, new_avarage_total))
                db.commit()
                print("Data replaced successfully")
                break
    elif user_input == 8:
        print("Goodbye!")
        break
    else:
        print("Thats was not a valid input. Try again")
        user_input = int(input("Input command number? "))

if __name__ == "__main__":
    print("report.py is being run directly")
else:
    print("report.py is being imported into another module")
