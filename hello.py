print("Hello World")
print("Hi")

name = "bro"

print(f"Hello {name}")

#Converting variables

print(type(name))
gpa = 3.2

gpa = int(gpa)
print(type(gpa))

age = int(input("what is your age : "))
print( f"you are {age} years old")


friends = 0
friends += 1
print(friends)


age = int(input("enter your age : "))

if age >= 18 :
    print("you are eligible")
elif age<0 :
    print("you are fucked")
else :
    print("you are underaged")