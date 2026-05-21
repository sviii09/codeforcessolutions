#include <iostream>
using namespace std;

int main() {
    int m, n;
    cin >> m >> n;
    
    // Maximum dominoes = floor((m * n) / 2)
    cout << (m * n) / 2 << endl;
    
    return 0;
}