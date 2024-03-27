#include<iostream>

using namespace std;

int main(int argc, char** argv)
{
    int N;
    cin >> N;

    int n = 2;
    for(int i=0; i<N; i++){
        n = 2*n - 1;
    }

    cout << n*n;
    
    return 0;
}