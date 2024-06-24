#include <bits/stdc++.h>
#include <iostream>
#include <cassert>
using namespace std;


int main(int argc, char* argv[]) {
	int n, a, b; 
	cin >> a >> b;
    assert(a <= b);
	for(n=0 ; a<=b ; ++n) {
        a *= 3;
        b *= 2;
	}
	cout << n << "\n"; 
}
