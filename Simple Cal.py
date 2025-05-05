oparator = input("enter an oparator (+ - / *) : ")

num1 = int(input("Enter number 1 : " ))
num2 = int(input("Enter number 2 : " ))

if oparator == "+" :
    result= num1+num2
elif oparator == "-" :
    result= num1-num2
elif oparator == "*" :
    result = num1*num2
elif oparator == "/" :
    result = num1/num2
else :
    result = "you are an idiot" 

print(result)