weight = float(input("Input your weight"))
unit = input("Kilograms or pounds (K/L)")

if unit =="K" :
    weight = weight*2.205
    unit = 'Lbs'
    print(f"your weight is {weight} {unit}")
elif unit == "L" :
    weight = weight/2.205
    unit = "Kgs"
    print(f"your weight is {weight} {unit}")
else :
    print(f"unit {unit} is invalid")