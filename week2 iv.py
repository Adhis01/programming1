# Getting the range inputs from the user
start = int(input("Enter the start value: "))
end = int(input("Enter the end value: "))
step = int(input("Enter the step value: "))

for i in range(start, end, step):  # Using start, end, and step values for the range
    print(i)
