from math import factorial

# declare variables acoording to assignment and calculations
states = [[0,0,0,0],[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,0,0,1],
        [0,1,0,1],[1,0,0,2],[0,0,0,2],[0,0,0,3],[0,0,0,4],[0,0,0,5]]
rohs = [0.14, 0.04, 0.02, 1]
required_capacity = [3,4,5,1]
capacity = 5

# calculate normalizing constant G
def calculate_normalizing_constant(states, rohs):
    # initialize temporal and final result variables
    sum = prod_sum = 0
    # loop through all states
    for state in states:
        # calculate partial product sum for each state
        for n, m in enumerate(state):
            if n == 0:
                prod_sum+=(rohs[n]**m)/factorial(m)
            else:
                prod_sum*=(rohs[n]**m)/factorial(m)
        # sum up all partial result to get G
        sum += prod_sum
        prod_sum = 0
    return sum

# Calculate the equilibruim distribution
def calculate_equi_distr(states, rohs):
    # Calculate G
    G = calculate_normalizing_constant(states, rohs)
    # make a dictionary to store results
    result_dict = {}
    for x, state in enumerate(states):
        # set the product sum to 0 for each new calculation
        prod_sum=0
        for n, m in enumerate(state):
            if n == 0:
                prod_sum+=(rohs[n]**m)/factorial(m)
            else:
                prod_sum*=(rohs[n]**m)/factorial(m)
        prod_sum = (1/G)*prod_sum
        result_dict[x]= (state,prod_sum)
    return result_dict

result = calculate_equi_distr(states, rohs)
for entry in result.values():
    print(f'For state {entry[0]} the value for pi is: {entry[1]}')
