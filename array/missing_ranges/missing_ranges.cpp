#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int arr[]={10,12,11,15};
    cout<<"Input : ";
    for(int x:arr)
        cout<<x<<" ";
    cout<<endl;
    sort(arr,arr+4);
    int low=arr[0];
    int high=arr[3];
    set<int>s;
    vector<int>v;
    for(int i=0;i<4;i++)
        s.insert(arr[i]);
    for(int i=low;i<high;i++)
    {
        if(s.find(i)==s.end())
            v.push_back(i);
    }
    for(int x:v)
        cout<<x<<endl;

    return 0;
}
