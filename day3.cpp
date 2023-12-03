#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>

using namespace std;

vector<string> readFile(string source) {
    ifstream file(source);

    vector<string> lines;
    if(file.is_open()){
        string line;

        while(getline(file,line)){
            lines.push_back(line);
        }
        return lines;
    }
    return lines;
}

void solvea() {
    vector<string> lines = readFile("input/in3");

    int n = lines.size(), m = lines[0].size();
    pair<int,int> neigh[] = {{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}};

    bool partNum = false;
    int currNum = 0;
    int res = 0;
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            if(isdigit(lines[i][j])){
                currNum = 10*currNum + (lines[i][j] - '0');
                for(const pair<int,int> p : neigh) {
                    int ni = i + p.first;
                    int nj = j + p.second;
                    partNum |=  (0 <= ni && ni < n && 0 <= nj && nj < m && lines[ni][nj] != '.' && !isdigit(lines[ni][nj]));
                }
            }
            else{
                if(partNum)res += currNum;
                partNum = false;
                currNum = 0;
            }

        }
    }
    cout << res << "\n";

}

void solveb() {
    vector<string> lines = readFile("input/in3");
    for(string s : lines)s = s + '.';

    int n = lines.size(), m = lines[0].size()+1;

    pair<int,int> neigh[] = {{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}};
    vector vals(n,vector<long long>(m,0));
    vector ids(n,vector<int>(m,0));

    bool partNum = false;
    int currNum = 0;

    map<pair<int,int>, pair<int,int>> gears;
    set<pair<int,int>> ind;

    int res = 0;
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            if(isdigit(lines[i][j])){
                currNum = 10*currNum + (lines[i][j] - '0');
                for(const pair<int,int> p : neigh) {
                    int ni = i + p.first;
                    int nj = j + p.second;
                    if(0 <= ni && ni < n && 0 <= nj && nj < m && lines[ni][nj] == '*'){
                        ind.insert({ni,nj});
                    }
                }
            }
            else{
                for(pair<int,int> p : ind){
                    gears[p].first++;
                    gears[p].second = gears[p].second == 0 ? currNum : gears[p].second*currNum ;
                }
                currNum = 0;
                ind.clear();
            }
        }
    }

    for(pair<pair<int,int>,pair<int,int>> p : gears){
        if(p.second.first == 2)res += p.second.second;
    }
    
    cout << res << "\n";
}



int main() {
    solveb();
    return 0;
}
