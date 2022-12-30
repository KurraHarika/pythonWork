def printSeriesIncreasing(ch,n):
    assert isinstance(ch,str),"First Argument should be string"
    assert isinstance(n,int),"Second Argument should be int"
    for i in range(1,n+1,1):
        print(ch*i)
    return None
def printSeriesDecreasing(ch,n):
    assert isinstance(ch,str),"First Argument should be string"
    assert isinstance(n,int),"Second Argument should be int"
    for i in range(n,0,-1):
        print(ch*i)
    return None

inpCh=input("Enter a Character:")
inpNum=int(input("Enter a no:"))
try:
    printSeriesIncreasing(inpCh,inpNum)
except AssertionError as ob:
    print(ob)
print('-'*40)
try:
    printSeriesDecreasing(inpCh,inpNum)
except AssertionError as ob:
    print(ob)
print('-'*40)
