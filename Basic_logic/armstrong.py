num = int(input("Enter number: "))
copy = num
sum = 0
n = len(str(num))

while num > 0:
    digit = num % 10
    sum += digit ** n # symbol of power - **
    num //= 10

if sum == copy:
    print("Armstrong")
else:
    print("Not Armstrong")

# Store armstrong number in list.

n = 500
armstrong_list = []

for num in range(1, n + 1):
    order = len(str(num))
    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** order
        temp //= 10

    if total == num:
        armstrong_list.append(num)

print(armstrong_list)