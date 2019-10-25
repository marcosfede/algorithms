#include <bits/stdc++.h>
using namespace std;

void bubblesort(int arr[],int n)
{
    for(int i=0;i<n-1;i++)
    {
        for(int j=i;j<n;j++)
        {
            if(arr[i]>arr[j])
            {
                int temp=arr[i];
                arr[i]=arr[j];
                arr[j]=temp;
            }
        }
    }
}

int main() {
    int arr[]={1, 5, 65, 23, 57, 1232, -1, -5, -2, 242, 100,
         4, 423, 2, 564, 9, 0, 10, 43, 64, 32, 1, 999};
    cout<<"Before Sorting : "<<endl;
    for(int i=0;i<23;i++)
    cout<<arr[i]<<" ";
    cout<<endl;
    bubblesort(arr,23);
    cout<<"After Sorting : "<<endl;
    for(int i=0;i<23;i++)
    cout<<arr[i]<<" ";
}
