# Luke Skywalker gave Chewbacca an integer number x. Chewbacca isn't good at numbers but he loves inverting digits in them. Inverting digit t means replacing it with digit 9 - t.
# Help Chewbacca to transform the initial number x to the minimum possible positive number by inverting some (possibly, zero) digits. The decimal representation of the final number shouldn't start with a zero.

# Input:
# The first line contains a single integer x (1 ≤ x ≤ 1018) — the number that Luke Skywalker gave to Chewbacca.

# Output:
# Print the minimum possible positive number that Chewbacca can obtain after inverting some digits. The number shouldn't contain leading zeroes.

# Examples
# input
# 27
# output
# 22


x = input()
result = []

for i, digit in enumerate(x):  
    d = int(digit)
    
    if d > 4:
        if i == 0 and d == 9:
            result.append(str(d))
        else:
            result.append(str(9 - d))
    else:
        result.append(str(d))
      
print(''.join(result))
