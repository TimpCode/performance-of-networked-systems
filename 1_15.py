from math import comb, factorial
from itertools import permutations, combinations_with_replacement

# function to calculate erlang B
def erlang_b(l, b, N):
    sum = 1
    for x in range(1,N+1):
        sum+= ((l*b)**x)/factorial(x)
    blocking = (((l*b)**N)/factorial(N))/sum
    return blocking

#function to calculate minimal blocking factor
def calculate_min_b(N):

    # variables as defined in the assignment
    lambdas = [1,20,7,20,16]
    b = 1.5
    channels = N

    # create a list containing all channels
    input = list(range(0,N+1))

    # define values to store temporal and final result of the calculation
    lowest_blocking = 1
    total_blocking = 0

    # create instances of all combinations of cells, eg (0,0,0,0,0), (0,0,0,0,1) ... (59,59,59,59,59)
    all_combinations = combinations_with_replacement(input, 5)
    for combination in all_combinations:
        # create valid combinations of cells that can share frequencies
        N1 = (combination[0], combination[3]) #cells 1,4
        N2 = (combination[1], combination[4]) #cells 2,5
        N3 = combination[2] #cell 3
        N4 = (combination[0], combination[4]) #cells 1,5
        N5 = (combination[1], combination[2], combination[3]) #cells 2,3,4
        # check that only valid combinations enter blocking calculation. 
        # The total amount can't exceed the set number of channels, 60 in this case.
        # However, different compositions exist (each is one of the conditions)
        if ((max(N1)+max(N2)+N3) <= channels):
            # ((max(N4)+sum(N5)) <= channels) or \
            # (sum(combination) <= channels):
            # calculate for each number of channels in the valid combination the blocking probability and multiply with normalization
            for x, N in enumerate(combination):
                total_blocking+= (lambdas[x]/sum(lambdas))*erlang_b(lambdas[x],b,N)
            # check if a new lowest blocking probability was found
            if total_blocking < lowest_blocking:
                lowest_blocking = total_blocking
                comb = combination
        total_blocking = 0
    print(f'Lowest blocking is {lowest_blocking} for combination: {comb},\
    the sum of all frequencies is {sum(comb)}')
   
calculate_min_b(60)