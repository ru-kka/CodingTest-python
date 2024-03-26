#include <iostream>
#include <vector>

using namespace std;

vector<int> status(1);

void switch_number(int num){
    if(status[num] == 1){
        status[num] = 0;
    } else if(status[num] == 0){
        status[num] = 1;
    }
}

int main(int argc, char** argv){
    int N;
    cin >> N;

    for(int i=0; i < N; i++){
        int num;
        cin >> num;
        status.push_back(num);
    }

    int M;
    cin >> M;
    for(int i=0; i < M; i++){
        int sex, number;
        cin >> sex >> number;

        if(sex == 1){
            for(int j=1; j <= N/number; j++){
                switch_number(number * j);
            }
        } else if(sex == 2){
            switch_number(number);
            int left = number - 1;
            int right = number + 1;
            while(left >= 1 and right <= N){
                if(status[left] == status[right]){
                    switch_number(left);
                    switch_number(right);
                    left -= 1;
                    right += 1;
                }else{
                    break;
                }
            }
        }
    }

    for(int i = 1; i < N+1; i++){
        cout << status[i] << " ";
        if(i % 20 == 0){
            cout << endl;
        }
    }
}