// Planets and Kingdoms
//
// Problem name: Planets and Kingdoms
// Problem Link: https://cses.fi/problemset/task/1683
// Author: Bernardo Archegas (https://codeforces.com/profile/Ber)

// A game has n planets, connected by m teleporters. 
// Two planets a and b belong to the same kingdom exactly 
// when there is a route both from a to b and from b to a. 
// Your task is to determine for each planet its kingdom.

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
 
int vis[MAXN], cnt = 0, c[MAXN];
vector<int> v[MAXN], w[MAXN], ord;
 
void dfs1(int node) {
	vis[node] = 1;
	for (int x : v[node]) 
		if (!vis[x]) dfs1(x);
	ord.pb(node);
}
 
void dfs2(int node) {
	vis[node] = 1;
	c[node] = cnt;
	for (int x : w[node])
		if (!vis[x]) dfs2(x);
}
 
int main () { _
	int n, m, a, b;
	cin >> n >> m;
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
	cout << cnt << '\n';
	for (int i = 1; i <= n; i++) cout << c[i] << ' ';
	cout << '\n';
    return 0;
}