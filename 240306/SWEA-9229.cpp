#include<iostream>

using namespace std;

int main(int argc, char** argv){
    int T;
    cin >> T;
    for(int test_case = 1; test_case <= T; test_case++){
        int N, M;
        cin >> N >> M;

        int snack[N];
        for(int i=0; i < N; i++){
            cin >> snack[i];
        }

        // 과자 2개씩 선택하는 모든 경우 탐색
        int answer = -1;
        for(int i=0; i<N-1; i++){
            for(int j=i+1; j<N; j++){
                int sum = snack[i] + snack[j];
                if(sum > answer and sum <= M){
                    answer = sum;
                }
            }
        }

        cout << '#' << test_case << ' ' << answer << endl;
    }
    return 0;
}