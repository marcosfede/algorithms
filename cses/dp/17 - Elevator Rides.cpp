// Elevator Rides
//
// Problem name: Elevator Rides
// Problem Link: https://cses.fi/problemset/task/1653
// Author: Bernardo Archegas (https://codeforces.com/profile/Ber)

// There are n people who want to get to the top of a building which has only one elevator. 
// You know the weight of each person and the maximum allowed weight in the elevator. 
// What is the minimum number of elevator rides?

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
    vector<int> v(n);
    for (int i = 0; i < n; i++) cin >> v[i];
    vector<pii> dp((1<<21), {n+1, 0});
    dp[0] = {0, 0};
    for (int i = 1; i < (1 << n); i++) {
        for (int j = 0; j < n; j++) {
            if (i & (1<<j)) {
                pii next = dp[i ^(1<<j)];
                if (next.S + v[j] > x) {
                    next.F++;
                    next.S = v[j];
                }
                else next.S += v[j];
                dp[i] = min(dp[i], next);
            }
        }
    }
    cout << dp[(1<<n)-1].F + (dp[(1<<n)-1].S >= 0) << '\n'; 
    return 0;
}