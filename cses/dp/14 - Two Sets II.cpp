// Two Sets II
//
// Problem name: Two Sets II
// Problem Link: https://cses.fi/problemset/task/1093
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
 
int fexp(ll b, int e) {
    ll resp = 1;
    while (e) {
        if (e&1) resp = (resp * b) % M;
        b = (b * b) % M;
        e = (e >> 1);
    }
    return resp;
}
 
int main () { _
    int n;
    cin >> n;
    if ((n%4) && ((n+1)%4)) cout << "0\n";
    else {
        int meta = n*(n+1)/4;
        vector<ll> dp(meta+1);
        dp[0] = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = meta; j >= 0; j--) {
                if (j+i <= meta) {
                    dp[j+i] += dp[j];
                    if (dp[j+i] >= M) dp[j+i] -= M;
                }
            }
        }
        cout << (dp[meta] * fexp(2, M-2)) % M << '\n';
    }
    return 0;
}