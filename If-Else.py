# Task
# Given an integer, n, perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of  to , print Not Weird
# If n is even and in the inclusive range of  to , print Weird
# If n is even and greater than , print Not Weird

# Input Format
# A single line containing a positive integer,n.

# Constraints
# 1 <= n <= 100

# Output Format
# Print Weird if the number is weird. Otherwise, print Not Weird.

# Sample Input 0
# 3
# Sample Output 0
# Weird

# Explanation 0
# n = 3
# n is odd and odd numbers are weird, so print Weird.

# Sample Input 1
# 24
# Sample Output 1
# Not Weird

# Explanation 1
# n = 24
# n > 20 and n is even, so it is not weird.



import sys


N = int(input().strip())

if N % 2 != 0:
    print("Weird")
else:
    if N >= 2 and N <= 5:
        print("Not Weird")
    elif N >= 6 and N <= 20:
        print("Weird")
    elif N > 20:
        print("Not Weird")
