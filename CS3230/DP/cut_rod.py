import math

# p -> array of prices for cutting at each point of the rod
# n -> length of RHS remainder of rod after each cut (begins with the length of the rod)
def cut_rod_naive(p, n):
    if n == 0:
        return 0
    
    max_revenue = -math.inf
    for i in range(1, n):
        max_revenue = max(max_revenue, p[i] + cut_rod_naive(p, n-i))
    
    return max_revenue

import math

def cut_rod_memoised(p, n):
    r = [-math.inf] * (n + 1)  # Adjusted to include n + 1 elements
    return cut_rod_memoised_helper(p, n, r)

def cut_rod_memoised_helper(p, n, r):
    if r[n] >= 0:  # solution present for rod of length n
        return r[n]
    if n == 0:
        q = 0
    else:
        q = -math.inf
        for i in range(1, n + 1):
            if i <= len(p): 
                q = max(q, p[i - 1] + cut_rod_memoised_helper(p, n - i, r))
    
    r[n] = q  # Memoise the solution value for length n  
    return q

def cut_rod_memoised_bottom_up(p, n):
    # initialize table
    r = [0] * (n + 1) 
    
    for i in range(1, n + 1):
        max_revenue = -math.inf
        for j in range(1, i + 1): # i is the position of first cut
            if j <= len(p): 
                max_revenue = max(max_revenue, p[j - 1] + r[i - j])
        r[i] = max_revenue
    
    return r[n]
    
# print(cut_rod_memoised([1, 5, 8, 9, 10, 17, 17, 20, 24, 30], 10))
print(cut_rod_memoised_bottom_up([1, 5, 8, 9, 10, 17, 17, 20, 24, 30], 10))
    
