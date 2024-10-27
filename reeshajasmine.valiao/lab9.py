# Function to print a right-angled triangle of numbers
rows = int(input("Enter the number of rows: "))
# Initialize a counter
num = 1
# Outer loop for each row
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(num, end=' ')
        num += 1
    print ()