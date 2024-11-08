// Cycle Finding
//
// Problem name: Cycle Finding
// Problem Link: https://cses.fi/problemset/task/1197
// Author: Bernardo Archegas (https://codeforces.com/profile/Ber)

// You are given a directed graph, and your task is to find out 
// if it contains a negative cycle, and also give an example of such a cycle.

#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define MAXN 2550
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
ll dist[MAXN];
int p[MAXN];
 
int main() { _
	int n, m;
	cin >> n >> m;
	array<int, 3> a;
	for (int i = 0; i < m; i++) {
		cin >> a[0] >> a[1] >> a[2];
		v.pb(a);
	}
	int x = -1;
	for (int i = 2; i <= n; i++) dist[i] = INF;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (dist[v[j][0]] + v[j][2] < dist[v[j][1]]) {
				dist[v[j][1]] = dist[v[j][0]] + v[j][2];
				p[v[j][1]] = v[j][0];
				if (i == n-1) x = v[j][1];
			}
		}
	}
	if (x == -1) cout << "NO\n";
	else {
		cout << "YES\n";
		for (int i = 0; i < n; i++) x = p[x];
		stack<int> ans;
		ans.push(x);
		for (int i = p[x]; i != x; i = p[i]) {
			ans.push(i);
		}
		ans.push(x);
		while (!ans.empty()) {
			cout << ans.top() << ' ';
			ans.pop();
		}
		cout << '\n';
	}
    return 0;
}