// Minimizing Coins
//
// Problem name: Minimizing Coins
// Problem Link: https://cses.fi/problemset/task/1634
// Author: Bernardo Archegas (https://codeforces.com/profile/Ber)

#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define MAXN 1000100
#define INF 1000005
 
using namespace std;
typedef long long int lli;
 
int dp[MAXN], n, x, v[105];
 
int coin(int soma) {
    if (dp[soma] > 0) return dp[soma];
    if (soma == 0) return 0;
    int resp = INF;
    for (int i = n; i > 0; i--) {
        if (soma-v[i] >= 0) resp = min(resp, 1+coin(soma-v[i]));
    }
    return dp[soma] = resp;
}
 
int main () {
    cin >> n >> x;
    for (int i = 1; i <= n; i++) {
        cin >> v[i];
    }
    int ans = coin(x);
    if (ans > 1000000) cout << "-1" << endl;
    else cout << ans << endl;
    return 0;
}