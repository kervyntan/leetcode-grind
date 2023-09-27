# def CalculateTime(W, wt, val, n):
#     if n == 0 or W == 0:
#         return 0

#     if (wt[n-1] > W):
#         return CalculateTime(W, wt, val, n-1)
#     else:
#         return max(val[n-1] + CalculateTime(W-wt[n-1], wt, val, n-1), CalculateTime(W, wt, val, n-1))
    
# https://codewindow.in/nagarro-question-solved-literary-competition-codewindow-in/
def CalculateTime(n, W, wt, val):
    if n == 0 or W == 0:
        return 0

    if (wt[n-1] > W):
        return CalculateTime(n - 1, W, wt, val)
    else:
        return max(val[n-1] + CalculateTime(n - 1, W-wt[n-1], wt, val), CalculateTime(n - 1, W, wt, val))



n = int(input())
W = int(input())
val = list(map(int, input().split(" ")))
wt = list(map(int, input().split(" ")))
print(CalculateTime(n, W, wt, val))