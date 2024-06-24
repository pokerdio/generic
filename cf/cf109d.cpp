#include <bits/stdc++.h>
#include <iostream>
#include <cassert>
using namespace std;
//#define VERBOSE 

int main(int argc, char* argv[]) {
    int n; 
	cin >> n;
    vector<vector<int>> v(2, vector<int>(n));
    for (int row=0 ; row<2 ; ++row) {
        for (int col=0 ; col<n ; ++col) {
            cin >> v[row][col];
        }
    }
}
