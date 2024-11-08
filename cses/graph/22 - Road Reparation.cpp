// Road Reparation
//
// Problem name: Road Reparation
// Problem Link: https://cses.fi/problemset/task/1675
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
 
int pai[MAXN], peso[MAXN];
vector<pair<int, pii>> v;
 
int find(int a) {
	if (pai[a] == a) return a;
	return pai[a] = find(pai[a]);
}
 
void join(int a, int b) {
	a = find(a);
	b = find(b);
	if (a == b) return;
	if (peso[a] > peso[b]) {
		pai[b] = a;
	}
	if (peso[b] > peso[a]) {
		pai[a] = b;
	}
	if (peso[a] == peso[b]) {
		pai[a] = b;
		peso[b]++;
	}
	return;
}
 
int main () { _
	int n, m;
	cin >> n >> m;
	for (int i = 1; i <= n; i++) pai[i] = i;
	for (int i = 0; i < m; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		v.pb({c, {a, b}});
	}
	sort(v.begin(), v.end());
	ll ans = 0;
	int count = 0;
	for (int i = 0; i < m; i++) {
		if (find(v[i].S.F) != find(v[i].S.S)) {
			join(v[i].S.F, v[i].S.S);
			ans += v[i].F;
			count++;
		}
	}
	if (count == n-1) cout << ans << '\n';
	else cout << "IMPOSSIBLE\n";
	return 0;	
}