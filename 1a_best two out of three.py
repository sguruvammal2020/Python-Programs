''' Write a python program to find the best of two test average marks
   out of three test's marks accepted from the user
'''
avg_Test1=float(input("Enter the average of Test 1:"))
avg_Test2=float(input("Enter the average of Test 2:"))
avg_Test3=float(input("Enter the average of Test 3:"))
if avg_Test1>avg_Test2 and avg_Test1>avg_Test3:
    best1=avg_Test1
    if avg_Test2>avg_Test3:
        best2=avg_Test2
    else:
        best2=avg_Test3
elif avg_Test2>avg_Test3:
    best1=avg_Test2
    best2=avg_Test3
else:
    best1=avg_Test3
    best2=avg_Test2
print(f"Best two average out of three test's marks are: {best1} and {best2}")