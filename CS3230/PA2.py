import sys; 
input = sys.stdin.readline
x = input()
y = input()
def shortest_common_supersequence(str1: str, str2: str) -> str:
    m = len(str1)
    n = len(str2)
    
    # Initialize DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Reconstruct the SCS
    scs = []
    i, j = m, n
    
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            scs.append(str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            scs.append(str1[i - 1])
            i -= 1
        else:
            scs.append(str2[j - 1])
            j -= 1
    
    # Add the remaining characters from str1 or str2
    while i > 0:
        scs.append(str1[i - 1])
        i -= 1
    while j > 0:
        scs.append(str2[j - 1])
        j -= 1
    
    # Since we've built the SCS from the end to the start, reverse it
    return ''.join(reversed(scs))


print(shortest_common_supersequence(x, y))
        