#include<iostream>
#include<vector>

using namespace std;

int main(int argc, char** argv)
{
    int N, M, K;
    cin >> N >> M >> K;
    vector<int> n(N);
    vector<int> m(M);
    for(int i=0; i<N; i++){
        cin >> n[i];
    }
    for(int i=0; i<M; i++){
        cin >> m[i];
    }

    vector<vector<int>> dp(N, vector<int>(M, 0));
    int answer = 0;
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            if(n[i] == m[j]){
                if(0<=(i-1) and 0<=(j-1) and dp[i-1][j-1] != 0){
                    dp[i][j] = dp[i-1][j-1] + 1;
                    answer = max(answer, dp[i][j]);
                }else{
                    dp[i][j] = 1;
                    answer = max(answer, 1);
                }
            }
        }
    }
    cout << answer;
    return 0;
}