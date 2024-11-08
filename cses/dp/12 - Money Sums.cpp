// Money Sums
//
// Problem name: Money Sums
// Problem Link: https://cses.fi/problemset/task/1745
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
    for (int i = 0; i < n; i++) cin >> v[i];
    vector<int> dp(1e5 + 5);
    dp[0] = 1;
    int c = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 1e5; j >= 0; j--) {
            if (dp[j] && j+v[i] <= 1e5) {
                c += (dp[j+v[i]] == 0);
                dp[j+v[i]] = 1;
            }
        }
    }
    cout << c << '\n';
    for (int i = 1; i <= 1e5; i++) 
        if (dp[i]) cout << i << ' ';
    cout << '\n';
    return 0;
}