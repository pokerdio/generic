#include <bits/stdc++.h>
#include <iostream>
#include <cassert>
using namespace std;

int name_id = 0;

string make_new_name(void) {
    int i = name_id++;

    string s; 

    s = s + "ABCD"[i % 4];
    i /= 4; 
    while (i > 0) {
        s = s + "abcd"[i % 4];
        i /= 4; 
    }
    return s;
}

int main(int argc, char* argv[]) {
	long long n, k; 
	cin >> n >> k;
    vector<int> v(n - k + 1, 0);

    string s;
    int first_yes = -1;
    for (int i=0 ; i<v.size() ; ++i) {
        cin >> s;
        if (s == "YES") {
            if (-1 == first_yes) {
                first_yes = i;
            }
            v[i] = 1; 
        }
    }


    if (-1 == first_yes) { // if all NO name all soldiers "A"
        for (int i=0 ; i<n ; ++i) {
            cout << "A "; 
        }
        cout << "\n";
        exit(0);
    }
    vector<string> ret(n, ""); 

    for (int i=0 ; i<k ; ++i) { 
        ret[first_yes + i] = make_new_name();
    }

    for (int i=first_yes+1 ; i<v.size() ; ++i) {
        if (v[i]) {
            ret[i + k - 1] = make_new_name();
        } else {
            ret[i + k - 1] = ret[i];
        }
    }

    for (int i=first_yes-1 ; i>=0 ; --i) {
        ret[i] = ret[i + k - 1];
    }

    for(int i=0 ; i<n ; ++i) {
        cout << ret[i] << " ";
    }
    cout << "\n";
}
