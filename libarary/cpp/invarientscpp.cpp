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
        q_tup[i] = 0;
    }
    // cout << q_tup.size() << endl;
    // print_tup(q_tup);

    double max_length = 0;
    double length = 0;
    while (!end(q_tup, q)) {
        // print_tup(q_tup);
        length = q_path_length(dists, n, q_tup);
        max_length = length > max_length ? length : max_length;
        next_tup(q_tup, n);
    }
    return max_length;
    return 0;
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
    size_t i = 0;
    while (hascopies())
        while ((tup[i] = (tup[i] + 1) % n) == 0 && i < n)
            i++;
    ++index;
    return tup;
}

bool Permutations::end() {
    if (q == 0 || limit != 0 && limit == index)
        return true;
    for (auto val : tup)
        if (val < n - 1)
            return false;
    return true;
}

bool Permutations::hascopies() {
    if (tup.size() == 0) {
        return false;
    }
    for (size_t i = 1; i < tup.size(); ++i) {
        for (size_t j = 0; j < i; ++j) {
            if (tup[i] == tup[j])
                return true;
        }
    }
    return false;
}

Combinations::Combinations(size_t _n, size_t _q) : n{_n}, q{_q}, limit{0}, que(q) {
    for (size_t i = 0; i < q; i++) {
        que.push_back(n - (q - i));
    }
}

Combinations::Combinations(size_t _n, size_t _q, vector<size_t> start, size_t _limit=0)
    : n{_n}, q{_q}, limit{_limit}, que(start) {}

const vector<size_t> &Combinations::next() {
    // it is a version of DFS where we move lexicographiclly
    //  in a case where we reached the end of a branch we backtrack
    //  we return que as it is the combination
    //  but it is also the que for the DFS run
    if (que.back() == n - 1) {
        // backtrack
        size_t i;
        for (i = q - 1; i > 0 && que[i] == n - (q - i); i--)
            que.pop_back();
        que[i]++;
        for (size_t j = i + 1; j < q; j++)
            que.push_back(que[i] + 1);
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
    // other wise we simply check if we reached the last comination in lexicograph manner
    if (q == 0 || limit != 0 && limit == index)
        return true;
    for (int i = 0; i < q; ++i)
        if (que[i] != n - q + i)
            return false;
    return true;
}