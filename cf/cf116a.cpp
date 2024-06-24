#include <bits/stdc++.h>
#include <iostream>
#include <cassert>
using namespace std;


int main(int argc, char* argv[]) {
	int n, a, b; 
	cin >> n;
	int ret = 0, current  = 0; 
	for(int i=0 ; i<n ; ++i) {
		cin >> a;
		cin >> b;
		current -= a;
		current += b;
		
		ret = max(ret, current); 
	}
	cout << ret << "\n"; 
}
