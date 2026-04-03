#include <iostream>
#include <cmath>
using namespace std;

double g(int n, int r) {
    if (n == 0)
        return 1;

    return pow(r, n) + g(n - 1, r);
}

int main() {
    int n;
    int r;

    cout << "n: ";
    cin >> n;

    cout << "r: ";
    cin >> r;

    cout << "Sonuc: " << g(n, r) << endl;

    return 0;
}