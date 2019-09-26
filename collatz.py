# The number we will perform the collatz operation on.
n = 20 

# Keep looping until we reach number 1.
# Note: This is assumes the collatz conjecture is true.
while n != 1:
    # Print the current value of n.
    print (n)
    #Check is n is even.
    if n % 2 == 0:
    # If n is even, divede it by two.
        n = n / 2
    else:
    # If n is odd, multiply it by three and add 1.
        n = (3 * n) + 1

# Finally, print the 1.
print (n)            
