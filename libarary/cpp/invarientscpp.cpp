#include "invarientscpp.h"

extern "C" {

    double q_extend_single(Nparray dists, size_t n, size_t q) {
        // cout << dists << ' '<< n<< ' '<< q<< endl;
        double res = Single_invarients().q_extend(dists, n, q);
        // cout << "in C: " << res << endl;
        return res;
    }

    double q_extend_multi(Nparray dists, size_t n, size_t q) {
        return Multi_invarients().q_extend(dists, n, q);
    }

    double excess_global_single(Nparray dists, size_t n) {
        return Single_invarients().excess_global(dists, n);
    }

    double q_packing_single(Nparray dists, size_t n, size_t q) {
        return Single_invarients().q_packing(dists, n, q) / 2;
    }

    void test() { cout << "hello world\n"; }

    void print_dists(Nparray dists, size_t n) {
        for (size_t i = 0; i < n; i++) {
            for (size_t j = 0; j < n; j++) {
                cout << dists[i * n + j] << " ";
            }
            cout << "\n";
        }
    }
}

Multi_invarients::Multi_invarients(size_t nthreads) : num_of_threads{nthreads} {
    pool = vector<thread>(num_of_threads);
}
Multi_invarients::Multi_invarients() : num_of_threads{NUM_THREARDS} {
    pool = vector<thread>(num_of_threads);
}

double Multi_invarients::q_extend(Nparray dists, size_t n, size_t q) { return 0; }

bool end(tup &t, size_t q) {
    for (size_t i = 0; i < q; i++)
        if (t[i] < q - 1)
            return false;
    return true;
}

void next_tup(tup &t, size_t n) {

    size_t i = 0;
    while ((t[i] = (t[i] + 1) % n) == 0 && i < n)
        i++;
}

double q_path_length(Nparray dists, size_t n, tup &t) {
    double length = 0;
    for (size_t i = 0; i < t.size() - 1; ++i) {
        if (dists[t[i] * n + t[i + 1]] == 0)
            return 0;
        length += dists[t[i] * n + t[i + 1]];
    }
    return length;
}

double Single_invarients::q_extend(Nparray dists, size_t n, size_t q) {

    // cout<<"in"<<endl;
    tup q_tup(static_cast<size_t>(q));
    for (size_t i = 0; i < q; ++i) {
        q_tup[i] = i;
    }
    Permutations_with_reps perms(n, q, q_tup, 0);
    // cout << q_tup.size() << endl;
    // print_tup(q_tup);

    double max_length = 0;
    double length = 0;
    while (!perms.end()) {
        // print_tup(q_tup);
        length = q_path_length(dists, n, q_tup);
        max_length = length > max_length ? length : max_length;
        q_tup = perms.next();
    }
    return max_length;
}

double Single_invarients::excess_global(Nparray dists, size_t n) {
    if (n < 3)
        return 0;
    vector<size_t> comb({0, 1, 2});
    Combinations combs(n, 3, comb, 0);
    double max_excess = 0;
    double curr_excess;
    while (!combs.end()) {
        curr_excess = excess(dists, comb, n);
        max_excess = max_excess > curr_excess ? max_excess : curr_excess;
        comb = combs.next();
    }
    return max_excess;
}

double excess(Nparray dists, tup &t, size_t n) {
    vector<double> tri_edges(3);
    tri_edges[0] = dists[t[0] * n + t[1]];
    tri_edges[1] = dists[t[1] * n + t[2]];
    tri_edges[2] = dists[t[0] * n + t[2]];
    if (tri_edges[0] == 0 || tri_edges[1] == 0 || tri_edges[2] == 0)
        return 0;
    sort(tri_edges.begin(), tri_edges.end());
    return tri_edges[2] + tri_edges[1] - tri_edges[0];
}

double Single_invarients::q_packing(Nparray dists, size_t n, size_t q) {
    if (n < q)
        q = n;
    if (q == 0)
        return 0;
    tup q_tup(static_cast<size_t>(q));
    for (size_t i = 0; i < q; ++i) {
        q_tup[i] = i;
    }
    Permutations_with_reps perms(n, q, q_tup, 0);
    double min_max_radius = 0;
    double radius = 0;
    while (!perms.end()) {
        // print_tup(q_tup);
        radius = max_radius(dists, q_tup, n);
        min_max_radius = radius > min_max_radius ? radius : min_max_radius;
        q_tup = perms.next();
    }
    return min_max_radius;
}

