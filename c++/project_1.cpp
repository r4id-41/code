#include <iostream>
using namespace std;

int main() {
    string nama;
    int umur;
    string alamat;
    string hobi;
    char jenis_kelamin;

    cout << "Masukkan nama: ";
    getline(cin, nama);

    cout << "Masukkan umur: ";
    cin >> umur;

    cout << "Masukkan alamat: ";
    cin.ignore();
    getline(cin, alamat);

    cout << "Masukkan hobi: ";
    getline(cin, hobi);

    cout << "Masukkan jenis kelamin (L/P): ";
    cin >> jenis_kelamin;

    cout << "Halo" << nama << " Sekarang kamu berusia ";
    cout << umur << " tahun dan berjenis kelamin " << jenis_kelamin << endl;
    cout << "Alamat kamu di " << alamat << " dan hobi kamu adalah " << hobi << endl;

    return 0;
}