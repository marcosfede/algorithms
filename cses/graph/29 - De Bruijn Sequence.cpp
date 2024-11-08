// De Bruijn Sequence
//
// Problem name: De Bruijn Sequence
// Problem Link: https://cses.fi/problemset/task/1692
// Author: Bernardo Archegas (https://codeforces.com/profile/Ber)

// Your task is to construct a minimum-length bit string that contains all possible substrings of length n. 
// For example, when n=2, the string 00110 is a valid solution, because its substrings of length 2 are 00, 01, 10 and 11.

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
 
vector<int> v[MAXN];
string ans;
int grau[MAXN], n, start = -1;
 
void euler(int node) {
	stack<pair<int, char>> path;
	path.push({node, ' '});
	while (!path.empty()) {
		pair<int, char> cur = path.top();
		if (!grau[cur.F]) {
			if (start == -1) start = cur.F;
			ans += cur.S;
			path.pop();
		}
		else {
			int next = v[cur.F].back();
			v[cur.F].pop_back();
			path.push({next, (next&1 ? '1' : '0')});
			grau[cur.F]--;
		}
	}
}
 
int main () { _
	cin >> n;
	for (int i = 0; i < (1<<(n-1)); i++) {
		int next = i<<1 & ((1<<(n-1)) - 1);
		v[i].pb(next);
		v[i].pb(next+1);
		grau[i] = 2;
	}
	euler(0);
	ans.pop_back();
	for (int i = 0; i < n-1; i++) {
		ans += (start & (1 << i) ? '1' : '0');
	}
	cout << ans << '\n';
	return 0;	
}