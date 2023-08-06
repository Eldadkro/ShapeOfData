#include "combi.h"

Combi::Factorial _factorial;

size_t Combi::factorial(size_t n) {
    size_t prod = 1;
    for (size_t i = 1; i <= n; i++) {
        prod *= i;
    }
    return prod;
    // return _factorial(n);
}

size_t Combi::comb(size_t n, size_t k) {
    size_t prod=1;
    for(size_t i=n;i>(n-k);--i) {
        prod *= i;
    }

    return  prod/factorial(k);
}

size_t Combi::perm(size_t n, size_t k) { return Combi::comb(n, k) * factorial(k); }

Combi::Factorial::Factorial() : factos(2) {
    factos[0] = 1;
    factos[1] = 1;
}

void Combi::Factorial::calculate_factorial(size_t n) {
    size_t prod = factos.back();
    for (size_t i = factos.size(); i < n+1; ++i) {
        prod *= i;
        factos.push_back(prod);
    }
}

size_t Combi::Factorial::operator()(size_t n) {
    if (factos.size() < n+1) {
        calculate_factorial(n);
    }
    return factos[n];
}
