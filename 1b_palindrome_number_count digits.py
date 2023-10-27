'''
1b_Develop a Python program to check whether a given number is palindrome
(e.g. 121,1331,2002,12321) or not and also count the number of
occurrences of each digit in the input number
'''

num = int(input("Enter the integer:"))
str_num=str(num)       # Convert the integer number into string
reverse_str=str_num[::-1]     # Reverse the string by slicing
if(str_num==reverse_str):
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not palindrome")
digit_count={}     # dictionary to hold the digit as key and count as value
for digit in str_num:
    if digit.isdigit():
        digit=int(digit)
        if digit in digit_count:
            digit_count[digit]+=1
        else:
            digit_count[digit]=1
for i in digit_count:
    print("Number of occurrences of",i,"is",digit_count[i])




