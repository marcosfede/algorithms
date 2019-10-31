#include <iostream>
#include <set>
#include <vector>

using namespace std;

vector<int> missing_ranges(vector<int> arr, int low, int high)
{
  set<int> s;
  vector<int> v;
  for (auto x : arr)
  {
    s.insert(x);
  }
  for (int i = low; i < high; i++)
  {
    if (s.find(i) == s.end())
      v.push_back(i);
  }
  return v;
}

int main()
{
  vector<int> arr = {10, 12, 11, 15};
  int low = 10;
  int high = 15;

  vector<int> missing = missing_ranges(arr, low, high);

  for (int x : missing)
    cout << x << endl;

  return 0;
}
