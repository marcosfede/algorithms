// Message Route
//
// Problem name: Message Route
// Problem Link: https://cses.fi/problemset/task/1667
// Author: Bernardo Archegas (https://codeforces.com/profile/Ber)

#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define MAXN 100100
#define INF 1000000
#define PB push_back
#define F first
#define S second
 
using namespace std;
typedef long long int lli;
typedef pair<int, int> pii;
const int mod = 1e9+7;
 
int n, m, dist[MAXN], go[MAXN];
vector<int> vizinhos[MAXN];
 
void dijkstra() {
    for (int i = 2; i <= n; i++) dist[i] = INF;
    priority_queue<pii, vector<pii>, greater<pii>> fila;
    dist[1] = 1;
    fila.push({dist[1], 1});
    while (!fila.empty()) {
        int atual = fila.top().S;
        int d = fila.top().F;
        fila.pop();
        if (d > dist[atual]) continue;
        for (int i = 0; i < (int)vizinhos[atual].size(); i++) {
            int prox = vizinhos[atual][i];
            if (dist[prox] > 1 + dist[atual]) {
                dist[prox] = 1 + dist[atual];
                fila.push({dist[prox], prox});
                go[prox] = atual;
            }
        }
    }
}
 
int main() { _
    int a, b;
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        cin >> a >> b;
        vizinhos[a].PB(b);
        vizinhos[b].PB(a);
    }
    dijkstra();
    if (dist[n] == INF) cout << "IMPOSSIBLE" << endl;
    else {
        cout << dist[n] << endl;
        int atual = n;
        stack<int> ans;
        ans.push(atual);
        while (atual != 1) {
            ans.push(go[atual]);
            atual = go[atual];
        }
        while (!ans.empty()) {
            cout << ans.top() << " ";
            ans.pop();
        }
        cout << endl;
    }
    return 0;
}