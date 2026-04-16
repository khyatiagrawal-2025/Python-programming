num = int(input("Enter number: "))
copy = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

if copy == rev:
    print("Palindrome")
else:
    print("Not Palindrome")