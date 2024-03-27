#include<iostream>
#include<vector>

using namespace std;

int main(int argc, char** argv)
{
    vector<int> gear(8);
    for(int i=0; i<8; i++){
        int number;
        cin >> number;
        gear[i] = number;
    }

    bool asc = true;
    bool des = true;

    for(int i=0; i<7; i++){
        if(gear[i+1] - gear[i] != 1){
            asc = false;
        }
        if(gear[i+1] - gear[i] != -1){
            des = false;
        }
    }

    if(asc == true){
        cout << "ascending";
    }
    if(des == true){
        cout << "descending";
    }
    if(asc == des){
        cout << "mixed";
    }
   return 0;
}