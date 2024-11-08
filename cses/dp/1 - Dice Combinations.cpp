// Dice Combinations
//
// Problem name: Dice Combinations
// Problem Link: https://cses.fi/problemset/task/1633
// Author: Bernardo Archegas (https://codeforces.com/profile/Ber)

#include <bits/stdc++.h>
 
using namespace std;
 
const int mod = 1e9 + 7;
int dp[1000005];
 
int dice(int n) {
    int resp = 0;
 
    // caso base
    if (n == 0) return 1;
 
    // se ja calculamos a dp
    if (dp[n] > 0) {
        return dp[n];
    }
    for (int i = 1; i<= 6; i++) {
        if (n - i >= 0) {
            resp += dice(n-i);
 
            // lembrar de tirar o modulo
            resp %= mod;
        }
    }
    return dp[n] = resp;
}
 
int main () {
    int n;
    cin >> n;
    cout << dice(n) << endl;
    return 0;
}