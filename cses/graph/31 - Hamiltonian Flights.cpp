// Hamiltonian Flights
//
// Problem name: Hamiltonian Flights
// Problem Link: https://cses.fi/problemset/task/1690
// Author: Bernardo Archegas (https://codeforces.com/profile/Ber)

// There are n cities and m flight connections between them. 
// You want to travel from Syrjälä to Lehmälä so that you visit each city exactly once. 
// How many possible routes are there?

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
 
int mat[25][25], dp[1100000][25];
 
int main () { _
	int n, m;
	cin >> n >> m;
	for (int i = 0; i < m; i++) {
		int a, b;
		cin >> a >> b;
		mat[a][b]++;
	}
	dp[1][1] = 1;
	for (int i = 1; i < (1<<n); i++) {
		for (int j = 1; j <= n; j++) {
			if (dp[i][j]) {
				for (int k = 0; k < n; k++) {
					if (!(i & (1<<k)) && mat[j][k+1]) {
						dp[i ^ (1<<k)][k+1] += (1ll* dp[i][j] * mat[j][k+1]) % M;
						if (dp[i ^ (1<<k)][k+1] >= M) dp[i ^ (1<<k)][k+1] -= M;
					}
				}
			}
		}
	}
	cout << dp[(1<<n) - 1][n] << '\n';
	return 0;	
}