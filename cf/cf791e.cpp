#include <bits/stdc++.h>
#include <iostream>
#include <cassert>
using namespace std;

//dp starting from left to right over the word positions

//imagine all the letter swapping in the optimal solution, identified as which letter is moved
//whatever order we move the letters in, the result is the same, so long as a certain letter moves
//in its preferred direction the correct number of times

//so we're free to move first the letter that goes to the leftmost position



void pv(vector<int> &v) {
    for (int i=0 ; i<v.size() ; ++i) { 
        cout << v[i] << " ";
    }
    cout << "\n";
}

#define K 2
#define V 1
#define X 0

void dp_optimize(int old_val, int delta, int& new_val) {
    if (old_val < 0) {
        return; // the "old" position isn't valid
    }
    if (new_val < 0 || (old_val + delta < new_val)) {
        new_val = old_val + delta;
    }
}

int main(int argc, char* argv[]) {
	long long n; 
	cin >> n;
    string s;
    cin >> s;

    vector<int> word;
    int nk=0, nv=0, nx=0; 

    vector<int> posk, posx, posv; 
    vector<int> countk, countx, countv;

    for (int i=0 ; i<n ; ++i) {
        if (s[i] == 'K') {
            nk += 1;
            word.push_back(2);
            posk.push_back(i);
        } else if (s[i] == 'V') {
            nv += 1;
            word.push_back(1);
            posv.push_back(i);
        } else {
            nx += 1;
            word.push_back(0);
            posx.push_back(i);
        }
        countk.push_back(nk);
        countv.push_back(nv);
        countx.push_back(nx);
    }
    vector<vector<vector<vector<int>>>> dp (nx + 1, vector<vector<vector<int>>> (nk + 1, vector<vector<int>>(nv + 1, vector<int>(2, -1))));

    dp[0][0][0][0] = 0;
    int cost; 
    for (int i=1 ; i<=n ; ++i) {
        for (int k=0 ; k<min(i, nk+1) ; ++k) {
            for (int v=0 ; v<min(i-k, nv+1) ; ++v) {
                int x = i - k - v - 1; 
                if (x > nx) {
                    continue;
                }
                // at this point we get all x/k/v triplets that sum to i-1 and are within 
                // the total available count of each letter in the word
                assert(x >= 0);

// add X 
                if (x < nx) {
                    int pos = posx[x];
                    cost = pos - i + 1;
                    if (countk[pos] < k) {
                        cost += k - countk[pos];
                    }
                    if (countv[pos] < v) {
                        cost += v - countv[pos];
                    }
                    assert(cost >= 0);
                    dp_optimize(dp[x][k][v][0], cost, dp[x+1][k][v][0]);
                    dp_optimize(dp[x][k][v][1], cost, dp[x+1][k][v][0]);
                }

// add K
                if (k < nk) {
                    int pos = posk[k];
                    cost = pos - i + 1;
                    if (countx[pos] < x) {
                        cost += x - countx[pos];
                    }
                    if (countv[pos] < v) {
                        cost += v - countv[pos];
                    }
                    assert(cost >= 0);
                    dp_optimize(dp[x][k][v][0], cost, dp[x][k+1][v][0]);
                }

// add V
                if (v < nv) {
                    int pos = posv[v];
                    cost = pos - i + 1;
                    if (countx[pos] < x) {
                        cost += x - countx[pos];
                    }
                    if (countk[pos] < k) {
                        cost += k - countk[pos];
                    }
                    assert(cost >= 0);
                    dp_optimize(dp[x][k][v][0], cost, dp[x][k][v+1][1]);
                    dp_optimize(dp[x][k][v][1], cost, dp[x][k][v+1][1]);
                }
            }
        }
    }
    int a =  dp[nx][nk][nv][0];
    int b = dp[nx][nk][nv][1];
    if (a < 0) {
        a = b;
    }
    if (b < 0) {
        b = a;
    }
    cout << min(a, b) << "\n";
}
