# CacheRecon
## data_0.py
 + to locate data’s of cache artifacts first thing to do is to calculate information of the index file.

 + every cache entry starts from offset 0x2000(Keep in mind that bytes are displayed in Little-endian format)

 + starting from the index file data_0
 ++ contains datas in 36 Bytes
 ++ 25 ~28 bytes indicates the URL info

 + First 2 Bytes = index number(block number)

 + Third Byte = Where the data is stored at(01 →data_1, 02 → data_2, 03 → data_3)

 + If the last Byte is 80 it means that the data is stored in f_###### way
 
 + data0.py analyze the metadata of data 0 and uses calculate_offest.py to indicate the exact offset of the data
 #### calculat_offset.py
 > data1
 >>  + first 2 bytes x 0x100(block size)  +8192(0x2000)
 *****
 > data2
 > >first 2 bytes x 0x400(block size) +8192(0x2000)
 *****
 > data3
 > >first 2 bytes x 0x1000(block size) +8192(0x2000)


## data_1.py

## Reconstruct.py