double max_radius(Nparray dists, tup &t, size_t n) {

    double radius = 0;
    for (size_t i = 0; i < t.size() - 1; i++) {
        for (size_t j = i + 1; j < t.size(); j++) {
            radius = radius > dists[i * n + j] ? radius : dists[i * n + j];
        }
    }
    return radius;
}

void print_tup(tup &t) {
    for (auto val : t) {
        cout << val << ' ';
    }

    cout << endl;
}
void test2() { cout << "hello world \n"; }

Permutations::Permutations(size_t _n, size_t _q, vector<size_t> start, size_t _limit = 0)
    : n{_n}, q{_q}, tup{start}, limit{_limit}, index{0} {}

const vector<size_t> &Permutations::next() {

    do {
        size_t i = q - 1;
        while ((tup[i] = (tup[i] + 1) % n) == 0 && i > 0)
            i--;
    } while (hascopies());
    return tup;
}

bool Permutations::end() {
    if (q == 0 || limit != 0 && limit == index)
        return true;
    size_t correct_value = n - 1;
    for (auto val : tup) {
        if (val != correct_value)
            return false;
        correct_value--;
    }
    return true;
}

bool Permutations::hascopies() {
    if (tup.size() == 0) {
        return false;
    }
    for (size_t i = 0; i < tup.size() - 1; ++i) {
        for (size_t j = i + 1; j < tup.size(); ++j) {
            if (tup[i] == tup[j])
                return true;
        }
    }
    return false;
}

bool Permutations::hascopies(pair<size_t, size_t> &res) {
    for (size_t i = 0; i < tup.size() - 1; ++i) {
        for (size_t j = i + 1; j < tup.size(); ++j) {
            if (tup[i] == tup[j]) {
                res = pair<size_t, size_t>(i, j);
                return true;
            }
        }
    }
    res = pair<size_t, size_t>(tup.size(), tup.size() + 1);
    return false;
}

Combinations::Combinations(size_t _n, size_t _q) : n{_n}, q{_q}, limit{0}, que() {
    for (size_t i = 0; i < q; i++) {
        que.push_back(i);
    }
}

Combinations::Combinations(size_t _n, size_t _q, vector<size_t> start, size_t _limit = 0)
    : n{_n}, q{_q}, limit{_limit}, que(start) {}

const vector<size_t> &Combinations::next() {
    // it is a version of DFS where we move lexicographiclly
    //  in a case where we reached the end of a branch we backtrack
    //  we return que as it is the combination
    //  but it is also the que for the DFS run
    size_t tmp = que.back();
    if (tmp == n - 1) {
        // backtrack
        size_t i;
        for (i = q - 1; i > 0 && que[i] == n - (q - i); i--)
            que.pop_back();
        que[i]++;
        for (size_t j = i + 1; j < q; j++)
            que.push_back(que[j - 1] + 1);
    } else {
        // no need to backtrack
        que[q - 1]++;
    }
    if (limit != 0) {
        index++;
    }
    return que;
}

bool Combinations::end() {
    // in case that we reached the limit or q is digenerate
    // other wise we simply check if we reached the last comination in lexicograph
    // manner
    if (q == 0 || limit != 0 && limit == index)
        return true;
    for (int i = 0; i < q; ++i)
        if (que[i] != n - q + i)
            return false;
    return true;
}

Permutations_with_reps::Permutations_with_reps(size_t _n, size_t _q, vector<size_t> start,
                                               size_t _limit = 0)
    : n{_n}, q{_q}, tup{start}, limit{_limit}, index{0} {}

bool Permutations_with_reps::end() {
    for (size_t i = 0; i < q; i++)
        if (tup[i] < n - 1)
            return false;
    return true;
}

const vector<size_t> &Permutations_with_reps::next() {
    size_t i = q - 1;
    while ((tup[i] = (tup[i] + 1) % n) == 0 && i > 0)
        i--;
    return tup;
}