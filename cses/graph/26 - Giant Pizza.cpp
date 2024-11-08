// Giant Pizza
//
// Problem name: Giant Pizza
// Problem Link: https://cses.fi/problemset/task/1684
// Author: Bernardo Archegas (https://codeforces.com/profile/Ber)

// Uolevi's family is going to order a large pizza and eat it together. 
// A total of n family members will join the order, and there are m possible toppings. 
// The pizza may have any number of toppings.
// Each family member gives two wishes concerning the toppings of the pizza. 
// The wishes are of the form "topping x is good/bad". Your task is to choose the toppings so that at least one wish from everybody becomes true (a good topping is included in the pizza or a bad topping is not included).

#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define MAXN 200100
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
 
vector<int> v[MAXN], w[MAXN], ord, c[MAXN];
int vis[MAXN], cnt = 0, cmp[MAXN], ans[MAXN];
 
void dfs1(int node) {
	vis[node] = 1;
	for (int x : v[node])
		if (!vis[x]) dfs1(x);
	ord.pb(node);
}
 
void dfs2(int node) {
	cmp[node] = cnt;
	c[cnt].pb(node);
	vis[node] = 1;
	for (int x : w[node])
		if (!vis[x]) dfs2(x);
}
 
int main () { _
	int n, m;
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		char a1, a2;
		int aux1, aux2;
		cin >> a1 >> aux1 >> a2 >> aux2;
		if (a1 == '+' && a2 == '+') {
			v[2*aux1+1].pb(2*aux2);
			v[2*aux2+1].pb(2*aux1);
			w[2*aux2].pb(2*aux1+1);
			w[2*aux1].pb(2*aux2+1);
		}
		else if (a1 == '+' && a2 == '-') {
			v[2*aux1+1].pb(2*aux2+1);
			v[2*aux2].pb(2*aux1);
			w[2*aux2+1].pb(2*aux1+1);
			w[2*aux1].pb(2*aux2);
		}
		else if (a1 == '-' && a2 == '+') {
			v[2*aux1].pb(2*aux2);
			v[2*aux2+1].pb(2*aux1+1);
			w[2*aux2].pb(2*aux1);
			w[2*aux1+1].pb(2*aux2+1);
		}
		else if (a1 == '-' && a2 == '-') {
			v[2*aux1].pb(2*aux2+1);
			v[2*aux2].pb(2*aux1+1);
			w[2*aux2+1].pb(2*aux1);
			w[2*aux1+1].pb(2*aux2);
		}
	}
	for (int i = 2; i <= 2*m+1; i++) 
		if (!vis[i]) dfs1(i);
	reverse(ord.begin(), ord.end());
	memset(vis, 0, sizeof(vis));
	for (int x : ord) {
		if (!vis[x]) {
			cnt++;
			dfs2(x);
		}
	}
	bool ok = true;
	for (int i = 2; i <= 2*m; i+=2) {
		if (cmp[i] == cmp[i+1]) ok = false;
		ans[i/2] = (cmp[i] > cmp[i+1]);
	}
	if (!ok) cout << "IMPOSSIBLE\n";
	else {
		for (int i = 1; i <= m; i++) cout << (ans[i] ? '+' : '-') << ' ';
		cout << '\n';
	}
    return 0;
}