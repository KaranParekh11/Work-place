import random
count_c=0
count_u=0
print("you have three choice. 1)Rock 2)Paper 3)Scissor . Type any one of them.")
def RC():
    rc=random.randint(0,2)
    if rc==0:
        x="Rock"
    elif rc==1:
        x="Paper"
    else:
        x="Scissor"
    return x
for i in range(5):
    uc = input("enter your choice.").capitalize()
    # print(uc)
    cc=RC()
    # print(cc)
    while uc==cc:
        print("choice is same.computer choosing another one.")
        cc=RC()
        # print(cc)
    if uc!=cc:
        if uc=="Rock" and cc=="Paper":
            print("computer's choice is Paper.you lost.")
            count_c=count_c+1
        elif uc=="Rock" and cc=="Scissor":
            print("computer's choice is Scissor.you won.")
            count_u=count_u+1
        elif uc == "Paper" and cc == "Rock":
            print("computer's choice is Rock.you won.")
            count_u = count_u + 1
        elif uc == "Paper" and cc == "Scissor":
            print("computer's choice is Scissor.you lost.")
            count_c = count_c + 1
        elif uc == "Scissor" and cc == "Rock":
            print("computer's choice is Rock.you lost.")
            count_c = count_c + 1
        elif uc == "Scissor" and cc == "Paper":
            print("computer's choice is Scissor.you won.")
            count_u = count_u + 1
        else:
            print("ahya loop ave to error hase kaik.")
    else:
        print("error!!!")
print("user point is",count_u)
print("computer point is",count_c)
if count_c<count_u:
    print("user won.")
else:
    print("computer won.")



