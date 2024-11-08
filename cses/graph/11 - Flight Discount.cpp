// Flight Discount
//
// Problem name: Flight Discount
// Problem Link: https://cses.fi/problemset/task/1195
// Author: Bernardo Archegas (https://codeforces.com/profile/Ber)

#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define MAXN 200100
#define INF 1e17
#define pb push_back
#define F first
#define S second
 
using namespace std;
typedef long long int ll;
typedef pair<int, int> pii;
const int M = 1e9+7;
 
vector<pii> v[MAXN];
ll dist[MAXN][10], n, m, coupons = 1;
 
struct d {
	int no;
	int sale;
	ll di;
 
	d(int _no = 0, ll _di = 0, int _sale = 0) {
		no = _no;
		di = _di;
		sale = _sale;
	}
 
	inline const bool operator<(const d& other) const {
		if (sale == other.sale) {
			return di > other.di;
		}
		return sale > other.sale;
	}
};
 
void dijkstra(int node) {
	for (int i = 1; i <= n; i++) {
		for (int j = 0; j < 10; j++) dist[i][j] = INF;
	}
	dist[node][0] = 0;
	d aux;
	aux.no = node, aux.di = 0, aux.sale = 0;
	priority_queue<d> fila;
	fila.push(aux);
	while (!fila.empty()) {
		aux = fila.top();
		fila.pop();
		if (dist[aux.no][aux.sale] < aux.di) continue;
		for (pii x : v[aux.no]) {
			if (dist[x.F][aux.sale] > aux.di + x.S) {
				dist[x.F][aux.sale] = aux.di + x.S;
				d next;
				next.no = x.F, next.di = dist[x.F][aux.sale], next.sale = aux.sale;
				fila.push(next);
			}
			if (aux.sale < coupons) {
				if (dist[x.F][aux.sale+1] > aux.di + x.S/2) {
					dist[x.F][aux.sale+1] = aux.di + x.S/2;
					d next;
					next.no = x.F, next.di = dist[x.F][aux.sale+1], next.sale = aux.sale+1;
					fila.push(next);
				}
			}
		}
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
	cout << dist[n][coupons] << '\n';
	return 0;	
}