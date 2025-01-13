// operator pembanding adalah operator yang digunakan untuk membandingkan dua nilai
// operator pembanding akan menghasilkan nilai boolean, yaitu true atau false (1 atau 0)
// pada C++ terdapat 6 operator pembanding, yaitu:
// 1. operator sama dengan (==) -> operator ini digunakan untuk membandingkan apakah dua nilai sama
// 2. operator tidak sama dengan (!=) -> operator ini digunakan untuk membandingkan apakah dua nilai tidak sama
// 3. operator lebih besar dari (>) -> operator ini digunakan untuk membandingkan apakah nilai pertama lebih besar dari nilai kedua
// 4. operator lebih kecil dari (<) -> operator ini digunakan untuk membandingkan apakah nilai pertama lebih kecil dari nilai kedua
// 5. operator lebih besar sama dengan (>=) -> operator ini digunakan untuk membandingkan apakah nilai pertama lebih besar atau sama dengan nilai kedua
// 6. operator lebih kecil sama dengan (<=) -> operator ini digunakan untuk membandingkan apakah nilai pertama lebih kecil atau sama dengan nilai kedua
// dibawah ini adalah contoh penggunaan operator pembanding pada C++:

#include <iostream>
using namespace std;

int main(){

    int a, b;

    cout << "Masukkan nilai a: ";
    cin >> a;

    cout << "Masukkan nilai b: ";
    cin >> b;

    cout << "Apakah a sama dengan b : " << (a == b) << endl;
    cout << "Apakah a tidak sama dengan b : " << (a != b) << endl;
    cout << "Apakah a lebih besar dari b : " << (a > b) << endl;
    cout << "Apakah a lebih kecil dari b : " << (a < b) << endl;
    cout << "Apakah a lebih besar sama dengan b : " << (a >= b) << endl;
    cout << "Apakah a lebih kecil sama dengan b : " << (a <= b) << endl;

    return 0;
}