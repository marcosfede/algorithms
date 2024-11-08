// Counting Numbers
//
// Problem name: Counting Numbers
// Problem Link: https://cses.fi/problemset/task/2220
// Author: Bernardo Archegas (https://codeforces.com/profile/Ber)

// Your task is to count the number of integers between a and b where no two adjacent digits are the same.

#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define MAXN 1000100
#define INF 100000000
#define pb push_back
#define F first
#define S second
 
using namespace std;
typedef long long int ll;
typedef pair<int, int> pii;
const int M = 1e9+7;
 
char cnum[10] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
string a, b;
ll dp[20][11][2][2][2];
// pos na string, ultimo digito, flag de ultrapassar, flag pra qual string estamos vendo, flag pra se ja teve num > 0
 
ll count(int pos, int ult, bool flag, bool pri, bool ja) {
    ll &resp = dp[pos][ult][flag][pri][ja];
    if (resp >= 0) return resp;
    if ((pri ? pos == (int)a.size() : pos == (int)b.size())) return 1ll;
    ll ans = 0;
    if (pri) {
        for (int i = 0; i < 10; i++) {
            if (cnum[i] > a[pos] && flag) break;
            if (cnum[i] == a[pos] && i != ult) {
                ans += count(pos+1, (!i && !ja ? 10 : i), flag, pri, (!i ? ja : true));
            }
            else if ((cnum[i] < a[pos] || !flag) && i != ult) {
                ans += count(pos+1, (!i && !ja ? 10 : i), false, pri, (!i ? ja : true));
            }
        }
    }
    else {
        for (int i = 0; i < 10; i++) {
            if (cnum[i] > b[pos] && flag) break;
            if (cnum[i] == b[pos] && i != ult) {
                ans += count(pos+1, (!i && !ja ? 10 : i), flag, pri, (!i ? ja : true));
            }
            else if ((cnum[i] < b[pos] || !flag) && i != ult) {
                ans += count(pos+1, (!i && !ja ? 10 : i), false, pri, (!i ? ja : true));
            }
        }
    }
    return resp = ans;
}
 
int main () { _
    ll c;
    memset(dp, -1, sizeof(dp));
    cin >> c >> b;
    c--;
    a = to_string(c);
    ll ans = count(0, 10, true, false, false) - (c >= 0 ? count(0, 10, true, true, false) : 0ll);
    cout << ans << '\n';
    return 0;
}