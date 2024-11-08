// Rectangle Cutting
//
// Problem name: Rectangle Cutting
// Problem Link: https://cses.fi/problemset/task/1744
// Author: Bernardo Archegas (https://codeforces.com/profile/Ber)

// Given an a×b rectangle, your task is to cut it into squares. 
// On each move you can select a rectangle and cut it into two rectangles 
// in such a way that all side lengths remain integers. What is the minimum possible number of moves?

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
    int a, b;
    cin >> a >> b;
    vector<vector<int>> dp(505, vector<int> (505, INF));
    for (int i = 1; i <= a; i++) {
        dp[i][i] = 0;
        for (int j = 1; j <= b; j++) {
            for (int k = 1; k < j; k++) {
                dp[i][j] = min(dp[i][j], 1 + dp[i][j-k] + dp[i][k]);
            }
            for (int k = 1; k < i; k++) {
                dp[i][j] = min(dp[i][j], 1 + dp[i-k][j] + dp[k][j]);
            }
        }
    }
    cout << dp[a][b] << '\n';
    return 0;
}