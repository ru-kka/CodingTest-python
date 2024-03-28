#include<iostream>
#include<vector>
#include<algorithm>
#include<cmath>

using namespace std;

int main(int argc, char** argv)
{
    int N, M, K;
    cin >> N >> M >> K;
    
    vector<int> weight(N);
    for(int i=0; i<N; i++){
        cin >> weight[i];
    }
    sort(weight.begin(), weight.end());
    
    vector<vector<int>> w_com;
    do{
        w_com.push_back(weight);
    }while(next_permutation(weight.begin(), weight.end()));

    long long answer = 10000000000LL;
    for(int i=0; i<w_com.size(); i++){
        int index = 0;
        long long candidate = 0;
        for(int j=0; j<K; j++){
            long long sum = 0;
            while(sum + w_com[i][index] <= M){
                sum += w_com[i][index];
                index += 1;
                index = index % N;
            }
            candidate += sum;
        }
        answer = min(answer, candidate);
    }
    cout << answer;
    return 0;
}