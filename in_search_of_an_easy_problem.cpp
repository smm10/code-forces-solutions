#include<iostream>

using namespace std;

int main(){

int n;
cin>>n;
int sum;
int temp;

int arr[n];

for(int i=0;i<n;i++)
{
cin>>arr[i];


}

for(int j=0;j<n;j++)
{
if(arr[j]==1)
{
    cout<<"HARD";
    return 0;

}

}

cout<<"EASY";






return 0;



}
