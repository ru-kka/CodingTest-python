#include<iostream>

using namespace std;

// 탐색해야하는 8개 구역
int dx[] = {-1, -1, -1, 0, 0, 1, 1, 1};
int dy[] = {-1, 0, 1, -1, 1, -1, 0, 1};

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin >> T;
	for(test_case = 1; test_case <= T; ++test_case)
	{
        int N;
        cin >> N;

        // 2차원 행렬 입력받기
        char matrix[N][N];
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                cin >> matrix[i][j];
            }
        }

        int answer = 0;
        for(int i=1; i<N-1; i++){
            for(int j=0; j<N-1; j++){
                int cnt = 0;
                for(int k=0; k<8; k++){
                    if(matrix[i+dx[k]][j+dy[k]] == 'W'){
                        cnt += 1;
                    }
                }
                if(answer < cnt){
                    answer = cnt;
                }
            }
        }
        cout << '#' << test_case << ' ' << answer << endl;
	}
	return 0;
}