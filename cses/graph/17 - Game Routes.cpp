// Game Routes
//
// Problem name: Game Routes
// Problem Link: https://cses.fi/problemset/task/1681
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
 
int dp[MAXN], check[MAXN];
vector<int> v[MAXN];
 
void dfs(int node) {
    for (int x : v[node]) {
        if (!check[x]) dfs(x);
        check[x] = 1;
        dp[node] += dp[x];
        if (dp[node] >= M) dp[node] -= M;
    }
}
 
int main () { _
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        v[a].pb(b);
    }
    dp[n] = 1;
    dfs(1);
    cout << dp[1] << '\n';
    return 0;
}