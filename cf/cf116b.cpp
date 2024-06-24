#include <bits/stdc++.h>
#include <iostream>
#include <cassert>
#include <unistd.h>
using namespace std;

#define N 66


char poly[N][N] = {0};

int minwolf(int &row, int&col, int n, int m) {
	row = -1;
	col = -1; 
	int bestpig = 5; 

	for (int i=0 ; i<n ; ++i) {
		for(int j=0 ; j<m ; ++j) {
			if (poly[i][j] != 'W') {
				continue;  //wolves only plz
			}
			int pig = 0; 
			if ((i < n - 1) && (poly[i+1][j] == 'P')) {
				pig += 1; 
			}

			if ((i > 0) && (poly[i-1][j] == 'P')) {
				pig += 1; 
				
			}

			if ((j < m - 1) && (poly[i][j+1] == 'P')) {
				pig += 1; 
			}

			if ((j > 0) && (poly[i][j-1] == 'P')) {
				pig += 1; 
			}
			if (pig < bestpig) {
				bestpig = pig;
				row = i;
				col = j;
			}
		}
	}
	return bestpig; 
}

void printpoly(int n) {
	for (int i=0 ; i<n ; ++i) {
		cout << poly[i] << "!!!" << "\n";
	}
	cout << "\n\n";
	sleep(1);
}

int main(int argc, char* argv[]) {
	int n, m, i, j, pigs; 
	int ret = 0;
	cin >> n >> m;

	cin.getline(poly[N-1], N);

	for (int i=0 ; i<n ; ++i) {
		cin.getline(poly[i], N);
	}
	//printpoly(n);
	while (1) {
		pigs = minwolf(i, j, n, m);
		if (pigs > 4) {
			break;
		}
		poly[i][j] = '.';
		//cout << i << " "  << j << " " << pigs << "\n";
		if (pigs > 0) {
			for (int di=-1 ; di<2 ; di+=1) {
				for (int dj=-1 ; dj<2 ; dj+=1) {
					if (di * dj != 0 || di + dj == 0) {
						continue; 
					}
					//cout << "trying "<< di << " " << dj << " " << di+i << " " << dj+j << "\n";
					if ((i+di)>=0  && (i+di)<n && (j+dj)>=0  && (j+dj)<m) {
						if (poly[i+di][j+dj] == 'P') {
							poly[i+di][j+dj] = '.';
							ret += 1;
							di = dj = 66;
						}
					}
				}
			}
		}
		//printpoly(n);
		//cout << ret << "\n"; 
	}
	
	cout << ret << "\n"; 
}
