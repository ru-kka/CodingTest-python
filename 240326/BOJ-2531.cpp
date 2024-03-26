#include <iostream>
#include <vector>
#include <set>

using namespace std;

int main(int argc, char** argv){
    int N, d, k, c;
    cin >> N >> d >> k >> c;

    vector<int> sushi(N);
    for(int i=0; i<N; i++){
        cin >> sushi[i];
    }

    int answer = 0;
    for(int i=0; i<N; i++){
        vector<int> s;
        if(i+(k-1) > N-1){
            s.insert(s.end(), sushi.begin() + i, sushi.end());
            s.insert(s.end(), sushi.begin(), sushi.begin() + k -(N - i));
        }else{
            s.insert(s.end(), sushi.begin() + i, sushi.begin() + i + k);
        }

        s.push_back(c);
        set<int> s_set(s.begin(), s.end());
        answer = max(int(s_set.size()), answer);
    }

    cout << answer << endl;

    return 0;
}