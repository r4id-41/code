// disini kita akan belajar tentang variable
// variable adalah tempat untuk menyimpan data
// di C++ kita harus mendeklarasikan tipe data dari variable yang kita buat, contoh:
// int umur = 17;
// variable umur bertipe data integer dan memiliki nilai 17
// dibawah ini adalah contoh penggunaan variable di C++

#include <iostream>
using namespace std;

int main() {
    string nama = "Kovix";
    int umur = 17;
    float berat_badan = 50.5;
    double tinggi_badan = 170.5;
    char jenis_kelamin = 'L';

    cout << "Namaku : " << nama << endl;
    cout << "Umurku : " << umur << " tahun" << endl;
    cout << "Berat badanku : " << berat_badan << " kg" << endl;
    cout << "Tinggi badanku : " << tinggi_badan << " cm" << endl;
    cout << "Jenis kelaminku : " << jenis_kelamin << endl;

    return 0;
}