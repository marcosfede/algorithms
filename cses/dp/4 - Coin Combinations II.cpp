// Coin Combinations II
//
// Problem name: Coin Combinations II
// Problem Link: https://cses.fi/problemset/task/1636
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
    int n, x;
    cin >> n >> x;
    vector<int> coin(n), dp(x+1);
    for (int i = 0; i < n; i++) {
        cin >> coin[i];
    }
    sort(coin.begin(), coin.end());
    dp[0] = 1;
    for (int i = 0; i < n; i++) {
        int atual = coin[i];
        for (int j = atual; j <= x; j++) {
            dp[j] = dp[j] + dp[j-atual];
            if (dp[j] >= M) dp[j] -= M;
        }
    }
    cout << dp[x] << '\n';
    return 0;
}