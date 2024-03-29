#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char**argv){
    int n;
    cin >> n;

    vector<int> dp{0, 1};
    for(int i=2; i<n+1; i++){
        dp.push_back(dp[i-2] + dp[i-1]);
    }

    cout << dp[n];
    return 0;
}