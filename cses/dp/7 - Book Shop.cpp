// Book Shop
//
// Problem name: Book Shop
// Problem Link: https://cses.fi/problemset/task/1158
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
    int n, x;
    cin >> n >> x;
    vector<int> h(n), v(n);
    for (int i = 0; i < n; i++) cin >> h[i];
    for (int i = 0; i < n; i++) cin >> v[i];
    vector<vector<int>> dp(n+1, vector<int> (x+1, -1));
    dp[0][x] = 0;
    for (int i = 0; i < n; i++) {
        for (int j = x; j >= 0; j--) {
            if (dp[i][j] >= 0) {
                dp[i+1][j] = max(dp[i+1][j], dp[i][j]);
                if (j >= h[i]) dp[i+1][j-h[i]] = max(dp[i+1][j-h[i]], dp[i][j] + v[i]);
            }
        }
    }
    int ans = 0;
    for (int i = x; i >= 0; i--) ans = max(ans, dp[n][i]);
    cout << ans << '\n';
    return 0;
}