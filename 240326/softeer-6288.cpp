#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char** argv){
    int W, N;
    cin >> W >> N;

    vector<pair<int, int>> type;
    for(int i=0; i<N; i++){
        int m, p;
        cin >> m >> p;
        type.push_back({m, p});
    }

    sort(type.begin(), type.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
        return a.second > b.second;
    });

    int weight = 0;
    int answer = 0;
    for(int i=0; i<N; i++){
        if(weight + type[i].first <= W) {
            weight += type[i].first;
            answer += type[i].first * type[i].second;
        } else {
            answer += (W - weight) * type[i].second;
            break;
        }
    }

    cout << answer;

    return 0;
}

// int main(int argc, char** argv){
//     int W, N;
//     cin >> W >> N;

//     vector<vector<int>> type(N);
//     for(int i=0; i<N; i++){
//         int m, p;
//         cin >> m >> p;
//         type[i].push_back(m);
//         type[i].push_back(p);
//     }

//     sort(type.begin(), type.end(), [](const vector<int> a, const vector<int> b) {
//         return a[1] > b[1];
//     });

//     int weight = 0;
//     int answer = 0;
//     for(int i=0; i<N; i++){
//         if(weight + type[i][0] <= W) {
//             weight += type[i][0];
//             answer += type[i][0] * type[i][1];
//         } else {
//             answer += (W - weight) * type[i][1];
//             break;
//         }
//     }

//     cout << answer;

// }