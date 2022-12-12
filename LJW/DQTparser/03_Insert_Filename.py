import sqlite3

### 시작 ### 
connect_db_path = input("Enter the DB path to link => ")

# DB 연동
connect_db = sqlite3.connect(connect_db_path)
cursor_db = connect_db.cursor()

# DB 데이터 삽입 (editor, filename)
editor = input("Enter Editor Name => ")
filename = input("Enter Filename Character of Editor's Image => ")

cursor_db.execute('SELECT * FROM Editor_Filename')
raw_data = cursor_db.fetchall()

# DB내 동일 내용이 없을 경우에만 INSERT
data = (editor, filename)
if data not in raw_data:
    cursor_db.execute("INSERT INTO Editor_Filename (editor, filename) VALUES (?, ?)", data)
    connect_db.commit()

print('\033[31m' + "Data insertion is complete." + '\033[0m')

connect_db.close()