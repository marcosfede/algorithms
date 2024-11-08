// Labyrinth
//
// Problem name: Labyrinth
// Problem Link: https://cses.fi/problemset/task/1193
// Author: Bernardo Archegas (https://codeforces.com/profile/Ber)

#include <bits/stdc++.h>
using namespace std;
#define MAXN 1003
#define MAXS 1003
int n, m, inix, iniy, fimx, fimy;
int vis[MAXN][MAXS];
char path[MAXN][MAXS];
char mapa[MAXN][MAXS];
int varx[] = {1, -1, 0, 0};
int vary[] = {0, 0, 1, -1};
int BFS(int a, int b) {
    queue<pair<int,int>> q;
    q.push({a, b});
	mapa[a][b] = '#';
    while(!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        for (int i = 0; i < 4; i++) {
            int X = varx[i] + x;
            int Y = vary[i] + y;
            if (X <= 0 || X > n || Y <= 0 || Y > m || mapa[X][Y] == '#') continue;
            q.push({X, Y});
            vis[X][Y] = vis[x][y] + 1;
			bool fim = (mapa[X][Y] == 'B');
	        mapa[X][Y] = '#';
            if (i == 0) path[X][Y] = 'D';
            else if (i == 1) path[X][Y] = 'U';
            else if (i == 2) path[X][Y] = 'R';
            else path[X][Y] = 'L';
            if (fim) {
                fimx = X;
                fimy = Y;
                return vis[X][Y];
            }
        }
    }
    return 0;
}
 
int main() {
    memset(vis, 0, sizeof(vis));
    cin >> n >> m;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            cin >> mapa[i][j];
            if (mapa[i][j] == 'A') {
                inix = i;
                iniy = j;
            }
        }
    }
    int resposta = BFS(inix, iniy);
	if (!resposta) cout << "NO\n";
	else {
		cout << "YES\n";
		cout << resposta << endl;
		vector<char> caminho;
		int i = fimx, j = fimy;
		while (make_pair(i, j) != make_pair(inix, iniy)) {
			caminho.push_back(path[i][j]);
			if (path[i][j] == 'D') i--;
			else if (path[i][j] == 'U') i++;
			else if (path[i][j] == 'R') j--;
			else j++;
		}
		for (int i = caminho.size()-1; i >= 0; i--) {
			cout << caminho[i];
		}
		cout << '\n';
	}
}