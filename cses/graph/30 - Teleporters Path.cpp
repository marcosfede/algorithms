// Teleporters Path
//
// Problem name: Teleporters Path
// Problem Link: https://cses.fi/problemset/task/1693
// Author: Bernardo Archegas (https://codeforces.com/profile/Ber)

// A game has n levels and m teleportes between them. 
// You win the game if you move from level 1 to level n using every teleporter exactly once.
// Can you win the game, and what is a possible way to do it?

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
int grau[MAXN], num[MAXN], edge[MAXN];
 
void euler(int node) {
	stack<int> path;
	path.push(node);
	while (!path.empty()) {
		int cur = path.top();
		if (!num[cur]) {
			ans.push(cur);
			path.pop();
		}
		else {
			pii next = v[cur].back();
			v[cur].pop_back();
			num[cur]--;
			edge[next.S] = 1;
			path.push(next.F);
		}
	}
}
 
int main () { _
	int n, m;
	cin >> n >> m;
	for (int i = 0; i < m; i++) {
		int a, b;
		cin >> a >> b;
		v[a].pb({b, i});
		grau[a]++;
		grau[b]--;
		num[a]++;
	}
	bool valid = (grau[1] == 1 && grau[n] == -1);
	for (int i = 2; i < n; i++) valid &= (grau[i] == 0);
	if (!valid) cout << "IMPOSSIBLE\n";
	else {
		euler(1);
		for (int i = 0; i < m; i++) valid &= edge[i];
		if (!valid) cout << "IMPOSSIBLE\n";
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