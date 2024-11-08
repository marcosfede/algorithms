// Flight Routes
//
// Problem name: Flight Routes
// Problem Link: https://cses.fi/problemset/task/1196
// Author: Bernardo Archegas (https://codeforces.com/profile/Ber)

// Your task is to find the k shortest flight routes from Syrjälä to Metsälä. 
// A route can visit the same city several times.
// Note that there can be several routes with the same price 
// and each of them should be considered (see the example).

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
const int M = 998244353;
 
vector<pii> v[MAXN];
priority_queue<ll> dist[MAXN];
int n, m, k;
 
void dijkstra() {
	for (int i = 1; i <= n; i++) {
		for (int j = 0; j < k; j++) dist[i].push(INF);
	}
	dist[1].pop();
	dist[1].push(0);
	priority_queue<pll, vector<pll>, greater<pll>> fila;
	fila.push({0, 1});
	while (!fila.empty()) {
		pll atual = fila.top();
		fila.pop();
		if (atual.F > dist[atual.S].top()) continue;
		for (pii x : v[atual.S]) {
			if (dist[x.F].top() > atual.F + x.S) {
				dist[x.F].pop();
				dist[x.F].push(atual.F + x.S);
				fila.push({atual.F + x.S, x.F});
			}
		}
	}
}
 
int main() { _
	cin >> n >> m >> k;
	for (int i = 0; i < m; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		v[a].pb({b, c});
	}
	dijkstra();
	vector<ll> ans;
	while (!dist[n].empty()) {
		ans.pb(dist[n].top());
		dist[n].pop();
	}
	reverse(ans.begin(), ans.end());
	for (ll x : ans) cout << x << ' ';
	cout << '\n';
    return 0;
}