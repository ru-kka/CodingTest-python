#include<iostream>
#include<vector>

using namespace std;

int main(int argc, char** argv)
{
    int M, N, K;
    cin >> M >> N >> K;

    vector<int> secret_number(M);
    for(int i=0; i<M; i++){
        cin >> secret_number[i];
    }

    vector<int> user_number(M);
    for(int i=0; i<N; i++){
        cin >> user_number[i];
    }

    bool flag = false;
    for(int i=0; i<N-M+1; i++){
        int cnt = 0;
        for(int j=0; j<M; j++){
            if(secret_number[j] == user_number[i+j]){
                cnt += 1;
            }else{
                break;
            }
        }
        if(cnt == M){
            flag = true;
        }
    }

    if(flag){
        cout << "secret";
    }else{
        cout << "normal";
    }
    return 0;
}