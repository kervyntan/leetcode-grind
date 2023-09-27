# https://codewindow.in/nagarro-question-solved-the-card-game-codewindow-in/
import sys

def minsubarraysum(n, a):
    min_sum = sys.maxsize
    curr_sum = 0
    for i in range(0, n):
        curr_sum = curr_sum + a[i]
        if curr_sum < min_sum:
            min_sum = curr_sum
        if curr_sum > 0:
            curr_sum  = 0
    return min_sum
    

n = int(input())
arr = list(map(int, input().split(" ")))
s = sum(arr)
min_sum = minsubarraysum(n, arr)
ans = s + min_sum * (-2)
print(ans)