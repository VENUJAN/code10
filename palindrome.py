number = int(raw_input("enter a number"))
sum = 0
n= number
while num != 0:
rem = number % 10
sum = (sum * 10)+rem
number = number / 10
if sum == n:
print(n,"is an palindrome")
else
print(n," is not a palindrome")
