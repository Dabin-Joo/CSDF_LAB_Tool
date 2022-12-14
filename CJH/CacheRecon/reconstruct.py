import F_table as F
import os
vid = F.video()
print("Video files are stored in ", F.video())
print("Image files are stored in ", F.image()) 
ans = ["Y", "N", "y", "n"]
recon = input("Do you want to reconstruct the video?(Y/N)")

if recon in ans and recon =="y" or recon =="Y":
    for i in range(0, len(vid)):
        print(i, ":", vid[i])
        i = i+1
    recon_Url_nb = input("Please choose the number of the URL wich you want to reconsturct:")
    recon_URL = vid[int(recon_Url_nb)]
    dir = F.cache()
    dir_selected = dir + "\\" + vid[int(recon_Url_nb)]
    os.chdir(dir_selected)

    Vid_name = input("Name of the reconstructed video:")
    cmd_for_recon = "copy /b * "+ Vid_name + ".mpeg"
    os.system(cmd_for_recon)
"""zero_or_one = ["0","1"]
end = input("Type 1 to view specific cache data\nType 0 to exit:")
"""
"""while end in zero_or_one:
    if end =="1":
        s = input("Which information would you like to view:\n1. URL_size \n \2. Meta data_size\n 3. Data_size\ n 4. Metadata_location\n 5. MDF_Number\n6. Data_location\n 7. DF_Number\n 8. Data_F \n 9. Data type")

    else:
        print("Thank you")
        break"""