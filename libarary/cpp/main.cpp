#include "combi.h"
#include "invarientscpp.h"
#include <chrono>

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

// TODO not ready
vector<size_t> Multi_invarients::combi_element(size_t pos, size_t q, size_t n) {
    vector<size_t> combi(q);
    for (size_t i = 0; i < q-1; ++i) {
        
    }
}

int main() {
    size_t n = 4;
    size_t q = 3;
    vector<double> dists(static_cast<size_t>(n * n));
    cout << Combi::comb(n,q) << endl;

    // // auto p_dists = dists.data();
    // for (size_t i = 0; i < n-1; ++i) {
    //     dists[i*n + i+1] = 1;
    //     dists[(i+1)*n + i] = 1;
    // }
    // cout << endl;

    // print_dists(dists.data(),n);
    // Single_invarients a;

    // cout << "enter single" << endl;
    // double res_single = a.q_extend(dists.data(), n,q);
    // cout << "end" << endl;
    // cout << res_single << endl;

    // Multi_invarients b;
    // cout << "enter multi" << endl;
    // double res_multi = b.q_extend(dists.data(), n, q);
    // cout << "end" << endl;
    // cout << res_multi << endl;

    // // test_perms_with_rep();
    // // test_perms();
    // // test_combs();
    // size_t n = 3000, q = 5;
    // vector<size_t> curp({0, 1, 2});
    // Permutations_with_reps permsr(static_cast<size_t>(n), static_cast<size_t>(q), curp,
    //   0);
    // size_t tmp = Combi::perm(n,q);
    // cout << "prems with reps " << tmp << " : \n";
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