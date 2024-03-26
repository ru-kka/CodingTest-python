#include <iostream>
#include <string>

using namespace std;

int main(int argc, char** argv){
    string str;
    getline(cin, str);

    int answer = 0;
    for(int i=0; i<str.length(); i++){
        if(str[i] == ' '){
            answer += 1;
        }
    }

    if(str[0] == ' '){;
        answer -= 1;
    }
    if(str[str.length() - 1] == ' '){
        answer -= 1;
    }

    cout << answer + 1;
}