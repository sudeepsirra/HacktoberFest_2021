def unbknapsack(val,wt,w,n):
    t = [-1]*(n+1)
    for i in range(n+1):
        t[i] = [-1]*(w+1)

    for i in range(n+1):
        for j in range(w+1):
            if i==0 or j==0:
                t[i][j] = 0
            elif wt[i-1]<=j:
                t[i][j] = max(val[i-1]+t[i][j-wt[i-1]], t[i-1][j])
            else:
                t[i][j] = t[i-1][j]
    return t[n][w]
    

val=[10,8,6]
wt=[5,5,5]
w=240
n = len(wt)
print(unbknapsack(val, wt, w, n))
