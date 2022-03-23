import json
def getbyid(id=0):
    with open('db1.json',"r") as f:
        id=int(id)
        rawdata = json.load(f)
        data=rawdata["users"]
        count=0
        c=0
        for i in data:
            if i["id"]==id:
                x=data[count]
                c=1
                break
            else:
                count=count+1
                continue
        if count==len(data) and c==0:
            x="data not found for this id"
    return x

def getall():
    with open('db1.json',"r") as f:
        rawdata = json.load(f)
    return rawdata

def create(data1):
    with open('db1.json',"r") as f:
        rawdata = json.load(f)
        rawdata["users"].append(data1)
    with open('db1.json',"w") as f:
        json.dump(rawdata,f,indent=4)   
    return "profile created successfully."

def deletebyid(id=0):
    with open('db1.json',"r+") as f:
        id=int(id)
        rawdata = json.load(f)
        data=rawdata["users"]
        count=0
        c=0
        for i in data:
            if i["id"]==id:
                data.pop(count)
                x="data deleted successfully"
                c=1
                break
            else:
                count=count+1
                continue
        if count==len(data) and c==0:
            x="data not found for this id or already deleted."
        with open('db1.json',"w") as f:
            json.dump(rawdata,f,indent=4)
    return x

def up_date(id,data2):
    with open('db1.json',"r+") as f:
        id=int(id)
        rawdata = json.load(f)
        data=rawdata["users"]
        count=0
        c=0
        for i in data:
            if i["id"]==id:
                x=data[count]
                x.update(data2)
                print("updated successfully")
                break
            else:
                count=count+1
                continue
        if count==len(data) and c==0:
            x="data can not be update for this id"
        with open('db1.json',"w") as f:
            json.dump(rawdata,f,indent=4)
    return x





