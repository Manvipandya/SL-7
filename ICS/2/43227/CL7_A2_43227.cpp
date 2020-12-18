/*
	Assignment: 2
	Roll Number: 43227
	Batch: Q10
	Lab: CL7
*/

#include<bits/stdc++.h> 

using namespace std;

int inverse(int a, int m)
{
    int m0 = m, t, q;
    int x0 = 0, x1 = 1;
    if (m == 1)
       return 0;
    while (a > 1)
    {
        q = a / m;
        t = m;
        m = a % m, a = t;
        t = x0;
        x0 = x1 - q * x0;
        x1 = t;
    }
    if (x1 < 0) 
       x1 += m0;
    return x1; 
}

int solve(int num[], int rem[], int k)
{
    int product=1, result=0, other_product=0;
    for (int i = 0; i < k; i++)
        product *= num[i];
    for (int i = 0; i < k; i++)
    {
        other_product = product / num[i];
        result += rem[i] * inverse(other_product, num[i]) * other_product;
    }
    return result % product;
}
  

int main()
{
    int count=0, i=0;
    cout<<"Enter the number of elements: ";
    cin>>count;
    int num[count], rem[count];
    cout<<"Enter element followed by remainder."<<endl;
    for(i=0; i<count; i++)
    {
        cin>>num[i]>>rem[i];
    }
    int k = sizeof(num)/sizeof(num[0]); 
    cout << "Solution: x is " << solve(num, rem, k)<<endl; 
    return 0; 
} 

/*
Output

$ ./a.out
Enter the number of elements: 3
Enter element followed by remainder.
3 1
5 4
7 6
Solution: x is 34

*/