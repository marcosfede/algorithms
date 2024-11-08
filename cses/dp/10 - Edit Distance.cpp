// Edit Distance
//
// Problem name: Edit Distance
// Problem Link: https://cses.fi/problemset/task/1639
// Author: Bernardo Archegas (https://codeforces.com/profile/Ber)

// The edit distance between two strings is the minimum number of operations required to transform one string into the other.
// The allowed operations are:
//     Add one character to the string.
//     Remove one character from the string.
//     Replace one character in the string.
// For example, the edit distance between LOVE and MOVIE is 2, because you can first replace L with M, and then add I.
// Your task is to calculate the edit distance between two strings.

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
    string a, b;
    cin >> a >> b;
    int tama = (int)a.size(), tamb = (int)b.size();
    vector<vector<int>> dp(5050, vector<int> (5050, 10000));
    dp[tama][tamb] = 0;
    for (int i = tama; i >= 0; i--) {
        for (int j = tamb; j >= 0; j--) {
            dp[i][j] = min(dp[i][j], (a[i] != b[j]) + dp[i+1][j+1]);
            dp[i][j] = min(dp[i][j], 1 + dp[i+1][j]);
            dp[i][j] = min(dp[i][j], 1 + dp[i][j+1]);
        }
    }
    cout << dp[0][0] << '\n';
    return 0;
}