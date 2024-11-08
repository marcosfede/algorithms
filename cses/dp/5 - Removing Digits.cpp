// Removing Digits
//
// Problem name: Removing Digits
// Problem Link: https://cses.fi/problemset/task/1637
// Author: Bernardo Archegas (https://codeforces.com/profile/Ber)

#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define MAXN 1000100
#define INF 1000005
 
using namespace std;
typedef long long int lli;
 
int dp[MAXN];
 
int digit(int x) {
    if (x == 0) return 0;
    if (dp[x] > 0) return dp[x];
    string s = to_string(x);
    int resp = INF;
    for (int i = 0; i < (int)s.size(); i++) {
        if (s.at(i) != '0') resp = min(resp, 1 + digit(x-(int)s.at(i)+48));
    }
    return dp[x] = resp;
}
 
int main () { _
    int n;
    cin >> n;
    cout << digit(n) << endl;
    return 0;
}