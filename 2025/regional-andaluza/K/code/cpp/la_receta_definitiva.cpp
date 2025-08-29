#include <iostream>
#include <vector>
#include <cmath>
#include <map>
#include <tuple>
#include <algorithm>
#include <iomanip>
#include <set>
#include <limits>

using namespace std;

class UnionFind {
public:
    UnionFind(int size) {
        parent.resize(size);
        for (int i = 0; i < size; ++i) {
            parent[i] = i;
        }
    }

    int find(int node) {
        if (parent[node] != node) {
            parent[node] = find(parent[node]);
        }
        return parent[node];
    }

    bool union_sets(int node1, int node2) {
        int root1 = find(node1);
        int root2 = find(node2);

        if (root1 != root2) {
            parent[root2] = root1;
            return true;
        }
        return false;
    }

private:
    vector<int> parent;
};

double binary_search(double lower_bound, double upper_bound, auto is_feasible) {
    double left = lower_bound;
    double right = upper_bound;

    while (round(right * 100) - round(left * 100) > 0) {
        double mid = (left + right) / 2;
        auto [feasible, _] = is_feasible(mid);

        if (feasible) {
            right = mid;
        } else {
            left = mid;
        }
    }

    return right;
}

pair<int, vector<pair<int, int>>> maximal_spanning_tree(int n_nodes, vector<tuple<int, int, int>> &edges) {
    UnionFind uf(n_nodes);
    sort(edges.rbegin(), edges.rend());

    int max_tree_weight = 0;
    vector<pair<int, int>> used_edges;

    for (auto &[v, a, b] : edges) {
        if (uf.union_sets(a, b)) {
            max_tree_weight += v;
            used_edges.emplace_back(a, b);
        }
    }

    set<int> roots;
    for (int i = 0; i < n_nodes; ++i) {
        roots.insert(uf.find(i));
    }

    if (roots.size() > 1) {
        return {-1, {}};
    }

    return {max_tree_weight, used_edges};
}

pair<bool, vector<pair<int, int>>> is_feasible(
    map<pair<int, int>, int> &views,
    vector<vector<double>> &distances,
    double max_distance,
    int s
) {
    int n = distances.size();
    vector<tuple<int, int, int>> edges;

    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            if (distances[i][j] <= max_distance) {
                int view = views.count({i, j}) ? views[{i, j}] : 0;
                edges.emplace_back(view, i, j);
            }
        }
    }

    auto [max_tree_weight, used_edges] = maximal_spanning_tree(n, edges);
    return {s <= max_tree_weight, used_edges};
}

pair<bool, vector<pair<int, int>>> is_feasible_wrapper(
    map<pair<int, int>, int> &views,
    vector<vector<double>> &distances,
    double max_distance,
    int s
) {
    return is_feasible(views, distances, max_distance, s);
}

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n, x, y, s;
        cin >> n >> x >> y >> s;

        vector<pair<int, int>> nodes = {{x, y}};
        for (int i = 0; i < n; ++i) {
            int a, b;
            cin >> a >> b;
            nodes.emplace_back(a, b);
        }

        double min_distance = numeric_limits<double>::infinity();
        double max_distance = 0;
        vector<vector<double>> distances(n + 1, vector<double>(n + 1, 0));

        for (int i = 0; i <= n; ++i) {
            for (int j = i + 1; j <= n; ++j) {
                double distance = hypot(nodes[i].first - nodes[j].first, nodes[i].second - nodes[j].second);
                distances[i][j] = distance;

                min_distance = min(min_distance, distance);
                max_distance = max(max_distance, distance);
            }
        }

        int m;
        cin >> m;
        map<pair<int, int>, int> views;

        for (int i = 0; i < m; ++i) {
            int a, b, v;
            cin >> a >> b >> v;
            if (a < b) {
                views[{a, b}] = v;
            } else {
                views[{b, a}] = v;
            }
        }

        auto [feasible, _] = is_feasible(views, distances, max_distance, s);
        if (!feasible) {
            cout << "-1.00" << endl;
        } else {
            double upper_bound = binary_search(
                min_distance - 1,
                2 * max_distance,
                [&](double d) { return is_feasible_wrapper(views, distances, d, s); }
            );

            double result = 0;
            for (int i = 0; i <= n; ++i) {
                for (int j = i + 1; j <= n; ++j) {
                    double d = distances[i][j];
                    if (d <= upper_bound && result < d) {
                        result = d;
                    }
                }
            }

            cout << fixed << setprecision(2) << result << endl;
        }
    }

    return 0;
}