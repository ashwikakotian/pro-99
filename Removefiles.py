# can u check it 

import os
import shutil
import time

path=input("Enter Path Name: ")
days=input("Enter How Old Your File Or Folder Is : ")

days=time.time()
if os.path.exists(path)==True:
    list=os.walk(path)
    getPath=os.path.join(path)
    get_ctime=os.stat(path).st_ctime

    if get_ctime==days:
        os.remove(path)
    elif get_ctime>=days:
        os.remove(path)   
    else:
        shutil.rmtree()
else :
    print("Not Found")

