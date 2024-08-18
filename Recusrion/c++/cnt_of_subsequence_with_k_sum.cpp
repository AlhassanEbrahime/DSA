#include<bits/stdc++.h>
using namespace std;

int  rec(int idx ,int sum , int tot , int n , int arr[])
{
    if (sum > tot)
    {
        return 0;
    }
    if(idx >= n)
    {
        if(sum == tot)
        {
            return 1;
        }
        return 0;
    }
    sum+=arr[idx];
    int l =rec(idx+1,sum,tot,n,arr);

    sum-=arr[idx];
    int r=rec(idx+1,sum,tot,n,arr);

    return l+r;


}
int main()
{  
    int n = 4;
    int a[] = {1,2,1,0};
    int tot = 2;
    cout<<rec(0,0,tot,n,a);
    
    return 0;

}