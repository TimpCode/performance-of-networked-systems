# load per job class
rohs = [0.14,0.04,0.02,1]

# required capacity
b = [3,4,5,1]

#total capacity
C = 5 

#number of jobs
K = 4

g = [0] * (2*C+1)
q = [0] * (C+1)

def kaufman_roberts(rohs, b, C, K):
    #Blocking probabilities
    B = [0]*K

    #calculating probabilities before normalizing
    for i in range(2*C+1):
        temp_sum = 0
        if i < C:
            g[i] = 0
        elif i == C:
            g[i] = 1
        elif i > C:
            for j in range(K):
                temp_sum += b[j]*rohs[j]*g[i-b[j]]
                g[i] = temp_sum*(1/(i-C))
    
    G = sum(g)

  #calculating probabilities after normalizing
    for k in range(C+1):
      q[k]= g[k + C] / G

  #calculating blocking probabilities
    for m in range(K):
      job_capacity = b[m]
      for i in range(C):
        if job_capacity-1 >= i:
          B[m]+=q[C-i]
    return B

print(kaufman_roberts(rohs, b, C, K))