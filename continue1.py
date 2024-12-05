i = 0
while i <= 9:  # Loop until i is less than or equal to 9
    if i % 2 != 0:  # Skip numbers that are not divisible by 2 (odd numbers)
        i += 1
        continue  # Skip to the next iteration
    print(i)
    i += 1  # Increment the counter
