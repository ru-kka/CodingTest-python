#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int main(int argc, char** argv){
    int N;
    cin >> N;
    vector<int> time(N);

    for(int i=0; i < N; i++){
        cin >> time[i];
    }

    sort(time.begin(), time.end());

    vector<int> total_time(N);
    int sum = 0;
    for(int i=0; i < N; i++){
        total_time[i] = sum + time[i];
        sum += time[i];
    }

    cout << accumulate(total_time.begin(), total_time.end(), 0) << endl;
}
