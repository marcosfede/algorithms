// Monsters
//
// Problem name: Monsters
// Problem Link: https://cses.fi/problemset/task/1194
// Author: Bernardo Archegas (https://codeforces.com/profile/Ber)

#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define MAXN 1010
#define INF 1000000
#define PB push_back
#define F first
#define S second
 
using namespace std;
typedef long long int lli;
typedef pair<int, int> pii;
const int mod = 1e9+7;
 
int n, m, dist[MAXN][MAXN];
pii go[MAXN][MAXN], a, A;
char v[MAXN][MAXN];
bool ber, check[MAXN][MAXN];
queue<pii> fila;
queue<pair<pii, int>> qu;
 
void BFS_multi() {
    while(!fila.empty()) {
        A = fila.front();
        fila.pop();
        check[A.F][A.S] = true;
        if (A.F + 1 < n && !check[A.F+1][A.S] && v[A.F+1][A.S] != '#') {
            dist[A.F+1][A.S] = min(dist[A.F+1][A.S], 1+dist[A.F][A.S]);
            fila.push({A.F+1, A.S});
            check[A.F+1][A.S] = true;
        }
        if (A.F - 1 >= 0 && !check[A.F-1][A.S] && v[A.F-1][A.S] != '#') {
            dist[A.F-1][A.S] = min(dist[A.F-1][A.S], 1+dist[A.F][A.S]);
            fila.push({A.F-1, A.S});
            check[A.F-1][A.S] = true;
        }
        if (A.S + 1 < m && !check[A.F][A.S+1] && v[A.F][A.S+1] != '#') {
            dist[A.F][A.S+1] = min(dist[A.F][A.S+1], 1+dist[A.F][A.S]);
            fila.push({A.F, A.S+1});
            check[A.F][A.S+1] = true;
        }
        if (A.S - 1 >= 0 && !check[A.F][A.S-1] && v[A.F][A.S-1] != '#') {
            dist[A.F][A.S-1] = min(dist[A.F][A.S-1], 1+dist[A.F][A.S]);
            fila.push({A.F, A.S-1});
            check[A.F][A.S-1] = true;
        }
    }
}
 
pii BFS() {
    while (!qu.empty()) {
        A = qu.front().F;
        if (A.F == 0 || A.F == n-1 || A.S == 0 || A.S == m-1) {
            return A;
        }
        int D = qu.front().S;
        qu.pop();
        check[A.F][A.S] = true;
        if (A.F + 1 < n && !check[A.F+1][A.S] && dist[A.F+1][A.S] > D+1 && v[A.F+1][A.S] != '#') {
            go[A.F+1][A.S] = A;
            qu.push(make_pair(make_pair(A.F+1, A.S), D+1));
            check[A.F+1][A.S] = true;
        }
        if (A.F - 1 >= 0 && !check[A.F-1][A.S] && dist[A.F-1][A.S] > D+1 && v[A.F-1][A.S] != '#') {
            go[A.F-1][A.S] = A;
            qu.push(make_pair(make_pair(A.F-1, A.S), D+1));
            check[A.F-1][A.S] = true;
        }
        if (A.S + 1 < m && !check[A.F][A.S+1] && dist[A.F][A.S+1] > D+1 && v[A.F][A.S+1] != '#') {
            go[A.F][A.S+1] = A;
            qu.push(make_pair(make_pair(A.F, A.S+1), D+1));
            check[A.F][A.S+1] = true;
        }
        if (A.S - 1 >= 0 && !check[A.F][A.S-1] && dist[A.F][A.S-1] > D+1 && v[A.F][A.S-1] != '#') {
            go[A.F][A.S-1] = A;
            qu.push(make_pair(make_pair(A.F, A.S-1), D+1));
            check[A.F][A.S-1] = true;
        }
    }
    return {-1, -1};
}
 
int main() { _
    memset(go, -1, sizeof(go));
    cin >> n >> m;
    int resp = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> v[i][j];
            if (v[i][j] == 'M') {
                dist[i][j] = 0;
                fila.push({i, j});
            }
            else dist[i][j] = INF;
            if (v[i][j] == 'A') a = {i, j};
        }
    }
    BFS_multi();
    memset(check, false, sizeof(check));
    qu.push({a, 0});
    pii fim = BFS();
    if (fim.F == -1) cout << "NO" << endl;
    else {
        cout << "YES" << endl;
        stack<char> ans;
        while(fim != a) {
            if (go[fim.F][fim.S] == make_pair(fim.F+1, fim.S)) ans.push('U');
            else if (go[fim.F][fim.S] == make_pair(fim.F-1, fim.S)) ans.push('D');
            else if (go[fim.F][fim.S] == make_pair(fim.F, fim.S+1)) ans.push('L');
            else ans.push('R');
            resp++;
            fim = go[fim.F][fim.S];
        }
        cout << (int)ans.size() << endl;
        while(!ans.empty()) {
            cout << ans.top();
            ans.pop();
        }
        cout << endl;
    }
    return 0;
}