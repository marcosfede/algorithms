// Course Schedule
//
// Problem name: Course Schedule
// Problem Link: https://cses.fi/problemset/task/1679
// Author: Bernardo Archegas (https://codeforces.com/profile/Ber)

// You have to complete n courses. There are m requirements of the form "course a has to be completed before course b". 
// Your task is to find an order in which you can complete the courses.

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
 
vector<int> v[MAXN], ans;
bool valid = true;
int cor[MAXN];
 
void dfs(int node) {
	cor[node] = 1;
	for (int x : v[node]) {
		if (cor[x] == 1) {
			valid = false;
			return;
		}
		if (!cor[x]) dfs(x);
	}
	cor[node] = 2;
	ans.pb(node);
}
 
int main () { _
	int n, m;
	cin >> n >> m;
	for (int i = 0; i < m; i++) {
		int a, b;
		cin >> a >> b;
		v[a].pb(b);
	}
	for (int i = 1; i <= n && valid; i++) {
		if (!cor[i]) {
			dfs(i);
		}
	}
	if (!valid) cout << "IMPOSSIBLE\n";
	else {
		reverse(ans.begin(), ans.end());
		for (int x : ans) cout << x << ' ';
		cout << '\n';
	}
	return 0;	
}