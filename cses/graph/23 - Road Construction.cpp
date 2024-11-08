// Road Construction
//
// Problem name: Road Construction
// Problem Link: https://cses.fi/problemset/task/1676
// Author: Bernardo Archegas (https://codeforces.com/profile/Ber)

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
 
int pai[MAXN], sz[MAXN], peso[MAXN], comp, maxi;
 
int find(int a) {
	if (pai[a] == a) return a;
	return pai[a] = find(pai[a]);
}
 
void join(int a, int b) {
	a = find(a);
	b = find(b);
	if (a == b) return;
	comp--;
	if (peso[a] > peso[b]) {
		pai[b] = a;
		sz[a] += sz[b];
	}
	if (peso[b] > peso[a]) {
		pai[a] = b;
		sz[b] += sz[a];
	}
	if (peso[a] == peso[b]) {
		pai[a] = b;
		sz[b] += sz[a];
		peso[b]++;
	}
	maxi = max({maxi, sz[a], sz[b]});
	return;
}
 
int main () { _
	int n, m;
	cin >> n >> m;
	for (int i = 1; i <= n; i++) {
		pai[i] = i;
		sz[i] = 1;
	}
	comp = n, maxi = 1;
	for (int i = 0; i < m; i++) {
		int a, b;
		cin >> a >> b;
		join(a, b);
		cout << comp << ' ' << maxi << '\n';
	}
	return 0;	
}