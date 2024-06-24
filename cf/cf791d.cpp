/* https://codeforces.com/contest/771/problem/C


 */
#include <bits/stdc++.h>
#include <iostream>
#include <cassert>
using namespace std;

int name_id = 0;

int subtract_modk(int a, int b, int k) {
    int ret = (k + (a - b) % k) % k;

    return ret;
}


// like the cf tutorial says, the simple problem of summing up the lengths of all the pair paths
// gets solved by adding up the contributions of each edge, knowing how many nodes are on each side of 
// the edge, the contribution is the product
// in this problem a path value is L/k rounded up, which is L+f/k where f is how much you need to add to L
// to make it k-divisible. this function sums up L+f (the answer is divided outside). (actually we return 2*L+2*f because of reasons)
// summing up L is solved as said, so what remains is summing up f for all uniques paths 
// we calculate the sum of f in two stages
// 1) paths that start at a highest node and only go down in the tree
// 2) paths that go down in two directions from the highest node on the path (highest = closest to the root)
// (we identify these by the top edge - since these paths go down in two directions, they're all identified by
// two edges, so they get double counted, so we multiply everything else by two and divide the answer by 2*k outside the function)
//
// figuring out f uses a recursively calculated subtree node count by distance to the subtree root, 
// built up in subtree_modk
long long df(vector<vector<int>> &tree, vector<int> &subtree_size, vector<vector<int>> &subtree_modk, 
             int node_a, int father, int k)  // df = depth first
{
    int n = tree.size();
    long long ret = 0; 
    subtree_size[node_a] = 1;

    subtree_modk[node_a].resize(0);
    subtree_modk[node_a].resize(k); // by default the node count by k modded distance from the subtree root is zeroed
    subtree_modk[node_a][0] = 1; // even if leaf, the root of the subtree is always at length zero from itself

    if (n == 1) { // leaf
        return 0;
    }

    //this has the recursive precalculation of all the sub-subtrees of the current subtree
    for (int node_b : tree[node_a]) {
        if (node_b == father) {
            continue;
        }
        ret += df(tree, subtree_size, subtree_modk, node_b, node_a, k); // paths that go inside that subtree only
        subtree_size[node_a] += subtree_size[node_b]; 
        ret += (long long)2 * (long long)subtree_size[node_b] * (long long)(n - subtree_size[node_b]);
        for (int i=0 ; i<k ; ++i) { 
            subtree_modk[node_a][(i + 1) % k] += subtree_modk[node_b][i]; 
        }

    }
    
    // add (twice) the round-up to k-divisible for paths that peak in the node node_a 
    for (int i=0 ; i<k ; ++i) { 
        ret += (long long)2 * subtree_modk[node_a][i] * subtract_modk(k, i, k);
    }

    //this has the ^ shaped paths that peak in the paths going down from node_a
    for (int node_b : tree[node_a]) {
        if (node_b == father) {
            continue;
        }
        // for every path going down:
        vector<int> rest_modk = subtree_modk[node_a]; 
        rest_modk[0] -= 1;
        for (int i=0 ; i<k ; ++i) {
            rest_modk[(i + 1) % k] -= subtree_modk[node_b][i];
        } //rest_modk has all the nodes in the node_a subtree minus those in the node_b sub-subtree, 
        // counted by distance to node_a mod k 
        for (int a=0 ; a<k ; ++a) {
            for (int b=0 ; b<k ; ++b) {
                long long delta = (long long)subtree_modk[node_b][b] * rest_modk[a] *
                    subtract_modk(k, (a + 1 + b), k);

                ret += delta;
            }
        }
    }
    return ret; 
}


int main(int argc, char* argv[]) {
    std::ios::sync_with_stdio(false);
    cin.tie(NULL);


	int n, k; 
	cin >> n >> k;

    vector<vector<int>> tree(n);
    for (int i=0 ; i<n-1 ; ++i) {
        int a, b;
        cin >> a >> b;
        tree[--a].push_back(--b);
        tree[b].push_back(a);
    }

    vector<int> sub_size(n);
    vector<vector<int>> sub_modk(n);
    long long ret = df(tree, sub_size, sub_modk, 0, -1, k);

    cout << ret / (2 * k) << "\n";
}
