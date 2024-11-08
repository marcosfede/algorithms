// Flight Routes Check
//
// Problem name: Flight Routes Check
// Problem Link: https://cses.fi/problemset/task/1682
// Author: Bernardo Archegas (https://codeforces.com/profile/Ber)

// There are n cities and m flight connections. Your task is to check if 
// you can travel from any city to any other city using the available flights.

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
 
int vis[MAXN], cnt = 0;
vector<int> v[MAXN], w[MAXN], ord, c[MAXN];
 
void dfs1(int node) {
	vis[node] = 1;
	for (int x : v[node]) 
		if (!vis[x]) dfs1(x);
	ord.pb(node);
}
 
void dfs2(int node) {
	vis[node] = 1;
	c[cnt].pb(node);
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
	if (cnt == 1) cout << "YES\n";
	else {
		cout << "NO\n";
		cout << c[2][0] << ' ' << c[1][0] << '\n';
	}
    return 0;
}