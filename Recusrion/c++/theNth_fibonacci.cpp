#include<bits/stdc++.h>
using namespace std;
int fib(int i , int n)
{
     if (i<=n)
     {
        return n;
     }

    int last = fib(i-1 , n);
    int sec_last = fib (i-2 , n);

    return last + sec_last;
}
int main()
{
    int n;
    cin>>n;
}

