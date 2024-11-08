// Counting Tilings
//
// Problem name: Counting Tilings
// Problem Link: https://cses.fi/problemset/task/2181
// Author: Bernardo Archegas (https://codeforces.com/profile/Ber)

// Your task is to count the number of ways you can fill an n×m grid using 1×2 and 2×1 tiles

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
    vector<vector<int>> v((1<<n)+2);
    vector<vector<int>> dp(1010, vector<int> (1<<(n+1)));
    for (int i = 0; i < (1<<n); i++) {
        for (int j = 0; j < (1<<n); j++) {
            int count = 0;
            bool valid = true;
            for (int k = 0; k < n; k++) {
                if ((i & (1<<k))) {
                    if ((j & (1<<k))) valid = false;
                    valid &= !(count&1);
                    count = 0;
                }
                else if (j & (1<<k)) {
                    valid &= !(count&1);
                    count = 0;
                }
                else count++;
            }
            valid &= !(count&1);
            if (valid) v[i].pb(j);
        }
    }
    for (int i = 0; i < (int)v[0].size(); i++) {
        dp[1][v[0][i]] = 1;
    }
    for (int i = 2; i <= m; i++) {
        for (int j = 0; j < (1<<n); j++) {
            for (int k = 0; k < (int)v[j].size(); k++) {
                int l = v[j][k];
                dp[i][j] += dp[i-1][l];
                if (dp[i][j] >= M) dp[i][j] -= M;
            }
        }
    }
    cout << dp[m][0] << '\n';
    return 0;
}