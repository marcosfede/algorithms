// Mail Delivery
//
// Problem name: Mail Delivery
// Problem Link: https://cses.fi/problemset/task/1691
// Author: Bernardo Archegas (https://codeforces.com/profile/Ber)

// Your task is to deliver mail to the inhabitants of a city. For this reason, 
// you want to find a route whose starting and ending point are the post office, 
// and that goes through every street exactly once.

#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define MAXN 4000100
#define INF 1000000001
#define pb push_back
#define F first
#define S second
 
using namespace std;
typedef long long int ll;
typedef pair<int, int> pii;
const int M = 1e9+7;
 
stack<int> ans;
vector<pii> v[MAXN];
int grau[MAXN], edge[MAXN];
 
void euler(int node) {
	stack<int> path;
	path.push(node);
	while (!path.empty()) {
		int cur = path.top();
		while (!v[cur].empty() && edge[v[cur].back().S]) {
			grau[cur]--;
			v[cur].pop_back();
		}
		if (!grau[cur]) {
			ans.push(cur);
			path.pop();
			continue;
		}
		pii next = v[cur].back();
		v[cur].pop_back();
		grau[cur]--;
		edge[next.S] = 1;
		path.push(next.F);
	}
}
 
int main () { _
	int n, m;
	cin >> n >> m;
	for (int i = 0; i < m; i++) {
		int a, b;
		cin >> a >> b;
		v[a].pb({b, i});
		v[b].pb({a, i});
		grau[a]++, grau[b]++;
	}
	bool ok = true;
	for (int i = 1; i <= n; i++) {
		ok &= (grau[i] % 2 == 0);
	}
	if (!ok) cout << "IMPOSSIBLE\n";
	else {
		euler(1);
		for (int i = 0; i < m; i++) {
			ok &= edge[i];
		}
		if (!ok) cout << "IMPOSSIBLE\n";
		else {
			while (!ans.empty()) {
				cout << ans.top() << ' ';
				ans.pop();
			}
			cout << '\n';
		}
	}
	return 0;	
}