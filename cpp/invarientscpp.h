#include <math.h>
#include <python3.11/Python.h>

#include <iostream>
#include <thread>
#include <vector>

using namespace std;
typedef float *Nparray;
typedef vector<size_t> tup;

extern "C" {
    // interface for the python reader for single thread calculations
    double q_extend_single(Nparray, size_t, size_t);
    // double excess_global_single(Nparray);
    // double q_packing_single(Nparray);

    // interface for the python reader for multi thread calculations
    double q_extend_multi(Nparray, size_t, size_t);
    // double excess_global_multi(Nparray);
    // double q_packing_multi(Nparray);
}

class Single_invarients {

  public:
    double q_extend(Nparray, size_t, size_t);
    // TODO
    // double excess_global(Nparray);
    // double q_packing(Nparray);
};

class Multi_invarients {
  private:
    vector<thread> pool;
    size_t num_of_threads;

  public:
    Multi_invarients(size_t);
    double q_extend(Nparray, size_t, size_t);
    // TODO
    //  double excess_global(Nparray);
    //  double q_packing(Nparray);
};
