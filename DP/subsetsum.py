def subsetsum(arr,sum,n):
    t = [False]*(n+1)
    for i in range(n+1):
        t[i] = [False]*(sum+1)

    for i in range(n+1):
        t[i][0] = True

    for i in range(n+1):
        for j in range(sum+1):
            if arr[i-1]<=sum:
                t[i][j] = t[i-1][j-arr[i-1]] or t[i-1][j]
            else:
                t[i][j] = t[i-1][j]

    return t[n][sum]
    


arr= [8,2,4,6]
sum = 2
n = len(arr)
print(subsetsum(arr, sum, n))