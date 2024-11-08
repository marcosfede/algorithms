// Knight's Tour
//
// Problem name: Knight's Tour
// Problem Link: https://cses.fi/problemset/task/1689
// Author: Bernardo Archegas (https://codeforces.com/profile/Ber)

// Given a starting position of a knight on an 8×8 chessboard, 
// your task is to find a sequence of moves such that it visits every square exactly once.
// On each move, the knight may either move two steps horizontally and one step vertically, 
// or one step horizontally and two steps vertically.

#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define MAXN 4000100
#define INF 1000000001
#define pb push_back
#define F first
#define S second
 
using namespace std;
typedef long long int ll;
typedef pair<int, int> pii;
const int M = 1e9+7;
 
int dx[8] = {2, 2, -2, -2, 1, -1, 1, -1}, dy[8] = {1, -1, 1, -1, 2, 2, -2, -2};
int mat[10][10];
 
bool valid(int x, int y) { return (x >= 0 && y >= 0 && x < 8 && y < 8 && !mat[x][y]); }
 
int count(int x, int y) {
	int resp = 0;
	for (int i = 0; i < 8; i++) {
		resp += valid(x+dx[i], y+dy[i]);
	}
	return resp;
}
 
bool dfs(int x, int y, int pos) {
	if (pos == 64) return true;
	vector<pair<int, pii>> v;
	for (int i = 0; i < 8; i++) {
		if (valid(x+dx[i], y+dy[i])) {
			v.pb({count(x+dx[i], y+dy[i]), {x+dx[i], y+dy[i]}});
		}
	}
	sort(v.begin(), v.end());
	for (int i = 0; i < (int)v.size(); i++) {
		mat[v[i].S.F][v[i].S.S] = pos+1;
		if (dfs(v[i].S.F, v[i].S.S, pos+1)) return true;
		mat[v[i].S.F][v[i].S.S] = 0;
	}
	return false;
}
 
int main () { _
	int x, y;
	cin >> x >> y;
	x--, y--;
	mat[y][x] = 1;
	dfs(y, x, 1);
	for (int i = 0; i < 8; i++) {
		for (int j = 0; j < 8; j++) {
			cout << mat[i][j] << ' ';
		}
		cout << '\n';
	}
	return 0;	
}