"""
Name: Petr V.
Date: 10/24/24
Description: For loops
"""

# For loop style 1 - for i in range(stop)
# this prints 0 1 2 3 4 each on their own line
# the number in range(stop) is how many nums are printed
# starting at 0 and ending at stop-1

#common use: doing a known number of things
for i in range(5):
    print(i)

# For loop style 2 - for i in range (start, stop)
# this prints start, start + 1..., stop-1
# loop runs stop-start number of times

for i in range (2, 6):
    print(i, end = ' ')

for num_to_square in range(1, 6):
    print("x | x^2")
    print(f"{num_to_square} | {num_to_square**2}")
    print("-----------")

# For loop style 3 - for i in range(start, stop, step)
# this prints start, start + 1, iterates by step
for i in range(10, 100, -1):
    print(i, end = ' ')

# want: start at 12, count by 7s up to but not past 93
for i in range(12, 93, 7):
    print(i, end=' ')

total = 0
for i in range(5):
    total += int(input(print("enter a num: ")))
print(f"The average of those is: {str(total/5)}")