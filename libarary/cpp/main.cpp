#include "invarientscpp.h"

int main() {
    vector<double> dists(static_cast<size_t>(9));
    cout<<dists.capacity()<<endl;
    cout<<dists.size()<<endl;
    double tmp[9] = {0, 2, 1, 2, 0, 1, 1, 1, 0};
    // auto p_dists = dists.data();
    for (size_t i = 0; i < 9; ++i) {
        dists[i] = tmp[i];
    }
    cout << endl;
    size_t n = 9;
    size_t q = 2;
    // print_dists(dists.data(),3);
    Single_invarients a;
    auto p = dists.data();
    cout << "enter" <<endl;
    double res = a.q_extend(tmp,3,2);
    cout << "end" <<endl;
    cout << res <<endl;
}