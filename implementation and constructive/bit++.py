# You're given a programme in language Bit++. The initial value of x is 0. Execute the programme and find its final value (the value of the variable when this programme is executed).

# Input:
# The first line contains a single integer n (1 ≤ n ≤ 150) — the number of statements in the programme.

# Next n lines contain a statement each. Each statement contains exactly one operation (++ or --) and exactly one variable x (denoted as letter «X»).Thus, there are no empty statements. The operation and the variable can be written in any order.

# Output:
# Print a single integer — the final value of x.


# Step 1: Input: Number of statements (n)
n = int(input())

# Step 2: Initialize x to 0
x = 0

# Step 3: Process each statement
for _ in range(n):
    statement = input()  # Read a statement (e.g., X++ or --X)
    
    # Step 4: Determine the operation and update x
    if "++" in statement:  # Check if the operation is increment
        x += 1
    elif "--" in statement:  # Check if the operation is decrement
        x -= 1

# Step 5: Output the final value of x
print(x)
