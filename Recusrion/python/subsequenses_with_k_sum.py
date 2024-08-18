"""
this function for retrung any subsequence with a specific sum
"""
def rec_any(idx , ds: list[int] , arr: list[int], sum , tot, n):
    
    if idx>=n:
        if sum == tot:
            print (*ds)
            return True
        
        return False
    
    ds.append(arr[idx])
    sum+=arr[idx]
    if  rec_any(idx+1, ds, arr, sum, tot, n) == True:
        return True
    
    ds.pop()
    sum-=arr[idx]
    if  rec_any(idx+1, ds, arr, sum, tot, n) == True:
        return True
    
    
    return False
    
    
"""
this function for printing all subsequences with a specific sum
"""
def rec(idx , ds: list[int] , arr: list[int], sum , tot, n):
    
    if idx>=n:
        if sum == tot:
            print (*ds)
        return 
    
    ds.append(arr[idx])
    sum+=arr[idx]
    rec(idx+1, ds, arr, sum, tot, n)
    ds.pop()
    sum-=arr[idx]
    rec(idx+1, ds, arr, sum, tot, n)

            

if __name__ == "__main__":
    
    a = [1,2,1]
    tot=2
    n = 3
    ds = []
    rec_any(0,ds,a,0,tot,n)