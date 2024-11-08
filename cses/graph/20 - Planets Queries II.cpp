// Planets Queries II
//
// Problem name: Planets Queries II
// Problem Link: https://cses.fi/problemset/task/1160
// Author: Bernardo Archegas (https://codeforces.com/profile/Ber)

// You are playing a game consisting of n planets. 
// Each planet has a teleporter to another planet (or the planet itself).
// You have to process q queries of the form: You are now on planet a and want to reach planet b. 
// What is the minimum number of teleportations?

#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define MAXN 200100
#define INF 1e17
#define pb push_back
#define F first
#define S second
 
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
const int M = 998244353;
 
int tree[MAXN], ciclo[MAXN], id[MAXN], peso[MAXN], tab[MAXN][20], cor[MAXN], dep[MAXN], in[MAXN], x;
 
int sobe(int node, int k) {
	if (k < 0) return -1;
	for (int i = 19; i >= 0; i--) {
		if (k & (1<<i)) node = tab[node][i];
	}
	return node;
}
 
void dfs(int node) {
	cor[node] = 1;
	if (!cor[tab[node][0]]) dfs(tab[node][0]);
	else if (cor[tab[node][0]] == 1) {
		x++;
		int atual = node, p = 0;
		do {	
			p++;
			ciclo[atual] = x;
			tree[atual] = atual;
			id[atual] = p;
			atual = tab[atual][0];
		} while (atual != node);
		peso[x] = p;
	}
	cor[node] = 2;
}
 
void dfs2(int node) {
	cor[node] = 1;
	if (!cor[tab[node][0]] && !ciclo[tab[node][0]]) dfs2(tab[node][0]);
	tree[node] = tree[tab[node][0]];
	dep[node] = dep[tab[node][0]] + 1;
}
 
int main() { _
	x = 0;
	int n, q;
	cin >> n >> q;
	for (int i = 1; i <= n; i++) {
		cin >> tab[i][0];
		in[tab[i][0]]++;
	}
	for (int i = 1; i < 20; i++) {
		for (int j = 1; j <= n; j++) tab[j][i] = tab[tab[j][i-1]][i-1];
	}
	for (int i = 1; i <= n; i++) {
		if (!cor[i]) dfs(i);
	}
	memset(cor, 0, sizeof(cor));
	for (int i = 1; i <= n; i++) {
		if (!in[i]) dfs2(i);
	}
	int a, b;
	for (int i = 0; i < q; i++) {
		cin >> a >> b;
		if (ciclo[a]) {
			if (ciclo[b]) {
				if (ciclo[a] == ciclo[b]) {
					if (id[b] >= id[a]) cout << id[b] - id[a] << '\n';
					else cout << peso[ciclo[b]] + id[b] - id[a] << '\n';
				}
				else cout << "-1\n";
			}
			else if (!ciclo[b]) cout << "-1\n";
		}
		else if (!ciclo[a]) {
			if (!ciclo[b]) {
				if (sobe(a, dep[a] - dep[b]) == b) cout << dep[a] - dep[b] << '\n';
				else cout << "-1\n";
			}
			else if (ciclo[b]) {
				if (ciclo[tree[a]] == ciclo[b]) {
					if (id[b] >= id[tree[a]]) cout << id[b] - id[tree[a]] + dep[a] << '\n';
					else cout << peso[ciclo[b]] + id[b] - id[tree[a]] + dep[a] << '\n';
				}
				else cout << "-1\n";
			}
		}
	}
    return 0;
}