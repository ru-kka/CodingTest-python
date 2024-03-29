#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char** argv){
    int N;
    cin >> N;

    vector<int> A(N);
    for(int i=0; i<N; i++){
        cin >> A[i];
    }
    vector<int> B(N);
    for(int i=0; i<N; i++){
        cin >> B[i];
    }

    sort(A.begin(), A.end());
    sort(B.begin(), B.end(), greater<int>());

    int answer = 0;
    for(int i=0; i<N; i++){
        answer += A[i] * B[i];
    }
    cout << answer;

    return 0;
}