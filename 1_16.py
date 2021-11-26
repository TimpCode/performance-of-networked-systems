from math import factorial
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
    lambdas = [1,3,7,11,16]
    b = 1.5
    channels = N   

    # define values to store temporal and final result of the calculation
    lowest_blocking = 1
    total_blocking = 0
    
    # we enter a for loop that checks if the lowest blocking factor 
    # for a certain amount of channels is larger than 2,5%. 
    # In case it is, the number of channels is incremented by 1 and new blocking factor and its distribution
    # over the channels is calculated.
    while lowest_blocking > 0.025:
        # create a list containing all channel
        input = list(range(0,channels+1))
        # create instances of all combinations of cells, eg (0,0,0,0,0), (0,0,0,0,1) ... (59,59,59,59,59)
        all_combinations = combinations_with_replacement(input, 5)
        for combination in all_combinations:
            # create valid tuples of cells that can share channels
            N1 = (combination[0], combination[3])
            N2 = (combination[1], combination[4])
            N3 = combination[2]
            N4 = (combination[0], combination[4])
            N5 = (combination[1], combination[2], combination[3])
            # check that only valid combinations enter blocking calculation
            # if (max(N1)+max(N2)+N3) <= channels:
            if ((max(N1)+max(N2)+N3) <= channels) or ((max(N4)+sum(N5)) <= channels) or (sum(combination) <= channels):
                for x, N in enumerate(combination):
                    total_blocking+= (lambdas[x]/sum(lambdas))*erlang_b(lambdas[x],b,N)
                if total_blocking < lowest_blocking:
                    lowest_blocking = total_blocking
                    comb = combination
            total_blocking = 0
        channels+=1
    print(f'Lowest blocking is {lowest_blocking} for combination: {comb} and the frequency is {channels-1}')

calculate_min_b(60)
