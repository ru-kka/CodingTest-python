#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char** argv){
    int N, M;
    cin >> N >> M;

    vector<int> tree(N);
    for(int i=0; i<N; i++){
        cin >> tree[i];
    }

    int left = 0;
    int right = *max_element(tree.begin(), tree.end());

    int answer = 0;
    int candidate = 0;
    bool find = false;

    while(left <= right){
        int target = (left + right) / 2;

        long long length = 0;
        for(int i=0; i < N; i++){
            if(tree[i] > target){
                length += (tree[i] - target);
            }
        }

        if(length < M){
            right = target - 1;
        } else if(length > M){
            left = target + 1;
            candidate = target;
        } else if(length == M){
            answer = target;
            find = true;
            break;
        }
    }

    if(find == true){
        cout << answer;
    } else{
        cout << candidate;
    }
}