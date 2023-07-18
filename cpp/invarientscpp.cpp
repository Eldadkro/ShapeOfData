#include "invarientscpp.h"

extern "C" {

    double q_extend_single(Nparray dists, size_t n, size_t q) {
        return Single_invarients{}.q_extend(dists, n, q);
    }

    double q_extend_multi(Nparray dists, size_t n, size_t q) {
        return Multi_invarients{}.q_extend(dists, n, q);
    }
}

Multi_invarients::Multi_invarients(size_t nthreads) : num_of_threads{nthreads} {
    pool = vector<thread>{num_of_threads};
}
Multi_invarients::Multi_invarients() : num_of_threads{NUM_THREARDS} {
    pool = vector<thread>{num_of_threads};
}


double Multi_invarients::q_extend(Nparray dists, size_t n, size_t q) {
    return 0;
}

bool end(tup &t, size_t n) {
    for (size_t i = 0; i < n; i++)
        if (t[i] < n)
            return false;
    return true;
}

void next_tup(tup &t, size_t n){

    size_t i=0;
    while((t[i] = (t[i]+1)%n) == 0)
        ++i;
}

double q_path_length(Nparray dists, size_t n, tup t) {
    double length = 0;
    for (size_t i = 0; i < t.size() - 1; ++i) {
        if (dists[i * n + (i + 1)] == 0)
            return 0;
        length += dists[i * n + (i + 1)];
    }
    return length;
}


double Single_invarients::q_extend(Nparray dists, size_t n, size_t q) {

    tup q_tup{static_cast<size_t>(q)};
    for (size_t i = 0; i < q; ++i) {
        q_tup[i] = 0;
    }
    double max_length = 0;
    double length = 0;
    // change to something better
    while (!end(q_tup, n)) {
        length = q_path_length(dists, n, q_tup);
        max_length = length > max_length ? length : max_length;
        next_tup(q_tup,n);
    }
    return max_length;
}




