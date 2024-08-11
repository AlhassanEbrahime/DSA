#include<bits/stdc++.h>
using namespace std;
/*
this function for retrung any subsequence with a specific sum
*/
bool rec_any(int idx , vector<int>&ds ,int sum , int tot , int n , int arr[])
{
    if(idx >= n)
    {
        if(sum == tot)
        {
            for (auto it : ds)
            {
                cout<<it<<" ";
            }
            cout<<endl;
            return true;
        }
        return false;
    }
    ds.push_back(arr[idx]); //take
    sum+=arr[idx];
    if(rec_any(idx+1,ds,sum,tot,n,arr) == true){
        return true;
    }

    ds.pop_back();  //not take
    sum-=arr[idx];
    if(rec_any(idx+1,ds,sum,tot,n,arr) == true)
    {
        return true;
    }

    return false;


}


/*
this function for printing all subsequences with a specific sum
*/

void rec(int idx , vector<int>&ds ,int sum , int tot , int n , int arr[])
{
    if(idx >= n)
    {
        if(sum == tot)
        {
            for (auto it : ds)
            {
                cout<<it<<" ";
            }
            cout<<endl;
        }
        return;
    }
    ds.push_back(arr[idx]); //take
    sum+=arr[idx];
    rec(idx+1,ds,sum,tot,n,arr);
    ds.pop_back();  //not take
    sum-=arr[idx];
    rec(idx+1,ds,sum,tot,n,arr);


}
int main()
{  
    int n = 4;
    int a[] = {1,2,1,0};
    int tot = 2;
    vector<int>ds;
    rec_any(0,ds,0,tot,n,a);

}