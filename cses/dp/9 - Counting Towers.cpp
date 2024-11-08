// Counting Towers
//
// Problem name: Counting Towers
// Problem Link: https://cses.fi/problemset/task/2413
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
    int t;
    cin >> t;
    vector<vector<ll>> dp(1e6+5, vector<ll> (5));
    dp[1][0] = 2, dp[1][1] = dp[1][2] = dp[1][3] = dp[1][4] = 1;
    for (int i = 1; i <= 1e6; i++) {
        dp[i+1][0] = (2*dp[i][0] + dp[i][1] + dp[i][2] + dp[i][3] + dp[i][4]) % M;
        dp[i+1][1] = (dp[i][0] + dp[i][1] + dp[i][2] + dp[i][3]) % M;
        dp[i+1][2] = dp[i+1][1];
        dp[i+1][3] = (dp[i][0] + dp[i][1] + dp[i][2] + dp[i][3]) % M;
        dp[i+1][4] = (dp[i][0] + dp[i][4]) % M;
    }
    while (t--) {
        int n;
        cin >> n;
        cout << dp[n][0] << '\n';
    }
    return 0;
}