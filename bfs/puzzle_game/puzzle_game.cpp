/*
General solution: Each board gets mapped to an integer in the range [0, 9^9)
We visualize the board as a 9 digit number written in base 9 and then convert it to base 10
We then simply run a BFS trying to reach the end state 
*/
#include <bits/stdc++.h>

using namespace std;

const int N = 381367045;

// A bitset to check visited states
bitset<N> vis;
// Precomputate the powers of 9
int pwr[10], dx[] = {1, -1, 0, 0}, dy[] = {0, 0, 1, -1};
map<int, bool> primes = {{2, true}, {3, true}, {5, true}, {7, true}, {11, true}, {13, true}, {17, true}};

int mapping(vector<vector<int>> &v) {
    int x = 0;
    for (int i = 2; i >= 0; i--) {
        for (int j = 2; j >= 0; j--) {
            x = 9 * x + v[i][j] % 9;
        }
    }
    return x;
}
 
int main () { 
    vector<vector<int>> v = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int goal = mapping(v);
    int t;
    cin >> t;
    while (t--) {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                cin >> v[i][j];
            }
        }
        queue<pair<vector<vector<int>>, int>> q;
        q.push({v, 0});
        int mp = mapping(v);
        vis[mp] = true;
        vector<int> visited_states = {mp};
        while (!q.empty()) {
            v = q.front().first;
            int dist = q.front().second;
            q.pop();
            if (mapping(v) == goal) {
                cout << dist << '\n';
                break;
            }
            for (int x = 0; x < 3; x++) {
                for (int y = 0; y < 3; y++) {
                    for (int i = 0; i < 4; i++) {
                        int nx = x + dx[i], ny = y + dy[i];
                        if (nx >= 0 && nx < 3 && ny >= 0 && ny < 3 && primes[v[x][y] + v[nx][ny]]) {
                            swap(v[x][y], v[nx][ny]);
                            int mp = mapping(v);
                            if (!vis[mp]) {
                                vis[mp] = true;
                                visited_states.push_back(mp);
                                q.push({v, dist + 1});
                            }
                            swap(v[x][y], v[nx][ny]);
                        }
                    }
                }
            }
        }
        if (!vis[goal]) cout << "-1\n";
        // resetting our bitset for the next test case
        for (int x : visited_states) {
            vis[x] = false;
        }
    }
    return 0;
}