def head():
    return print("+","-","-","-","-","+","-","-","-","-","+")
def body():
    for X in range(3):
        print ("|",end="         ")
def body_full():
    for X in range(4):
        body()
        print("")
def drawing():
    count = 0
    for X in range(3):
        count +=1
        head()
        if(count == 3):
            break
        else:
            body_full()
drawing()