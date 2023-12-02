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
    ll res= 0;
    string digits[] = {"one","two","three","four", "five","six","seven","eight","nine"};
    for(int i=0; i<1000; i++){
        string s;
        cin >> s;
        bool first = true;
        int last = 0;
        int n = s.size();
        for(int j=0; j<s.size(); j++){
            char c = s[j];
            if('0' <= c && c <= '9'){
                if(first){
                    res += 10*(c - '0');
                    first = false;
                }
                last = c-'0';
            }
            else{
                for(int k=0; k<9; k++){
                    if(j + digits[k].size() <= n){
                        if(s.substr(j,digits[k].size()) == digits[k]){
                            if(first){
                                res += 10*(k+1);
                                first = false;
                            }
                            last = k+1;
                        }
                    }
                }
            }
        }
        res += last;
    }
    cout << res << "\n";
}


int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    for (int t = 1; t <= tc; t++) {
        // cout << "Case #" << t << ": ";
        solve();
    }
}
