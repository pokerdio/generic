#include <bits/stdc++.h>
#include <iostream>
#include <cassert>
using namespace std;


int main(int argc, char* argv[]) {
	long long n, m; 
	cin >> n >> m;
    vector<vector<long long>> neigh(n, vector<long long>(0, 0));
    for (long long i=0 ; i<m ; ++ i) {
        long long a, b;
        cin >> a >> b;
        neigh[--a].push_back(--b);
        neigh[b].push_back(a);
    }

    long long color = 0;
    vector<long long> col(n, -1);

    for (long long i=0 ; i<n ; ++i) {
        if (-1 != col[i]) {
            continue;
        }

        long long node_count = 0;
        long long link_count = 0;
        vector<long long> q;
        q.push_back(i);
        col[i] = 0;
        while (q.size()) {
            long long node = q.back();
            q.pop_back();
            node_count++;
            link_count += neigh[node].size();

            for (long long next : neigh[node]) {
                if (col[next] == -1) {
                    col[next] = color;
                    q.push_back(next);
                }
            }
        }

        if (link_count < node_count * (node_count - 1)) {
            cout << "NO\n";
            exit(0);
        }
        color++;
    }

    cout << "YES\n";
}
