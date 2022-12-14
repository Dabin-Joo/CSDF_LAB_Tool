import sqlite3
from sqlite3 import Error
from registry_parse import UserAssist, Shimcache, OpenSaveMRU, LastVisitedMRU, CIDSizeMRU
from organizing import organize

con = sqlite3.connect('registry_anti.db')
cursor = con.cursor()
cursor.execute("SELECT tool_name, download_file_name, MD5_hash_value FROM Wiping_tool")
list = cursor.fetchall()

Uhash = UserAssist()
Shash = Shimcache()
Chash = CIDSizeMRU()
Lhash = LastVisitedMRU()
Ohash = OpenSaveMRU()
finhash = Uhash + Shash + Chash + Lhash + Ohash

finthash = organize(finhash)
uthash = organize(Uhash)
sthash = organize(Shash)
cthash = organize(Chash)
lthash = organize(Lhash)
othash = organize(Ohash)
finthash = [x for x in finthash]

print('안티 포렌식 툴 목록 : ', end = '')
print(', '.join(finthash))
print('UserAssist : ', end = '')
print(', '.join(uthash))
print('Shimcache : ', end = '')
print(','.join(sthash))
print('CIDSizeMRU : ', end = '')
print(','.join(cthash))
print('LastVisitedMRU : ', end = '')
print(','.join(lthash))
print('OpenSaveMRU : ', end = '')
print(','.join(othash))









