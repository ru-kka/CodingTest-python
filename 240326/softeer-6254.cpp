#include<iostream>
#include<string>

using namespace std;

int main(int argc, char** argv)
{
    int answer = 0;
    for(int i=0; i<5; i++){
        string start, finish;
        cin >> start >> finish;

        int start_hour = stoi(start.substr(0,2));
        int start_minute = stoi(start.substr(3));
        int finish_hour = stoi(finish.substr(0,2));
        int finish_minute = stoi(finish.substr(3));

        if(start_minute > finish_minute){
            answer += (finish_hour - start_hour - 1) * 60;
            answer += 60 + finish_minute - start_minute;
        } else{
            answer += (finish_hour - start_hour) * 60;
            answer += finish_minute - start_minute;
        }
    }
    cout << answer;
    
   return 0;
}