// Planets Queries I
//
// Problem name: Planets Queries I
// Problem Link: https://cses.fi/problemset/task/1750
// Author: Bernardo Archegas (https://codeforces.com/profile/Ber)

#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define MAXN 1000100
#define INF 1e17
#define pb push_back
#define F first
#define S second
 
using namespace std;
typedef long long int ll;
typedef pair<int, int> pii;
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
const int M = 1e9+7;
 
int tab[31][MAXN];
 
int main () { _
	int n, q;
	cin >> n >> q;
	for (int i = 1; i <= n; i++) {
		cin >> tab[0][i];
	}
	for (int i = 1; i < 31; i++) {
		for (int j = 1; j <= n; j++) {
			tab[i][j] = tab[i-1][tab[i-1][j]];
		}
	}
	for (int i = 0; i < q; i++) {
		int a, b;
		cin >> a >> b;
		int atual = a;
		for (int j = 0; j < 31; j++) {
			if (b & (1<<j)) atual = tab[j][atual];
		}
		cout << atual << '\n';
	}
	return 0;
}