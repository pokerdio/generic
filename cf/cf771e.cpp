#include <bits/stdc++.h>
#include <iostream>
#include <cassert>
using namespace std;
//#define VERBOSE 




int main(int argc, char* argv[]) {
    int n; 
	cin >> n;
    vector<Item> v(n);
    vector<Item> sortme(n);

    int swap_token = -1; 
    for (int i=0 ; i<n ; ++i) {
        sortme[i].idx = i;
        cin >> sortme[i].value;
        v[i].value = sortme[i].value; 

        if (lucky(v[i].value) && -1 == swap_token) {
            swap_token = i;
        }
    }
    if (isSorted(v)) {
        cout << "0\n";
        return 0; 
    }
    if (-1 == swap_token) {
        cout << "-1\n";
        return 0; 
    }

    sort(sortme.begin(), sortme.end());
    for (int i=0 ; i<n ; ++i) { // idx is the origin in sortme but it is the final destination in v
        v[sortme[i].idx].idx = i; //v is important for us because it has the values in the pre-sort format
    }

    vector<int> va(0), vb(0); 

#ifdef VERBOSE
    cout << "test " << swap_token << " " << v[0].idx << " " << v[0].value << "\n";
#endif
    bool ok = true;

    while (ok) {
        ok = false; 
        for (int i=0 ; i<n ; ++i) {
#ifdef VERBOSE
            cout << "test i=" << i << " ";
            for (int i=0 ; i<n ; ++i) {
                if (i == swap_token) {
                    cout << "["; 
                }
                cout << v[i].value << "," << v[i].idx;
                if (i == swap_token) {
                    cout << "]"; 
                }
                cout << "  "; 
            }
            cout << "\n";
#endif
            if (i == v[i].idx) { // already sorted
                continue; 
            }

            if (i == swap_token) { //never move the token for its own sake 
                continue; //that way the last move fixes the last misplaced piece as well as the token
            }

            if (v[i].idx == swap_token) { 
                Swap(va, vb, v, i, swap_token);
                swap_token = i;
                ok = true; 
                continue; 
            }
        
            int dest = v[i].idx;
            Swap(va, vb, v, swap_token, dest);
            Swap(va, vb, v, i, dest);
            swap_token = i; 
            ok = true; 
        }
    }
    if (swap_token != v[swap_token].idx) {
        Swap(va, vb, v, swap_token, v[swap_token].idx);
    }

    cout << va.size() << "\n";
    for (int i=0 ; i<va.size() ; ++i) {
        cout << va[i] + 1 << " " << vb[i]  + 1  << "\n";
    }
}
