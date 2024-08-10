#include<bits/stdc++.h>
using namespace std;
void rec(int idx , vector<int>&ds,int arr[] ,int n)
{  
     if(idx>=n)
     {
        for (auto it : ds)
        {
            cout<<it<<" ";
        }
        cout<<endl;
        return;
     }

     ds.push_back(arr[idx]);
     rec(idx+1,ds,arr,n);
     ds.pop_back();
     rec(idx+1,ds,arr,n);


}
int main(){
     
     int a[]={3,1,2};
     int n = 3;
     vector<int> ds;

     rec(0,ds,a,n);





}

