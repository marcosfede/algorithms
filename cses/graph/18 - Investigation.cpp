// Investigation
//
// Problem name: Investigation
// Problem Link: https://cses.fi/problemset/task/1202
// Author: Bernardo Archegas (https://codeforces.com/profile/Ber)

// You are going to travel from Syrjälä to Lehmälä by plane. You would like to find answers to the following questions:
//     what is the minimum price of such a route?
//     how many minimum-price routes are there? (modulo 109+7)
// 	   what is the minimum number of flights in a minimum-price route?
//	   what is the maximum number of flights in a minimum-price route?

#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define MAXN 100100
#define INF 1e17
#define pb push_back
#define F first
#define S second
 
using namespace std;
typedef long long int ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
const int M = 1e9+7;
 
vector<pii> v[MAXN], w[MAXN];
ll dist[MAXN], quant[MAXN], mn[MAXN], mx[MAXN];
int n, m, vis[MAXN];
 
void dijkstra(int node) {
	for (int i = 1; i <= n; i++) dist[i] = INF;
	dist[node] = 0;
	priority_queue<pll, vector<pll>, greater<pll>> fila;
	fila.push({0, node});
	while (!fila.empty()) {
		pll atual = fila.top();
		fila.pop();
		if (dist[atual.S] < atual.F) continue;
		for (pii x : v[atual.S]) {
			if (dist[x.F] > atual.F + x.S) {
				dist[x.F] = atual.F + x.S;
				fila.push({dist[x.F], x.F});
			}
		}
	}
}
 
void dag(int node) {
	vis[node] = 1;
	for (pii x : v[node]) {
		if (dist[node] + x.S == dist[x.F]) {
			w[node].pb(x);
			if (!vis[x.F]) dag(x.F);
		}
	}
}
 
void dfs(int node) {
	vis[node] = 1;
	for (pii x : w[node]) {
		if (!vis[x.F]) dfs(x.F);
		quant[node] += quant[x.F];
		if (quant[node] >= M) quant[node] -= M;
		mn[node] = min(mn[node], mn[x.F]+1);
		mx[node] = max(mx[node], mx[x.F]+1);
	}
}
 
int main () { _
	cin >> n >> m;
	for (int i = 0; i < m; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		v[a].pb({b, c});
	}
	dijkstra(1);
	dag(1);
	memset(vis, 0, sizeof(vis));
	for (int i = 1; i <= n; i++) {
		mn[i] = INF;
		mx[i] = -INF;
	}
	mn[n] = mx[n] = 0;
	quant[n] = 1;
	// min price = dist[n]
	// how many routes
	// min number of edges in route
	// max number of edges in route
	dfs(1);
	cout << dist[n] << ' ' << quant[1] << ' ' << mn[1] << ' ' << mx[1] << '\n';
	return 0;
}