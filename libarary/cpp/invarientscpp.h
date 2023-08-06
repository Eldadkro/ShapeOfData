#include <math.h>
// #include <python3.11/Python.h>

#include <algorithm>
#include <iostream>
#include <thread>
#include <unordered_map>
#include <utility>
#include <vector>
#define NUM_THREARDS 32

using namespace std;
typedef double *Nparray;
typedef vector<size_t> tup;

extern "C" {
    // interface for the python reader for single thread calculations
    double q_extend_single(Nparray, size_t, size_t);
    double excess_global_single(Nparray dists, size_t n);
    double q_packing_single(Nparray dists, size_t n, size_t q);

    // interface for the python reader for multi thread calculations
    double q_extend_multi(Nparray, size_t, size_t);
    // double excess_global_multi(Nparray);
    // double q_packing_multi(Nparray);

    void test();

    void print_dists(Nparray dists, size_t n);
}

class Single_invarients {

  public:
    Single_invarients() {}
    double q_extend(Nparray dists, size_t n, size_t q);
    double excess_global(Nparray dists, size_t n);
    double q_packing(Nparray dists, size_t n, size_t q);
};

class Multi_invarients {
  private:
    vector<thread> pool;
    size_t num_of_threads;
    vector<size_t> pos_element(size_t pos, size_t q, size_t n);
    void thread_q_extend(ThreadInput input);

  public:
    Multi_invarients(size_t);
    Multi_invarients();
    double q_extend(Nparray dists, size_t n, size_t q);
    //     // TODO
    double excess_global(Nparray dists, size_t n);
    double q_packing(Nparray dists, size_t n, size_t q);
};

struct ThreadInput {
    vector<size_t> start; 
    size_t n;
    size_t q;
    size_t limit;
    vector<double> *res; 
    size_t index;
    Nparray dists;
};

double q_path_length(Nparray dists, size_t n, tup &t);
double excess(Nparray dists, tup &t, size_t n);
double max_radius(Nparray dists, tup &t, size_t n);
// void next_tup(tup &t, size_t n);
// bool end(tup &t, size_t n);

void test2();

void print_tup(tup &t);

class Permutations {

  private:
    size_t n;
    size_t q;
    size_t limit, index;
    vector<size_t> tup;

    bool hascopies();
    bool hascopies(pair<size_t, size_t> &res);

  public:
    Permutations(size_t _n, size_t _q, vector<size_t> start, size_t _limit);
    const vector<size_t> &next();
    bool end();
};

class Combinations {
  private:
    size_t n;
    size_t q;
    size_t limit, index;
    vector<size_t> que;

  public:
    Combinations(size_t _n, size_t _q);
    Combinations(size_t _n, size_t _q, vector<size_t> start, size_t _limit);
    const vector<size_t> &next();
    bool end();
};

class Permutations_with_reps {
  private:
    size_t n;
    size_t q;
    size_t limit, index;
    vector<size_t> tup;

  public:
    Permutations_with_reps(size_t _n, size_t _q, vector<size_t> start, size_t _limit);
    const vector<size_t> &next();
    bool end();
};
