def rec(idx , arr: list[int], sum , tot, n):
    
    if sum > tot:
        return 0
    if idx>=n:
        if sum == tot:
            return 1
        return 0
    
    sum+=arr[idx]
    l = rec(idx+1, arr, sum, tot, n)
    sum-=arr[idx]
    r = rec(idx+1, arr, sum, tot, n)
    
    return l + r


if __name__ == "__main__":
    
    a = [1,2,1]
    tot=2
    n = 3
    print(rec(0,a,0,tot,n))
    