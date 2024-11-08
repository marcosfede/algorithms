// Coin Combinations I
//
// Problem name: Coin Combinations I
// Problem Link: https://cses.fi/problemset/task/1635
// Author: Bernardo Archegas (https://codeforces.com/profile/Ber)

#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define MAXN 1000100
#define INF 1000005
 
using namespace std;
typedef long long int lli;
 
const int mod = 1e9 + 7;
int dp[MAXN], n, x, v[105];
 
int coin(int soma) {
    if (dp[soma] >= 0) return dp[soma];
    int resp = 0;
    for (int i = 1; i <= n; i++) {
        if (soma - v[i] >= 0) {
            resp += coin(soma-v[i]);
            resp %= mod;
        }
        else break;
    }
    return dp[soma] = resp;
}
 
int main () { _
    memset(dp, -1, sizeof(dp));
    cin >> n >> x;
    for (int i = 1; i <= n; i++) {
        cin >> v[i];
    }
    sort(v+1, v+n+1);
    dp[0] = 1;
    cout << coin(x) << endl;
    return 0;
}