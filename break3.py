user_input = int(input("Enter a number: "))
count = 0
half_range = user_input // 2

for i in range(user_input + 1):
    if i == half_range:
        break
    print(i)
