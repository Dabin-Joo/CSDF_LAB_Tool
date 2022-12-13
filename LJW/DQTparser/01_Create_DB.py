import sqlite3
import os

# Get OS USERNAME
username = os.environ.get("USERNAME")

# DB 생성 & Auto Commit
make_DB = sqlite3.connect('C:/Users/{}/Desktop/Meta_DB.db'.format(username), isolation_level=None)

# Cursor
data = make_DB.cursor()

# 테이블 생성
data.execute("CREATE TABLE IF NOT EXISTS Editor_DQT(editor text, exif text, hash text)")
data.execute("CREATE TABLE IF NOT EXISTS Editor_Filename(editor text, filename text)")
