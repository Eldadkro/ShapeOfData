#include <vector>
namespace Combi {

using namespace std;
class Factorial {

  private:
    vector<size_t> factos;
    void calculate_factorial(size_t n);
  public:
    Factorial();
    size_t operator()(size_t n);

};


size_t factorial(size_t n);
size_t comb(size_t n, size_t k);
size_t perm(size_t n, size_t k);



} // namespace Factorials