#include<iostream>
#include<vector>
#include<algorithm>
#include<string>

using namespace std;

int main(int argc, char** argv)
{
    int N, M;
    cin >> N >> M;

    vector<string> name;
    for(int i=0; i<N; i++){
        string n;
        cin >> n;
        name.push_back(n);
    }
    sort(name.begin(), name.end());

    vector<vector<bool>> time(N);
    for(int i=0; i<N; i++){
        time[i] = {true, true, true, true, true, true, true, true, true};
    }

    for(int i=0; i<M; i++){
        string r;
        int s, t;
        cin >> r >> s >> t;

        int index = find(name.begin(), name.end(), r) - name.begin();
        for(int j=s; j<t; j++){
            time[index][j-9] = false;
        }
    }

    vector<vector<pair<int,int>>> answer;
    for(int i=0; i<N; i++){
        vector<pair<int, int>> room;
        bool flag = false;
        int begin = 0;
        for(int j=0; j<9; j++){
            if(time[i][j] == true){
                if(!flag){
                    flag = true;
                    begin = j+9;
                    if(j==8){
                        room.push_back({begin, 18});
                    }
                } else{
                    if(j==8){
                        room.push_back({begin, 18});
                    }
                }
            } else if(time[i][j] == false){
                if(!flag){
                    continue;
                } else{
                    flag = false;
                    room.push_back({begin, j+9});
                }
            }
        }
        answer.push_back(room);
    }

    for(int i=0; i<N; i++){
        cout << "Room " << name[i] << ":" << endl;
        if(answer[i].empty()){
            cout << "Not available" << endl;
        } else{
            cout << answer[i].size() << " available:" << endl;
            for(int j=0; j<answer[i].size(); j++){
                string str = "";
                if(answer[i][j].first == 9){
                    str += "09";
                } else{
                    str += to_string(answer[i][j].first);
                }
                str += '-';
                str += to_string(answer[i][j].second);
                cout << str << endl;
            }
        }
        if(i != (N-1)){
            cout << "-----" << endl;
        }
    }
    return 0;
}