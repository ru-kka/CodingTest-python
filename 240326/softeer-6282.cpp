#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

vector<int> dx = {-1, 1, 0, 0};
vector<int> dy = {0, 0, -1, 1};

// bfs
// 함수 불러올 때 matrix, N 인자로 같이 가지고 옴
// matrix 앞에 & 붙여서 matrix 수정 가능하게함
int bfs(int x, int y, vector<vector<int>>& matrix, int N){
    // queue, pair사용
    queue<pair<int, int>> q;
    // pair 넣을 때 이와 같이 사용
    q.push({x, y});
    int cnt = 1;
    // queue가 비었는지로 while문 돌림
    while(!(q.empty())){
        // queue에서 front로 확인
        pair<int, int> p = q.front();
        // queue에서 이거는 그냥 pop만 수행함
        q.pop();
        for(int i=0; i<4; i++){
            int nx = p.first + dx[i];
            int ny = p.second + dy[i];
            // 조건문 유의
            if(nx >= 0 and nx < N and ny >= 0 and ny < N and matrix[nx][ny] == 1){
                matrix[nx][ny] = 0;
                cnt += 1;
                q.push({nx, ny});
            }
        }
    }

    return cnt;
}

int main(int argc, char** argv){
    int N;
    cin >> N;

    // 2차원 백터
    vector<vector<int>> matrix(N);
    for(int i=0; i<N; i++){
        string row;
        cin >> row;
        
        vector<int> l;
        // 문자일 때는 이렇게 해서 정수로 바꿔서 넣을 수 있음
        // 문자열이면 stoi
        for(int j=0; j<row.length(); j++){
            l.push_back(row[j] - '0');
        }
        // matrix를 2차원으로 선언했으니 해당 row 이렇게 정해줄 수 있음
        matrix[i] = l;
    }

    vector<int> answer;
    for(int x=0; x<N; x++){
        for(int y=0; y<N; y++){
            if(matrix[x][y] == 1){
                matrix[x][y] = 0;
                answer.push_back(bfs(x, y, matrix, N));
            }
        }
    }

    // vector 오름차순 정렬
    sort(answer.begin(), answer.end());
    // vector 크기 확인 방법
    cout << answer.size() << endl;
    for(int i=0; i<answer.size(); i++){
        cout << answer[i] << endl;
    }
}