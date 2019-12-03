#include <fstream>
#include <iostream>
#include <vector>
using namespace std;

int run(vector<int> program) {
  vector<int> arr = program;
  auto i = 0;
  while (true) {
    auto op = arr[i];
    if (op == 99) {
      return arr[0];
    }
    auto a = arr[i + 1];
    auto b = arr[i + 2];
    auto to = arr[i + 3];
    if (op == 1) {
      arr[to] = arr[a] + arr[b];
    } else if (op == 2) {
      arr[to] = arr[a] * arr[b];
    }
    i += 4;
  }
}

int main() {
  ifstream ifile("./input.txt");
  vector<int> program;
  while (ifile) {
    char c;
    int i;
    ifile >> i >> c;
    program.push_back(i);
  }

  vector<int> p1 = program;
  p1[1] = 12;
  p1[2] = 2;
  cout << run(p1) << "\n";

  for (int x = 0; x < 100; ++x) {
    for (int y = 0; y < 100; ++y) {
      vector<int> p2 = program;
      p2[1] = x;
      p2[2] = y;
     if (run(p2) == 19690720) {
        cout << x*100+y << "\n";
     }
    }
  }

  return 0;
}
