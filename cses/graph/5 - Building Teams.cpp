// Building Teams
//
// Problem name: Building Teams
// Problem Link: https://cses.fi/problemset/task/1668
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
 
int n, m, id, resp[MAXN];
vector<int> viz[MAXN];
bool check[MAXN], ber;
 
void DFS(int node, int z) {
    check[node] = true;
    resp[node] = z+1;
    for (int i = 0; i < (int)viz[node].size(); i++) {
        int atual = viz[node][i];
        if (!check[atual]) DFS(atual, 1-z);
        else if (resp[atual] == resp[node]) ber = true;
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
    id = 0;
    for (int i = 1; i <= n; i++) {
        if (!check[i]) {
            DFS(i, 0);
        }
    }
    if (!ber) {
        for (int i = 1; i <= n; i++) {
            cout << resp[i] << " ";
        }
        cout << endl;
    }
    else cout << "IMPOSSIBLE" << endl;
    return 0;
}