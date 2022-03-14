import json
def main():
    global a
    k = 0
    a = input("enter number of operation which do you want.\n1.ADD\n2.SHOW\n3.FIND\n4.UPDATE\n5.DELETE\n6.EXIT")
    while k != 1:
        try:
            a = int(a)
            k = 1
        except:
            a = input("enter valid number between 1 to 6")
    return a
def add():
    try:
        with open('studentdata.json') as json_file:
            data = json.load(json_file)
    except:
        data=[]
    dict1={}
    details={}
    name=input("enter name")
    while True:
        count=len(data)
        for i in data:
            if i['name']==name:
                name=input("name already taken.choose another name.")
            else:
                count=count-1
        if count==0:
            dict1['name']=name
            break
    an = input("enter a number of raw-information you want to add.if name and email id then enter 2.")
    while True:
        try:
            an=int(an)
            break
        except:
            print("enter valid number.")
            an = input("enter a number of raw-information you want to add.if name and email id then enter 2.")
    for i in range(an):
        x=input ("enter information's title")
        y=input("enter information's value of "+x)
        details[x]=y
    dict1['Details']=details
    data.append(dict1)
    # print(data)
    with open("studentdata.json.", "r+") as file:
        json.dump(data,file,indent=4)
def show():
    try:
        with open('studentdata.json') as json_file:
                data = json.load(json_file)
                for i in data:
                    print(i)
    except:
            print("file is empty")
def find():
    n=input("enter name of user which do you want to find!!")
    with open('studentdata.json') as json_file:
        data = json.load(json_file)
        count=len(data)
        for i in data:
            if i["name"]==n:
                print(i)
                break
            else:
                count=count-1
                continue
        if count==0:
            print("data not found for this user.")
def update():
    n = input("enter name of user which data do you want to update!!")
    with open('studentdata.json') as json_file:
        data = json.load(json_file)
        count = len(data)
        for i in data:
            if i["name"] == n:
                print(i)
                val=input("enter 0 for name change and 1 for details changes and 2 for changing in feature name")
                while True:
                    try:
                        val=int(val)
                        if val==0 or val==1 or val==2:
                            break
                        else:
                            val = input("enter valid number 0 or 1 or 2.")
                    except:
                        val=input("enter valid number 0 or 1 or 2.")
                if val==0:
                    name=input("enter new name!!")
                    while True:
                        count = len(data)
                        for i in data:
                            if i['name'] == name:
                                name = input("name already taken.choose another name.")
                            else:
                                count = count - 1
                        if count == 0:
                            break
                    i['name']=name
                    print("name sucessfully changed.")
                elif val==1:
                    dv=input("enter feature name which one do you want to update")
                    vx=i['Details']
                    if dv in vx.keys():
                        value=input("enter the new value of feature")
                        vx[dv]=value
                        print("value sucessfully updated.")

                    else:
                        nf=input("enter feature title.")
                        nv=input("enter feature value .")
                        vx[nf]=nv
                        print("new feature sucessfully added.")
                else:
                    of = input("enter old feature title.")
                    vy=i['Details']
                    cf=0
                    for i in vy.keys():
                        if i==of:
                            nfn = input("enter new feature value .")
                            vy[nfn]=vy.pop(of)
                            print("feature name successfully changed.")
                            cf=None
                            break
                        else:
                            cf=cf+1
                            continue
                    if cf==len(vy):
                        print("there is no such old feature.")
            else:
                count = count - 1
                continue
        if count == 0:
            print("data not found for this user.")
    with open("studentdata.json","w+") as f:
        json.dump(data,f,indent=4)
def delete():
    n = input("enter name of user which data do you want to delete!!")
    with open('studentdata.json',"r+") as json_file:
        data = json.load(json_file)
        count = 0
        for i in data:
            if i['name'] == n:
                data.pop(count)
                print("data deleted succesfully!!!")
                count=None
                break
            else:
                count = count + 1
                continue
        if count == len(data):
            print("data not found for this user or already deleted..")
    with open("studentdata.json","w+") as f:
        json.dump(data,f,indent=4)
def emptycheck():
    try:
        with open('studentdata.json') as json_file:
            data = json.load(json_file)
            z=1
    except:
        z=0
    return z
a=main()
while True:
    while (a <= 6 and a >= 1):
        if a==1:
            add()
        elif a==2:
            show()
        elif a==3:
            ec=emptycheck()
            if ec==0:
                print("file is empty.cant do operation.")
            else:
                find()
        elif a==4:
            ec = emptycheck()
            if ec == 0:
                print("file is empty.cant do operation.")
            else:
                update()
        elif a==5:
            ec = emptycheck()
            if ec == 0:
                print("file is empty.cant do operation.")
            else:
                delete()
        elif a==6:
            exit()
        a=main()
    else:
        print("Enter a valid number.")
        a=main()



