#include <iostream>

using namespace std;

int main(int argc, char** argv){
    int N;
    cin >> N;

    int answer = -1;
    int standard = N / 5;
    for(int i=standard; i>=0; i--){
        int cnt = i;
        int left = N - 5*i;
        if(left % 3 == 0){
            cnt += left / 3;
            answer = cnt;
            break;
        }
    }

    cout << answer;
}