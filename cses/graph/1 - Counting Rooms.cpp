// Counting Rooms
//
// Problem name: Counting Rooms
// Problem Link: https://cses.fi/problemset/task/1192
// Author: Bernardo Archegas (https://codeforces.com/profile/Ber)

#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define MAXN 200100
#define INF 10000000000
 
using namespace std;
typedef long long int lli;
const int mod = 1e9+7;
 
int n, m, matriz[1010][1010], resp = 0;
bool check[1010][1010];
 
void DFS (int i, int j) {
    check[i][j] = true;
    if (i+1 < n and !check[i+1][j] and !matriz[i+1][j]) DFS(i+1, j);
    if (i-1 >= 0 and !check[i-1][j] and !matriz[i-1][j]) DFS(i-1, j);
    if (j+1 < m and !check[i][j+1] and !matriz[i][j+1]) DFS(i, j+1);
    if (j-1 >= 0 and !check[i][j-1] and !matriz[i][j-1]) DFS(i, j-1);
}
 
int main() { _
    char c;
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> c;
            if (c == '.') matriz[i][j] = 0;
            else matriz[i][j] = 1;
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (!check[i][j] and !matriz[i][j]) {
                DFS(i, j);
                resp++;
            }
        }
    }
    cout << resp << endl;
    return 0;
}