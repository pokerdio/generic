#include <bits/stdc++.h>
#include <iostream>
#include <cassert>
using namespace std;

#define N 200


int main(int argc, char* argv[]) {
	char s[N + 1] = {0};
	int minweed[N];
	int maxweed[N];

	int n, m;
	int x=0;
	cin >> n >> m; 
	cin.getline(s, N); //consume newline
	int lastn = 0; 
	for (int i=0 ; i<n ; ++i) {
		cin.getline(s, N);
		minweed[i] = N;
		maxweed[i] = -1; 

		for(int j=0 ; s[j] ; ++j) {
			if (s[j] == 'W') {
				lastn = i + 1; 
				maxweed[i] = j;
				if (minweed[i] == N) {
					minweed[i] = j; 
				}
			}
		}
	}
	n = lastn; 
	if (n == 0){
		cout << "0\n";
		exit(0);
	}
	maxweed[n] = -1;  //create a virtual extra empty (grass only) row
	minweed[n] = N; 

	int ret = 0;
	int i = 0; 
	int dest; 
	while (i < n) {
		// go right and down
		dest = max(x, max(maxweed[i], maxweed[i + 1]));
		ret += (dest - x);
		x = dest; 
		i++;
		//cout << dest << "\n";
		// go left and down
		if (i < n) {
			dest = min(x, min(minweed[i], minweed[i + 1]));
			ret += (x - dest);
			x = dest; 
			i++;
		}
		//cout << dest << "\n";
	}
	
	cout << ret + n - 1 << "\n";
}
