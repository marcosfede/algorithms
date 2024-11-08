// Shortest Routes II
//
// Problem name: Shortest Routes II
// Problem Link: https://cses.fi/problemset/task/1672
// Author: Bernardo Archegas (https://codeforces.com/profile/Ber)

#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define MAXN 505
#define INF 1000000000000000LL
#define PB push_back
#define F first
#define S second
 
using namespace std;
typedef long long int lli;
typedef pair<int, int> pii;
const int mod = 1e9+7;
 
int n, m;
lli dist[MAXN][MAXN];
 
void FW() {
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            for (int k = 1; k <= n; k++) {
                dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k]);
            }
        }
    }
}
 
int main () { _
    int a, b, q;
    lli c;
    cin >> n >> m >> q;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            dist[i][j] = INF;
        }
    }
    for (int i = 0; i < m; i++) {
        cin >> a >> b >> c;
        dist[a][b] = dist[b][a] = min(dist[a][b], c);
    }
    for (int i = 1; i <= n; i++) dist[i][i] = 0;
    FW();
    for (int i = 0; i < q; i++) {
        cin >> a >> b;
        if (dist[a][b] == INF) cout << "-1" << endl;
        else cout << dist[a][b] << endl;
    }
    return 0;
}