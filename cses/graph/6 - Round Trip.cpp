// Round Trip
//
// Problem name: Round Trip
// Problem Link: https://cses.fi/problemset/task/1669
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
 
int n, m, go[MAXN], inicio;
vector<int> viz[MAXN], resp;
bool check[MAXN], ber;
 
void DFS(int node, int pai) {
    check[node] = true;
    for (int i = 0; i < (int)viz[node].size(); i++) {
        int atual = viz[node][i];
        if (!check[atual]) {
            if (!ber) go[atual] = node;
            DFS(atual, node);
        }
        else if (atual != pai and !ber) {
            ber = true;
            inicio = atual;
            go[atual] = node;
        }
    }
}
 
int main() { _
    int a, b;
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        cin >> a >> b;
        viz[a].PB(b);
        viz[b].PB(a);
    }
    for (int i = 1; i <= n; i++) {
        if (!check[i]) {
            resp.PB(i);
            DFS(i, 0);
        }
        if (ber) break;
    }
    if (ber) {
        stack<int> ans;
        ans.push(inicio);
        int atual = go[inicio];
        while (atual != inicio) {
            ans.push(atual);
            atual = go[atual];
        }
        ans.push(atual);
        cout << (int)ans.size() << endl;
        while (!ans.empty()) {
            cout << ans.top() << " ";
            ans.pop();
        }
        cout << endl;
    }
    else cout << "IMPOSSIBLE" << endl;
    return 0;
}