#include <bits/stdc++.h>

using namespace std;

#define debug(x) cout << "[" <<  #x << " " << x << "] ";

#define ar array
#define ll long long
#define ld long double
#define sz(x) ((int)x.size())
#define all(a) (a).begin(), (a).end()

typedef vector<int> vi;
typedef pair<int,int> pi;

const int MAX_N = 1e5 + 5;
const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

void solve() {
    int r,g,b;
    cin >> r >> g >> b;
    ifstream file("input/in2");
    if(!file.is_open()){
        cout << "Unable to open file";
        return;
    }

    string line;
    ll res = 0;
    while(getline(file,line)){
        if(line.empty())continue;

        istringstream ss(line);
        string gameLabel;
        string colornum;
        ll quantity;
        string color;

        ss.ignore(4);
        ss >> colornum;
        colornum.pop_back();
        int gamen = stoi(colornum);


        unordered_map<string, ll> colorQuantityMap;
        colorQuantityMap["red"] = colorQuantityMap["blue"] = colorQuantityMap["green"] = 0;

        while(ss >> quantity >> color){
            if(color.back() == ','  || color.back() == ';'){
                color.pop_back();
            }
            colorQuantityMap[color] = max(colorQuantityMap[color], quantity);
        }
        res += (colorQuantityMap["red"]*colorQuantityMap["blue"]*colorQuantityMap["green"]);

    }
    cout << res << "\n";
    file.close();

}


int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    solve();
}
