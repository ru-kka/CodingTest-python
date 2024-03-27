#include<iostream>
#include<vector>

using namespace std;

int main(int argc, char** argv)
{
    int N, M;
    cin >> N >> M;

    vector<int> standard = {0};
    for(int i=0; i<N; i++){
        int length, speed;
        cin >> length >> speed;
        for(int j=0; j<length; j++){
            standard.push_back(speed);
        }
    }

    int answer = 0;
    int length_start = 1;
    for(int i=0; i<M; i++){
        int length, speed;
        cin >> length >> speed;
        for(int j=length_start; j<(length_start+length); j++){
            answer = max(answer, speed - standard[j]);
        }
        length_start += length;
    }
    cout << answer;
    return 0;
}