# Calculator for Erlang B blocking probability

from math import factorial

def erlang_b(l, b, N):
    sum = 1
    for x in range(1,N+1):
        sum+= ((l*b)**x)/factorial(x)
    blocking = (((l*b)**N)/factorial(N))/sum
    return blocking

print(erlang_b(0.25, 4, 5))
