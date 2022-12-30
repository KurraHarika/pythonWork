def printSeriesDecreasing(ch,n):
    assert isinstance(ch,str),'First Argument should be string'
    assert isinstance(n,int),'Second Argument should be int'
    for i in range(n,0,-1):
        print(ch*i)
    return None

inpCh=input("Enter a Character:")
inpNum=int(input("Enter a no:"))
print('-'*40)

try:
    printSeriesDecreasing(inpCh,inpNum)
except AssertionError as ob:
    print(ob)
    
