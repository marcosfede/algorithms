// Removal Game
//
// Problem name: Removal Game
// Problem Link: https://cses.fi/problemset/task/1097
// Author: Bernardo Archegas (https://codeforces.com/profile/Ber)

#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define MAXN 1000100
#define INF 100000000
#define pb push_back
#define F first
#define S second
 
using namespace std;
typedef long long int ll;
typedef pair<int, int> pii;
const int M = 1e9+7;
 
int main () { _
    int n;
    cin >> n;
    vector<int> v(n);
    vector<vector<ll>> dp(n, vector<ll> (n));
    ll soma = 0;
    for (int i = 0; i < n; i++) {
        cin >> v[i];
        soma += v[i];
        dp[i][i] = v[i];
    }
    for (int j = 1; j < n; j++) {
        for (int i = 0; i < n; i++) {
            if (i + j < n) {
                dp[i][i+j] = max(v[i] - dp[i+1][i+j], v[i+j] - dp[i][i+j-1]);
            }
        }
    }
    cout << (soma+dp[0][n-1])/2 << '\n';
    return 0;
}