// Round Trip II
//
// Problem name: Round Trip II
// Problem Link: https://cses.fi/problemset/task/1678
// Author: Bernardo Archegas (https://codeforces.com/profile/Ber)

#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define MAXN 200100
#define INF 1000000001
#define pb push_back
#define F first
#define S second
 
using namespace std;
typedef long long int ll;
typedef pair<int, int> pii;
const int M = 1e9+7;
 
vector<int> v[MAXN];
stack<int> ans;
int valid;
int cor[MAXN], go[MAXN];
 
void dfs(int node) {
	cor[node] = 1;
	for (int x : v[node]) {
		if (cor[x] == 1 && ans.empty()) {
			int ini = x;
			valid = node;
			ans.push(x);
			while (valid != ini) {
				ans.push(valid);
				valid = go[valid];
			}
			ans.push(valid);
		}
		if (!cor[x]) {
			go[x] = node;
			dfs(x);
		}
	}
	cor[node] = 2;
}
 
int main () { _
	int n, m;
	cin >> n >> m;
	for (int i = 0; i < m; i++) {
		int a, b;
		cin >> a >> b;
		v[a].pb(b);
	}
	for (int i = 1; i <= n && !valid; i++) {
		if (!cor[i]) {
			dfs(i);
		}
	}
	if (!valid) cout << "IMPOSSIBLE\n";
	else {
		cout << ans.size() << '\n';
		while (!ans.empty()) {
			cout << ans.top() << ' ';
			ans.pop();
		}
		cout << '\n';
	}
	return 0;	
}