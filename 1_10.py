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

# calculate subset of states per j-class
def calculate_state_subset(states, required_capacity, capacity):
    # initialize empty list to store lists of subsets for later usage
    subset = []
    # iterate through each j-class
    for i, cap in enumerate(required_capacity):
        subset.append([])
        # check for each state if it meets the requirements to become part of subset
        for state in states:
            sum = 0
            for n, m in enumerate(state):
                sum+= required_capacity[n]*m
            if sum <= (capacity - cap):
                if state not in subset:
                    subset[i].append(state)
    return(subset)

# calcualte blocking probability
def blocking_probability(states, required_capacity, capacity, rohs):
    # build subsets from existing states in markov chain
    subsets = calculate_state_subset(states, required_capacity, capacity)
    counter = 1
    # calculate normalizing constant for all states
    normalizing_const_all = calculate_normalizing_constant(states, rohs)
    for set in subsets:
        # calculate normalizing constant for the current subset
        normalizing_const_subset = calculate_normalizing_constant(set, rohs)
        # calculate blocking probability
        blocking_probability = 1 - (normalizing_const_subset/normalizing_const_all)
        print(f'blocking probability for j-class {counter} is: {blocking_probability}')
        counter += 1

subsets = (calculate_state_subset(states, required_capacity, capacity))
for j , set in enumerate(subsets):
    print(f'subset for j-class: {j+1} is {set}')

blocking_probability(states, required_capacity, capacity, rohs)