#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int main(int argc, char** argv){
    int N;
    cin >> N;

    vector<float> score(N);
    for(int i=0; i<N; i++){
        cin >> score[i];
    }

    float M = *max_element(score.begin(), score.end());

    for(int i=0; i<N; i++){
        score[i] = (score[i] / M) * 100;
    }

    float answer = accumulate(score.begin(), score.end(), 0.0) / float(N);
    cout << answer;
}