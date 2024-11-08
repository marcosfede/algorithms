// Array Description
//
// Problem name: Array Description
// Problem Link: https://cses.fi/problemset/task/1746
// Author: Bernardo Archegas (https://codeforces.com/profile/Ber)

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
 
int main () { _
    int n, m;
    cin >> n >> m;
    vector<int> v(n);
    for (int i = 0; i < n; i++) cin >> v[i];
    vector<vector<ll>> dp(n+1, vector<ll> (m+2, 0));
    for (int i = 1; i <= m; i++) {
        if (!v[0] || v[0] == i) dp[0][i] = 1;
    }    
    for (int i = 1; i < n; i++) {
        for (int j = 1; j <= m; j++) {
            if (!v[i] || v[i] == j) {
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]) % M;
            }
        }
    }
    int ans = 0;
    for (int i = 1; i <= m; i++) {
        if (v[n-1] == i || !v[n-1]) {
            ans += dp[n-1][i];
            if (ans >= M) ans -= M;
        }
    }
    cout << ans << '\n';
    return 0;
}