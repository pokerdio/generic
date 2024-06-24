#include <bits/stdc++.h>
#include <iostream>
#include <cassert>
using namespace std;

int lucky(int x) {
    while (x > 0) {
        if (x % 10 != 4 && x % 10 != 7) {
            return 0; 
        }
        x /= 10; 
    }
    return 1; 
}

int main(int argc, char* argv[]) {
    int n; 
	cin >> n;
    vector<vector<int>> neigh(n);

    for (int i=0 ; i<n ; ++i) {
        int u, v, w;
        cin >> u >> v >> w; 
        if (!lucky(w)) {
            neigh[u - 1].push_back(v - 1);
            neigh[v - 1].push_back(u - 1);
        } // we just keep the unlucky tree edges 
    }

    vector<int> visited(n, 0);
    long long ret = 0; 
    for (int i=0 ; i<n ; ++i) {
        if (visited[i]) {
            continue; 
        }
        vector<int> queue = {i};
        int count = 0; 

// we breadth/depth search each connected part of the graph left
// getting outside the current connected component  always passes a lucky edge
// getting from one node to another inside the connected component never passes a lucky edge
// all the nodes inside the component create valid triples towards all ordered pairs of nodes outside
// all valid triples are created this way
        while (!queue.empty()) { 
            int x = queue.back();
            queue.pop_back();
            count++; 

            visited[x] = 1;
            for (int y : neigh[x]) {
                if (!visited[y]) {
                    queue.push_back(y);
                    visited[y] = 1; 
                }
            }
        }
        ret += (long long)count * (n - count) * (n - count - 1);
    }
    cout << ret; 
}
