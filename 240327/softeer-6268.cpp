#include<iostream>
#include <vector>
#include <string>

using namespace std;

int main(int argc, char** argv){
    vector<vector<int>> number(10);
    number[0] = {1, 1, 1, 0, 1, 1, 1};
    number[1] = {0, 0, 1, 0, 0, 0, 1};
    number[2] = {1, 0, 1, 1, 1, 1, 0};
    number[3] = {1, 0, 1, 1, 0, 1, 1};
    number[4] = {0, 1, 1, 1, 0, 0, 1};
    number[5] = {1, 1, 0, 1, 0, 1, 1};
    number[6] = {1, 1, 0, 1, 1, 1, 1};
    number[7] = {1, 1, 1, 0, 0, 0, 1};
    number[8] = {1, 1, 1, 1, 1, 1, 1};
    number[9] = {1, 1, 1, 1, 0, 1, 1};

    int T;
    cin >> T;
    for(int t=0; t<T; t++){
        string A, B;
        cin >> A >> B;

        int answer = 0;
        if(A.length() == B.length()){
            for(int position=0; position<A.length(); position++){
                for(int i=0; i<7; i++){
                    if(number[A[position] - '0'][i] != number[B[position] - '0'][i]){
                        answer += 1;
                    }
                }
            }
        } else if(A.length() > B.length()){
            for(int position=0; position<(A.length() - B.length()); position++){
                for(int i=0; i<7; i++){
                    if(number[A[position] - '0'][i] == 1){
                        answer += 1;
                    }
                }
            }
            A = A.substr(A.length() - B.length());
            for(int position=0; position<B.length(); position++){
                for(int i=0; i<7; i++){
                    if(number[A[position] - '0'][i] != number[B[position] - '0'][i]){
                        answer += 1;
                    }
                }
            }
        } else if(A.length() < B.length()){
            for(int position=0; position<(B.length() - A.length()); position++){
                for(int i=0; i<7; i++){
                    if(number[B[position] - '0'][i] == 1){
                        answer += 1;
                    }
                }
            }
            B = B.substr(B.length() - A.length());
            for(int position=0; position<A.length(); position++){
                for(int i=0; i<7; i++){
                    if(number[A[position] - '0'][i] != number[B[position] - '0'][i]){
                        answer += 1;
                    }
                }
            }
        }
        cout << answer << endl;
    }
   return 0;
}