#include <chrono>
#include "invarientscpp.h"
#include "combi.h"

void pv(vector<size_t> v) {
    cout << "(";
    for (auto a : v)
        cout << a << ", ";
    cout << ")" << endl;
}

void test_perms() {
    cout << "prems: \n";
    size_t n = 4, q = 3;
    vector<size_t> curp({0, 1, 2});
    Permutations perms(static_cast<size_t>(n), static_cast<size_t>(q), curp, 0);
    while (!perms.end()) {
        pv(curp);
        curp = perms.next();
    }
    pv(curp);
}

void test_perms_with_rep() {
    cout << "prems with reps: \n";
    size_t n = 4, q = 3;
    vector<size_t> curp({0, 1, 2});
    Permutations_with_reps perms(static_cast<size_t>(n), static_cast<size_t>(q), curp, 0);
    while (!perms.end()) {
        pv(curp);
        curp = perms.next();
    }
    pv(curp);
}

void test_combs() {

    cout << "combs: \n";
    size_t n = 4, q = 3;
    vector<size_t> curp({0, 1, 2});
    Combinations perms(static_cast<size_t>(n), static_cast<size_t>(q), curp, 0);
    while (!perms.end()) {
        pv(curp);
        curp = perms.next();
    }
    pv(curp);
}
int main() {
    // vector<double> dists(static_cast<size_t>(9));
    // cout << dists.capacity() << endl;
    // cout << dists.size() << endl;
    // double tmp[9] = {0, 2, 1, 2, 0, 1, 1, 1, 0};
    // // auto p_dists = dists.data();
    // for (size_t i = 0; i < 9; ++i) {
    //     dists[i] = tmp[i];
    // }
    // cout << endl;
    // size_t n = 9;
    // size_t q = 2;
    // // print_dists(dists.data(),3);
    // Single_invarients a;
    // auto p = dists.data();
    // cout << "enter" << endl;
    // double res = a.q_extend(tmp, 3, 2);
    // cout << "end" << endl;
    // cout << res << endl;

    // test_perms_with_rep();
    // test_perms();
    // test_combs();
    size_t n = 3000, q = 5;
    vector<size_t> curp({0, 1, 2});
    Permutations_with_reps permsr(static_cast<size_t>(n), static_cast<size_t>(q), curp,
                                  0);
    size_t tmp = Combi::perm(n,q);                                  
    cout << "prems with reps " << tmp << " : \n";
    // auto startpr = std::chrono::steady_clock::now();
    // while (!permsr.end()) {
    //     // pv(curp);
    //     curp = permsr.next();
    // }
    // auto endpr = std::chrono::steady_clock::now();
    // std::cout << "perms with reps = ";
    // std::cout
    //     << std::chrono::duration_cast<std::chrono::microseconds>(endpr -
    //     startpr).count()
    //     << "[µs]" << std::endl;

    // Combinations combs(static_cast<size_t>(n), static_cast<size_t>(q));
    // vector<size_t> curc({0, 1, 2});
    // cout << "combs: \n";
    // auto startc = std::chrono::steady_clock::now();
    // while (!combs.end()) {
    //     // pv(curc);
    //     curc = combs.next();
    // }
    // auto endc = std::chrono::steady_clock::now();

    // std::cout << "combs = ";
    // std::cout
    //     << std::chrono::duration_cast<std::chrono::microseconds>(endc - startc).count()
    //     << "[µs]" << std::endl;
    // curp = {0, 1, 2};
    // cout << curp.size() << endl;
    // Permutations perms(static_cast<size_t>(n), static_cast<size_t>(q), curp, 0);
    // cout << "prems: \n";
    // auto startp = std::chrono::steady_clock::now();
    // while (!perms.end()) {
    //     // pv(curp);
    //     curp = perms.next();
    // }
    // auto endp = std::chrono::steady_clock::now();
    // std::cout << "prems = ";
    // std::cout
    //     << std::chrono::duration_cast<std::chrono::microseconds>(endp - startp).count()
    //     << "[µs]" << std::endl;
}