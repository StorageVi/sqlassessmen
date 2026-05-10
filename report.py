import sqlite3
db=sqlite3.connect('reportscore')
cursor = db.cursor()
sql = 'SELECT * FROM subject_score'
cursor.execute(sql)
results = cursor.fetchall()
print(results)
db.close()
order_by = input('Order by what? ')