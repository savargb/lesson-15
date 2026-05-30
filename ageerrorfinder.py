try:
    age = int(input("please enter your age:"))
    print("I see that  you are {age} years old")
    if age>18:
        raise ValueError

except ValueError:
    print("Error. Please make the age below 18.")