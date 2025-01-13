// operator aritmatika adalah operator yang digunakan untuk melakukan operasi matematika
// pada c++ terdapat beberapa operator aritmatika yaitu:
// 1. operator penjumlahan (+) -> operator ini digunakan untuk melakukan penjumlahan
// 2. operator pengurangan (-) -> operator ini digunakan untuk melakukan pengurangan
// 3. operator perkalian (*) -> operator ini digunakan untuk melakukan perkalian
// 4. operator pembagian (/) -> operator ini digunakan untuk melakukan pembagian
// 5. operator modulus (%) -> operator ini digunakan untuk mendapatkan sisa hasil bagi
// dibawah ini adalah operator aritmatika pada c++ :


#include <iostream>
using namespace std;

int main(){

    int a, b;

    cout << "Inputkan nilai a: ";
    cin >> a;

    cout << "Inputkan nilai b: ";
    cin >> b;

    cout << "Hasil a + b: " << a + b << endl;
    cout << "Hasil a - b: " << a - b << endl;
    cout << "Hasil a * b: " << a * b << endl;
    cout << "Hasil a / b: " << a / b << endl;
    cout << "Hasil a % b: " << a % b << endl;

    return 0;
}

// hasil dari operasi aritmatika bisa berupa bilangan bulat maupun bilangan desimal
// tergantung dari tipe data yang digunakan
// jika tipe data integer maka hasilnya akan tetap berupa bilangan bulat, meskipun hasilnya aslinya bilangan desimal.
// jika tipe data float atau double maka hasilnya akan berupa bilangan desimal.

// dibawah ini adalah contoh penggunaan operator aritmatika dengan tipe data float
// int main(){

//     float a, b;

//     cout << "Inputkan nilai a: ";
//     cin >> a;

//     cout << "Inputkan nilai b: ";
//     cin >> b;

//     cout << "Hasil a + b: " << a + b << endl;
//     cout << "Hasil a - b: " << a - b << endl;
//     cout << "Hasil a * b: " << a * b << endl;
//     cout << "Hasil a / b: " << a / b << endl;
//     // cout << "Hasil a % b: " << a % b << endl;
//     // operator modulus tidak bisa digunakan untuk tipe data float

//     return 0;
// }