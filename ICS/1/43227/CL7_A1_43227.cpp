/*
	Assignment: 1
	Roll Number: 43227
	Batch: Q10
	Lab: CL7
*/

#include<bits/stdc++.h>

using namespace std;

int gcd(int m, int n)
{
	if(n==0)
		return m;
	else
		return gcd(n, m%n);
}

unsigned long long int modular_exponentiation(unsigned long long int value, unsigned long long int exponent, unsigned long long int base)
{
	int i=0;
	unsigned long long result=1;
	for(i=0; i<exponent; i++)
	{
		result *= value%base;
		result = result%base;
	}
	return result;
}

int main()
{
	string plaintext, encrypted_text, decrypted_text;
	unsigned long long int p, q, d, e, n, t, i, enc, dec;
	p = 10433;
	q = 11617;
	n = p * q;
	t = (p-1) * (q-1);
	cout<<"Enter plaintext: ";
	cin>>plaintext;
	int *plain = new int[plaintext.length()];
	for(i=2; i<t; i++)
	{
		if(gcd(i, t) == 1)
		{
			e = i;
			break;
		}
	}
	while(1)
	{
		if((i*t + 1) % e == 0)
		{
			d = (i*t + 1) / e;
			break;
		}
		i++;
	}
	cout<<endl<<"Prime number 1: "<<p;
	cout<<endl<<"Prime number 2: "<<q;
	cout<<endl<<"Public key: "<<e;
	cout<<endl<<"Private key: "<<d;
	for(i=0; i<plaintext.length(); i++)
	{
		enc = modular_exponentiation(plaintext[i], e, n);
		encrypted_text.append(1, (char)enc);
		dec = modular_exponentiation(enc, d, n);
		decrypted_text.append(1, (char)dec);
	}
	cout<<endl<<"Encrypted Text: "<<encrypted_text;
	cout<<endl<<"Decrypted Text: "<<decrypted_text;
	cout<<endl;
	return 0;
}

/*
Output

Enter plaintext: hello

Prime number 1: 10433
Prime number 2: 11617
Public key: 5
Private key: 169649357
Encrypted Text: �ggD
Decrypted Text: hello

*/
