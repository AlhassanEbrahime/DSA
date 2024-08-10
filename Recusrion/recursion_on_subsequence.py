def rec(idx ,ds:list[int] , a:list[int] , n ):
    
    if idx >= n:
        print(*ds)
        return
    
    ds.append(a[idx])
    rec(idx+1 , ds ,a ,n)
    ds.pop()
    rec(idx+1 , ds ,a ,n)



if __name__ == "__main__":
     
    a = [3,1,2]
    n = 3
    ds = []
    rec(0 , ds , a , n)
     