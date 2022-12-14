import os
def f_path(a,b):

    
    T = True
    while T == True:
        if os.path.isdir(a) == False:
            a=input("***Invalid Route*** Please enter the route again:")
            continue
        for i in range (0,len(b)):
            f_check = a.replace("\\","/")
            if os.path.isfile(f_check+"/"+b[i]) == False:
                a=input("***Cant find "+b[i]+" file*** Please enter the route again:")
                break
            else:
                T = False
                break       
        continue
    return f_check