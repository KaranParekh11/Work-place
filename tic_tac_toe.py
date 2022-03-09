import random
raw1=["_","_","_"]
raw2=["_","_","_"]
raw3=["_","_","_"]
y=0
count=0
print("user's sign is X and computer sign is O.First turn is user's turn.")
def computerturn():
    cc=random.randint(1,9)
    print("computer's number is",cc)
    return cc
def gameboard():
    print(raw1)
    print(raw2)
    print(raw3)
def userturn():
    uc=int(input("enter a number between 1 to 9."))
    while uc<1 or uc>9 :
        print("please enter valid number.")
        uc = int(input("enter a number between 1 to 9."))
    return uc
def kval(y):
    if y==0:
        K="X"
    elif y==1:
        K="O"
    else:
        print("error")
        K=None
    return K
def assignval(p,K):
    global count
    if p==1:
        raw1[0]=K
    elif p==2:
        raw1[1]=K
    elif p==3:
        raw1[2]=K
    elif p==4:
        raw2[0]=K
    elif p==5:
        raw2[1]=K
    elif p==6:
        raw2[2]=K
    elif p==7:
        raw3[0]=K
    elif p==8:
        raw3[1]=K
    elif p==9:
        raw3[2]=K
    else:
        print("error. ")
    count=count+1
def checkwho(l):
    if l=="X":
        print("user won.")
        exit()
    elif l=="O":
        print("computer won.")
        exit()
    else:
        return None
def checkresult():
    if raw1[0]==raw1[1]==raw1[2]:
        checkwho(raw1[0])
    elif raw2[0]==raw2[1]==raw2[2]:
        checkwho(raw2[0])
    elif raw3[0]==raw3[1]==raw3[2]:
        checkwho(raw3[0])
    elif raw1[0]==raw2[0]==raw3[0]:
        checkwho(raw1[0])
    elif raw1[1]==raw2[1]==raw3[1]:
        checkwho(raw1[1])
    elif raw1[2]==raw2[2]==raw3[2]:
        checkwho(raw1[2])
    elif raw1[0]==raw2[1]==raw3[2]:
        checkwho(raw1[0])
    elif raw1[2]==raw2[1]==raw3[0]:
        checkwho(raw1[2])
    else:
        return None
def positioncheck(r):
    data=valreturn(r)
    # print(data)
    while data!="_":
        if y==0:
            print("place is taken.choose another place.")
            r=userturn()
            # print(r)
            data=valreturn(r)
            # print(data)
        elif y==1:
            print("place is taken .computer choosing another place.")
            r=computerturn()
            data=valreturn(r)
            # print(data)
        else:
            print("error in positioncheck!")
    return True,r
def valreturn(r):
    if r == 1:
        return raw1[0]
    elif r == 2:
        return raw1[1]
    elif r == 3:
        return raw1[2]
    elif r == 4:
        return raw2[0]
    elif r == 5:
        return raw2[1]
    elif r == 6:
        return raw2[2]
    elif r == 7:
        return raw3[0]
    elif r == 8:
        return raw3[1]
    elif r == 9:
        return raw3[2]
    else:
        print("error")
        return None
def gamestart():
    global y
    global count
    while count<9:
        if y==0:
            r = userturn()
            pc1 = positioncheck(r)
            pc = pc1[0]
            r = pc1[1]
            if pc == True:
                K = kval(y)
                assignval(r, K)
                print("your number is", r)
                y = y + 1
            else:
                print("something went wrong.")
            print("after your turn.")
            gameboard()
            print("total move is", count)
        elif y==1:
            r = computerturn()
            pc1 = positioncheck(r)
            pc=pc1[0]
            r=pc1[1]
            if pc == True:
                K = kval(y)
                assignval(r, K)
                y = y - 1
            else:
                print("something went wrong.")
            print("after computer's turn.")
            gameboard()
            print("total move is", count)
        else:
            print("something went wrong.")
        checkresult()
    print("match draw")
gamestart()
