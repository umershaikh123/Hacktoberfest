#include <bits/stdc++.h>
using namespace std;
int sorting(int arr[],int n,int k){
   sort(arr,arr+n);
   int res=arr[k-1];
       return res;
}
int main() {
	int arr[]={7,10,4,3,20,15};
	int n=sizeof(arr)/sizeof(arr[0]);
	cout<<sorting(arr,n,3);
	return 0;
}
