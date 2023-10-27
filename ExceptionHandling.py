a=5
b=2
try:
    print("Resource Open")
    print(a/b)
    k=int(input("Enter a number:"))
    print(k)
except ZeroDivisionError as e:
    print("You can not divide a number by zero",e)
except ValueError as e:
    print("Invalid Input",e)
except Exception as e:
    print("someting went wrong..")
finally:
    print("Resource closed")
