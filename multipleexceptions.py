try:
    num1,num2=eval(input("Two numbers seperated by a comma pls: "))
    result =  num1/num2
    print("Result is:", result)

except ZeroDivisionError:
    print("Division by zero is error")

except SyntaxError:
    print("There is an error in the syntax as comma is missing in the input")

except:
    print("Wrong input")
else:
    print("No exceptions")

finally:
    print("This will execute no matter what")