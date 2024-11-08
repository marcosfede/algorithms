// Building Roads
//
// Problem name: Building Roads
// Problem Link: https://cses.fi/problemset/task/1666
// Author: Bernardo Archegas (https://codeforces.com/profile/Ber)

#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define MAXN 100100
#define INF 1000000
 
using namespace std;
typedef long long int lli;
typedef pair<int, int> pii;
const int mod = 1e9+7;
 
int pai[MAXN], n, m;
bool check[MAXN];
vector<int> resp;
 
int find(int x) {
    if (pai[x] == x) return x;
    return pai[x] = find(pai[x]);
}
 
void join(int a, int b) {
    int pai1 = find(a);
    int pai2 = find(b);
 
    if (pai1 == pai2) return;
    if (pai1 == 1) {
        pai[pai2] = pai1;
    }
    else pai[pai1] = pai2;
}
 
int main() { _
    int resp = 0;
    queue<pii> ans;
    cin >> n >> m;
    int a, b;
    for (int i = 1; i <= n; i++) {
        pai[i] = i;
    }
    for (int i = 0; i < m; i++) {
        cin >> a >> b;
        join(a, b);
    }
    int conec = 1;
    for (int i = 2; i <= n; i++) {
        if (find(i) != conec) {
            resp++;
            ans.push({1, i});
            join(1, i);
        }
    }
    cout << resp << endl;
    while(!ans.empty()) {
        cout << ans.front().first << " " << ans.front().second << endl;
        ans.pop();
    }
    return 0;
}