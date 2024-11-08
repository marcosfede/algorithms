// Longest Flight Route
//
// Problem name: Longest Flight Route
// Problem Link: https://cses.fi/problemset/task/1680
// Author: Bernardo Archegas (https://codeforces.com/profile/Ber)

#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define MAXN 100100
#define INF 100000000
#define pb push_back
#define F first
#define S second
 
using namespace std;
typedef long long int ll;
typedef pair<int, int> pii;
const int M = 1e9+7;
 
int dp[MAXN], check[MAXN], go[MAXN], n;
vector<int> v[MAXN];
 
void dfs(int node) {
    dp[node] = (node == n ? 0 : -1e6);
    for (int x : v[node]) {
        if (!check[x]) dfs(x);
        check[x] = 1;
        if (dp[x] >= dp[node]) {
            dp[node] = 1 + dp[x];
            go[node] = x;
        }
    }
}
 
int main () { _
    int m;
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        v[a].pb(b);
    }
    dfs(1);
    if (dp[1] < 0) cout << "IMPOSSIBLE\n";
    else {
        cout << dp[1] + 1 << '\n';
        cout << "1 ";
        int atual = go[1];
        while (atual != 0) {
            cout << atual << ' ';
            atual = go[atual];
        }
        cout << '\n';
    }
    return 0;
}