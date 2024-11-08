// High Score
//
// Problem name: High Score
// Problem Link: https://cses.fi/problemset/task/1673
// Author: Bernardo Archegas (https://codeforces.com/profile/Ber)

#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define MAXN 5050
#define INF 1e17
#define pb push_back
#define F first
#define S second
 
using namespace std;
typedef long long int ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
const int M = 998244353;
 
vector<array<int, 3>> v;
vector<int> u[MAXN], w[MAXN];
ll dist[MAXN];
int inv[MAXN], vis1[MAXN], vis2[MAXN];
 
void dfs1(int node) {
	vis1[node] = 1;
	for (int x : u[node]) 	
		if (!vis1[x]) dfs1(x);
}
 
void dfs2(int node) {
	vis2[node] = 1;
	for (int x : w[node]) 	
		if (!vis2[x]) dfs2(x);
}
 
int main() { _
	int n, m;
	cin >> n >> m;
	array<int, 3> a;
	for (int i = 0; i < m; i++) {
		cin >> a[0] >> a[1] >> a[2];
		a[2] = -a[2];
		v.pb(a);
		u[a[0]].pb(a[1]);
		w[a[1]].pb(a[0]);
	}
	for (int i = 2; i <= n; i++) dist[i] = INF;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			dist[v[j][1]] = min(dist[v[j][1]], dist[v[j][0]] + v[j][2]);
		}
	}
	for (int j = 0; j < m; j++) {
		if (dist[v[j][0]] + v[j][2] < dist[v[j][1]]) inv[v[j][1]] = 1;
	}
	bool ok = true;
	dfs1(1);
	dfs2(n);
	ll ans = -dist[n];
	for (int i = 1; i <= n; i++) {
		if (inv[i] && vis1[i] && vis2[i]) ok = 0;
	}
	if (!ok) ans = -1;
	cout << ans << '\n';
    return 0;
}