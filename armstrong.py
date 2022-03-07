
num = int(input("Enter a number: "))
sum = 0
x = num
n=len(str(num)) #for calculate the lenth of number.
if x>0:
    while x > 0:
        y = x % 10 #take last digit one by one.
        sum += y ** n #power of digit and add into sum for last check step63105425988599693916
        x //= 10 #for while loop condition and further calculation
elif x==0:
    print("please enter valid number.")
else:
    z = -x #convert into positive for easy calculation
    while z > 0:
        if n % 2 == 0: #condition for even power
            y = z % 10
            sum = (sum + y ** (n - 1)) #we take n-1 beacause where use negative number negative sign included in length..so reduce length by 1.
            z //= 10
        else:
            break
    sum = -sum #here we calculate as positive number but our number is actual negative so converting sum into negative number for checking.


if num == sum:
    print(num, "is an Armstrong number and the reason is \n")
    count = 1
    if num>0:
        for i in str(num):
            if count < n:
                print(i + "^" + str(n), end="  +  ") #for n-1 lenth
                count += 1
            else:
                print(i + "^" + str(n)+" = "+str(num)) #for last step printing.
    else:
        for i in str(num)[1:]: #here we neglect first character beacuse it is -sign.
            if count < n-1:
                print("-"+i + "^" + str(n-1), end="  +  ") #number is negative so we reduce length by 1.
                count += 1
            else:
                print("-"+i + "^" + str(n-1)+" = "+str(num))

else:
   print(num,"is not an Armstrong number")