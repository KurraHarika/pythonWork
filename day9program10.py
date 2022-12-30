def printDay(dn):
    mn=''
    if (dn==1):
        mn= "SUNDAY"
    elif(dn==2):
        mn= "MONDAY"
    elif(dn==3):
        mn= "TUESDAY"
    elif(dn==4):
        mn= "WEDNESDAY"
    elif(dn==5):
        mn= "THURSDAY"
    elif(dn==6):
        mn= "FRIDAY"                                                                                      
    elif(dn==7):
        mn= "SATURDAY"
    else:
        mn= "Invalid"
    return mn
def printDay1(dn):
    mn=''
    if (dn==1):
        mn= "SUNDAY"
    if(dn==2):
        mn= "MONDAY"
    if(dn==3):
        mn= "TUESDAY"
    if(dn==4):
        mn= "WEDNESDAY"
    if(dn==5):
        mn= "THURSDAY"
    if(dn==6):
        mn= "FRIDAY"                                                                                      
    if(dn==7):
        mn= "SATURDAY"
    
    return mn
import time
for i in range(7):
    inpNum=int(input())
    start=time.time()
    print(printDay(inpNum))
    print((time.time()-start))
    start=time.time()
    print(printDay1(inpNum))
    print((time.time()-start))
    
