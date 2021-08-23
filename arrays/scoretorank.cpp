#include <iostream>
#include <vector>
#include <fstream>
#include <map>
using namespace std;

int n; 
cin >> n;

vector<int> p(n);
fo(i, n) {
    cin >> p[i];
}
int k; cin >> k;

sort(p.begin(), p.end(), greater<int>());

map<int, int>mp;
int rank = 1;

for (auto x : p) {

    if (!mp.count(x))
        mp[x] = rank;
    rank++;
}
int count = 0;
for (auto x : p) {
    if (mp[x] <= k)
        count++;
}

cout << count << endl;