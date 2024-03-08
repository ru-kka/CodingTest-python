#include<iostream>
#include<vector>

using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin>>T;
	for(test_case = 1; test_case <= T; ++test_case)
	{
        int N, D;
        cin >> N >> D;

        vector<int> v(N);
        for(int i=0; i<N; i++){
            cin >> v[i];
        }

        int cnt = 0;
        int answer = 0;
        for(int i=0; i<N; i++){
            if(v[i] == 1){
                cnt = 0;
            } else if(v[i] == 0){
                cnt += 1;
                if(cnt == D){
                    answer += 1;
                    cnt = 0;
                }
            }
        }

        cout << '#' << test_case << ' ' << answer << endl;
	}
	return 0;
}