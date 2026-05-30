try: 
    number = int(input("Enter a number: "))
    print("The number enterd is")
except ValueError as ex:
    print("Exception = ",ex)