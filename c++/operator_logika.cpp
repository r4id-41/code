// operator logika adalah operator yang digunakan untuk menggabungkan dua atau lebih ekspresi logika.
// Operator logika terdiri dari tiga jenis, yaitu AND, OR, dan NOT.
// AND (&&) : - Operator AND digunakan untuk menggabungkan dua ekspresi logika. 
//            - Operator ini akan menghasilkan nilai benar jika kedua ekspresi bernilai benar.
// OR (||) : - Operator OR digunakan untuk menggabungkan dua ekspresi logika.
//           - Operator ini akan menghasilkan nilai benar jika salah satu atau kedua ekspresi bernilai benar.
// NOT (!) : - Operator NOT digunakan untuk membalikkan nilai dari suatu ekspresi logika.
//           - Operator ini akan menghasilkan nilai benar jika ekspresi bernilai salah, dan sebaliknya.
// contoh penggunaan operator logika

#include <iostream>
using namespace std;

int main() {
    int a = 5;
    int b = 3;
    int c;

    // operator logika AND
    cout << (a > b && b == c) << endl; // 0

    // operator logika OR
    cout << (a > b || b == c) << endl; // 1

    // operator logika NOT
    cout << !(a > b) << endl; // 0

    return 0;
}