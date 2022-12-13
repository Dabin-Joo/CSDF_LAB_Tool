import sqlite3
import os

# DB 생성 & Auto Commit
make_DB = sqlite3.connect('./DQTparser.db', isolation_level=None)

# Cursor
data = make_DB.cursor()

# 테이블 생성
data.execute("CREATE TABLE IF NOT EXISTS Editor_DQT(editor text, exif text, hash text)")
data.execute("CREATE TABLE IF NOT EXISTS Editor_Filename(editor text, filename text)")
