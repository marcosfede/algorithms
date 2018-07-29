//Merge sort
//time complexity: O(n log(n))
#include<iostream>
#define SIZE(x) sizeof(x)/sizeof(x[0])
using namespace std;

//merging the two sorted array l[] and r[] into a[]
//time complexity: O(n)
void merge(int l[],int r[],int a[],int nl, int nr, int na){
	int i=0,j=0,k=0;
	//when both l[] and r[] array has element
	while(i<nl && j<nr){
		if(l[i]<=r[j]){
			a[k]=l[i];
			i++; k++;
		}
		else if(l[i]>r[j]){
			a[k]=r[j];
			j++; k++;
		}
	}
	//when r[] array has no element to merge
	while(i<nl){
		a[k]=l[i];
		i++; k++;
	}
	//when l[] array has no element to merge
	while(j<nr){
		a[k]=r[j];
		j++; k++;
	}
}

//divide array into two part
void mergeSort(int a[],int n){
	//our recursive base case
	if(n<=1) return;
	int mid=n/2;
	int left[mid],right[n-mid];

	for(int i=0;i<mid;i++)
		left[i]=a[i];

	for(int i=mid;i<n;i++)
		right[i-mid]=a[i];

	//merge sort both the halves recursively
	mergeSort(left,SIZE(left));
	mergeSort(right,SIZE(right));
	//place both halves together
	merge(left,right,a,SIZE(left),SIZE(right),n);
}


int main(){
	int arr[]={3,5,7,2,7,4,32,65,76,8,45,567,87,67,4,3,3};
	int n= SIZE(arr);
	mergeSort (arr,n);
	for(int i=0;i<n;i++)
		cout<<arr[i]<<" ";
	cout<<endl;
	return 0;
}
