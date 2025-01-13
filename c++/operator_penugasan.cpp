// operator penugasan adalah operator yang digunakan untuk memberikan nilai pada variabel
// dibawah ini adalah tabel operator penugasan yang sering digunakan
// Nama Operator                : penjelasan
// Pengisian Nilai              : =, seperti a = 10
// Pengisian dan Penambahan     : +=, seperti a += 10
// Pengisian dan Pengurangan	: -=, seperti a -= 10
// Pengisian dan Perkalian	    : *=, seperti a *= 10
// Pengisian dan Pembagian	    : /=, seperti a /= 10
// Pengisian dan Sisa bagi	    : %=, seperti a %= 10
// Pengisian dan shift left	    : <<=, seperti a <<= 10
// Pengisian dan shift right	: >>=, seperti a >>= 10
// Pengisian dan bitwise AND	: &=, seperti a &= 10
// Pengisian dan bitwise OR	    : |=, seperti a |= 10
// Pengisian dan bitwise XOR	: ^=, seperti a ^= 10
// Pengisian dan bitwise NOT	: ~, seperti a = ~10

#include <iostream>
using namespace std;

int main() {
    int a = 20;
    int b = 10;

    cout << "a: " << a << endl;
    cout << "b: " << b << endl;

    a += b;
    cout << "a += b: " << a << endl; // a ditambah b dan hasilnya disimpan di a

    a -= b;
    cout << "a -= b: " << a << endl; // a dikurang b dan hasilnya disimpan di a

    a *= b;
    cout << "a *= b: " << a << endl; // a dikali b dan hasilnya disimpan di a

    a /= b;
    cout << "a /= b: " << a << endl; // a dibagi b dan hasilnya disimpan di a

    a %= b;
    cout << "a %= b: " << a << endl;

    a <<= b;
    cout << "a <<= b: " << a << endl;

    a >>= b;
    cout << "a >>= b: " << a << endl;

    a &= b;
    cout << "a &= b: " << a << endl;
    
    return 0;
}