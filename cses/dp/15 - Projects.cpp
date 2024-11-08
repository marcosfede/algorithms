// Projects
//
// Problem name: Projects
// Problem Link: https://cses.fi/problemset/task/1140
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
    vector<pair<pii, int>> v(n);
    vector<int> c;
    for (int i = 0; i < n; i++) {
        cin >> v[i].F.F >> v[i].F.S >> v[i].S;
        c.pb(v[i].F.F), c.pb(v[i].F.S);
    }
    sort(c.begin(), c.end());
    map<int, int> mapa;
    int atual = 0;
    mapa[c[0]] = atual++;
    for (int i = 1; i < (int)c.size(); i++) {
        if (c[i] != c[i-1]) mapa[c[i]] = atual++;
    }
    for (int i = 0; i < n; i++) {
        v[i].F.F = mapa[v[i].F.F];
        v[i].F.S = mapa[v[i].F.S];
    }
    sort(v.begin(), v.end());
    vector<ll> dp(1e6);
    atual = n-1;
    for (int i = 5e5; i >= 0; i--) {
        dp[i] = max(dp[i], dp[i+1]);
        while (atual >= 0 && i == v[atual].F.F) {
            dp[i] = max(dp[i], v[atual].S + dp[v[atual].F.S + 1]);
            atual--;
        }
    }
    cout << dp[0] << '\n';
    return 0;
}