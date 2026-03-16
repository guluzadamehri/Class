#include <iostream>
using namespace std;
int main() {
    double a, b;
    cin >> a >> b;
    if (a == 0) {
        if (b == 0) cout << "Sonsuz hell" << endl;
        else cout << "Hell yoxdur" << endl;
    } else {
        cout << b / a << endl;
    }
    return 0;
}
