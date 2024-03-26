#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char** argv){
    vector<string> word;
    for(int i=0; i<4; i++){
        string w;
        cin >> w;
        word.push_back(w);
    }

    string first = word[0] + word[1];
    string second = word[2] + word[3];

    long long answer = stoll(first) + stoll(second);

    cout << answer;
}