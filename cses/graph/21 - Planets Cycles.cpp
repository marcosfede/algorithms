// Planets Cycles
//
// Problem name: Planets Cycles
// Problem Link: https://cses.fi/problemset/task/1751
// Author: Bernardo Archegas (https://codeforces.com/profile/Ber)

// You are playing a game consisting of n planets. Each planet has a teleporter to another planet (or the planet itself).
// You start on a planet and then travel through teleporters until you reach a planet that you have already visited before.
// Your task is to calculate for each planet the number of teleportations there would be if you started on that planet.

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
 
int dist[MAXN], v[MAXN], cor[MAXN];
 
void dfs(int node) {
	cor[node] = 1;
	if (cor[v[node]] == 0) {
		dfs(v[node]);
		if (!dist[node]) dist[node] = dist[v[node]]+1;
	}
	else if (cor[v[node]] == 1) {
		// ciclo
		int atual = node, p = 0;
		do {
			p++;
			atual = v[atual];
		} while (atual != node);
		do {
			dist[atual] = p;
			atual = v[atual];
		} while (atual != node);
	}
	else {
		dist[node] = dist[v[node]]+1;
	}
	cor[node] = 2;
}
 
int main() { _
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++) cin >> v[i];
	for (int i = 1; i <= n; i++) {
		if (!cor[i]) dfs(i);
	}
	for (int i = 1; i <= n; i++) cout << dist[i] << ' ';
	cout << '\n';
    return 0;
}