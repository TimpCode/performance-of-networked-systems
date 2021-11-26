# Calculator for Erlang B blocking probability

from math import factorial

# calculates erlang b blocking factor according to the formula from the slides. 
def erlang_b(l, b, N):
    sum = 1
    for x in range(1,N+1):
        sum+= ((l*b)**x)/factorial(x)
    blocking = (((l*b)**N)/factorial(N))/sum
    return blocking*100

# calculate amount of video cards required based on given blocking factor
def calculate_vc(blocking_factor):
    vc = 0
    while erlang_b(0.25,4, vc*5) >= blocking_factor:
        vc+=1
    return vc

# amounts required for blocking factor of 0.1%
print(calculate_vc(0.1))

# amounts required for blocking factor of 0.01%
print(calculate_vc(0.01))