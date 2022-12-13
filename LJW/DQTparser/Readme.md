# DQT parser #
DQT Parser considers the DQT of JPEG images as well as Exif to check the Last Source of Image more accurately.



## 01_Create_DB.py ##
- Create DB(DQTparser.db) for image last source comparison.

## 02_Insert_DQT_Exif.py ##
- This is a process that must be preceded to check the source of the last image, and it is the process of stacking DQT and Exif in the DB. As an input, the folder path containing images edited with a specific editor is entered, and the DQT and Exif of each image are inserted into the DB.
- DQT inserts data hashed with MD5.
- Exif is parsed using the freeware, exiftool.exe (by Phil Harvey).

## 03_Insert_Filename.py ##
- If the image edited with Editor has a specific signature in Filename, 'Editor name & signature' are inserted into the DB.

## 04_Check_Source.py ##
- As a function to check the last source of a specific image, when an image is entered as an input, the DQT, Exif, and Filename characteristics of this image are comprehensively considered to find the corresponding editor name in the DB and print it as output.
