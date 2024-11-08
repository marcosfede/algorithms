// Shortest Routes I
//
// Problem name: Shortest Routes I
// Problem Link: https://cses.fi/problemset/task/1671
// Author: Bernardo Archegas (https://codeforces.com/profile/Ber)

#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define MAXN 100100
#define INF 1000000000000000LL
#define PB push_back
#define F first
#define S second
 
using namespace std;
typedef long long int lli;
typedef pair<int, int> pii;
const int mod = 1e9+7;
 
int n, m;
lli dist[MAXN];
vector<pair<lli, int>> viz[MAXN];
 
void dijkstra() {
    for (int i = 2; i <= n; i++) dist[i] = INF;
    dist[1] = 0LL;
    priority_queue <pair<lli, int>, vector<pair<lli, int>>, greater<pair<lli, int>>> fila;
    fila.push({dist[1], 1});
    while(!fila.empty()) {
        int atual = fila.top().S;
        lli d = fila.top().F;
        fila.pop();
        if (d > dist[atual]) continue;
        for (auto v : viz[atual]) {
            if (dist[v.S] > d + v.F) {
                dist[v.S] = d + v.F;
                fila.push({dist[v.S], v.S});
            }
        }
    }
}
 
int main () { _
    int a, b;
    lli c;
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        cin >> a >> b >> c;
        viz[a].PB({c, b});
    }
    dijkstra();
    for (int i = 1; i <= n; i++) {
        cout << dist[i] << " ";
    }
    cout << endl;
    return 0;
}