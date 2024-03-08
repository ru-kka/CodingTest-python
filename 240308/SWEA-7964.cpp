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

        // 초기 point -1로 잡음
        int point = -1;
        int answer = 0;
        // 모든 도시 접근 가능하게 만들 때까지 while문 돌림
        while(point+D < N){
            // 현재 위치에서 제한 거리까지 1이 있는지 없는지 확인하는 flag
            bool flag = false;
            // 현재 위치에서 제한 거리만큼 먼 부분부터 1이 있는지 확인
            for(int i=point+D; i > point; i--){
                // 1이 있으면 point위치 해당 위치로 바꾸고
                // flag true로 바꿈
                if(v[i] == 1){
                    point = i;
                    flag = true;
                }
            }

            // 현재 위치에서 제한 거리 내 1이 없으면
            // 제한 거리만큼 떨어진 곳에 차원 관문 추가로 건설
            if(flag == false){
                point += D;
                v[point] = 1;
                answer++;
            }
        }

        cout << '#' << test_case << ' ' << answer << endl;
	}
	return 0;
}