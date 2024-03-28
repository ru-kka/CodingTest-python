#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main(int argc, char** argv)
{
    int N;
    cin >> N;
    vector<int> rock(N);
    for(int i=0; i<N; i++){
        cin >> rock[i];
    }

    vector<int> dp(N, 1);
    for(int i=1; i<N; i++){
        int find = 0;
        for(int j=0; j<i; j++){
            if(rock[i] > rock[j]){
                find = max(find, dp[j]);
            }
        }
        dp[i] = find + 1;
    }

    int answer = *max_element(dp.begin(), dp.end());
    cout << answer;
    return 0;
}