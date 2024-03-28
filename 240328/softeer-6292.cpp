#include<iostream>

using namespace std;

long long number = 1000000007;

long long recur(long long p, long long n){
    if(n == 1){
        return p;
    } 
    long long a;
    a = recur(p, n/2);
    a = (a*a) % number;
    if(n%2 == 1){
        a = (a*p) % number;
    }
    return a;
}

int main(int argc, char** argv)
{
    long long K, P, N;
    cin >> K >> P >> N;

    long long result;
    result = recur(P, 10*N);

    cout << (result*K) % number;
    return 0;
}