#include<iostream>

using namespace std;

int main(int argc, char** argv)
{
    long long number = 1000000007;

    long long K, P, N;
    cin >> K >> P >> N;

    long long num = K;
    for(int i=0; i<N; i++){
        num *= P;
        if(num >= number){
            num = num % number;
        }
    }
    cout << num;
    return 0;
}