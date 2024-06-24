#include <bits/stdc++.h>
#include <iostream>
#include <cassert>
#include <unistd.h>
using namespace std;

int main(int argc, char* argv[]) {
	int n; 
	int ret = 0;
	int v[2005];
	int boss[2005] = {0};
	cin >> n;
	for (int i=0 ; i<n ; ++i) {
		int x;
		cin >> x; 
		if (x > 0) {
			x -= 1; 
		}
		v[i] = x; 
		boss[x] = 1; 
	}

	int best_rank = 1; 
	for (int i=0 ; i<n ; ++i) {
		if (!boss[i]) {
			int j = v[i];
			int r = 1;
			while (j >= 0) {
				r++;
				j = v[j];
			}
			if (r > best_rank) {
				best_rank = r;
			}
		}
	}
	cout << best_rank << "\n";
}
