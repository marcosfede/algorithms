// Grid Paths
//
// Problem name: Grid Paths
// Problem Link: https://cses.fi/problemset/task/1638
// Author: Bernardo Archegas (https://codeforces.com/profile/Ber)

#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define MAXN 1000100
#define INF 1000005
 
using namespace std;
typedef long long int lli;
const int mod = 1e9+7;
 
int dp[1010][1010], n;
bool m[1010][1010];
 
int ways (int i, int j) {
    if (dp[i][j] >= 0) return dp[i][j];
    int resp = 0;
    if (i < n and m[i+1][j]) {
        resp += ways(i+1, j);
        resp %= mod;
    }
    if (j < n and m[i][j+1]) {
        resp += ways(i, j+1);
        resp %= mod;
    }
    return dp[i][j] = resp;
}
 
int main () { _
    char c;
    memset(dp, -1, sizeof(dp));
    cin >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> c;
            if (c == '.') m[i][j] = true;
            else m[i][j] = false;
        }
    }
    dp[n-1][n-1] = 1;
    if (!m[0][0]) cout << "0" << endl;
    else cout << ways(0,0) << endl;
    return 0;
}