// Coin Collector
//
// Problem name: Coin Collector
// Problem Link: https://cses.fi/problemset/task/1686
// Author: Bernardo Archegas (https://codeforces.com/profile/Ber)

#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define MAXN 100100
#define INF 1e18
#define pb push_back
#define F first
#define S second
 
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
const int M = 1e9+7;
 
int vis[MAXN], comp[MAXN], cnt = 0;
ll c1[MAXN], c2[MAXN], dp[MAXN], ans = 0;
vector<int> v[MAXN], w[MAXN], nv[MAXN], ord;
 
void dfs1(int node) {
	vis[node] = 1;
	for (int x : v[node]) 
		if (!vis[x]) dfs1(x);
	ord.pb(node);
}
 
void dfs2(int node) {
	vis[node] = 1;
	c2[cnt] += c1[node];
	comp[node] = cnt;
	for (int x : w[node])
		if (!vis[x]) dfs2(x);
}
 
void dfs3(int node) {
	vis[node] = 1;
	dp[node] = c2[node];
	for (int x : nv[node]) {
		if (!vis[x]) dfs3(x);
		dp[node] = max(dp[x] + c2[node], dp[node]);
	}
	ans = max(ans, dp[node]);
}
 
int main () { _
	int n, m, a, b;
	cin >> n >> m;
	for (int i = 1; i <= n; i++) cin >> c1[i];
	for (int i = 0; i < m; i++) {
		cin >> a >> b;
		v[a].pb(b);
		w[b].pb(a);
	}
	for (int i = 1; i <= n; i++) {
		if (!vis[i]) dfs1(i);
	}
	memset(vis, 0, sizeof(vis));
	reverse(ord.begin(), ord.end());
	for (int x : ord) {
		if (!vis[x]) {
			cnt++;
			dfs2(x);
		}
	}
	for (int i = 1; i <= n; i++) {
		for (int x : v[i]) {
			if (comp[x] != comp[i]) nv[comp[i]].pb(comp[x]);
		}
	}
	memset(vis, 0, sizeof(vis));
	for (int i = 1; i <= n; i++) {
		if (!vis[i]) dfs3(i);
	}
	cout << ans << '\n';
    return 0;
}