Judul Program:
Sistem Fuzzy Logic Inference (Mamdani) untuk Pemilihan 5 Restoran Terbaik

Deskripsi:
Program ini merupakan implementasi sistem berbasis Fuzzy Logic Inference model Mamdani untuk menentukan 5 restoran terbaik berdasarkan dua atribut, yaitu Kualitas Servis dan Harga. Sistem melakukan proses fuzzifikasi, inferensi menggunakan 9 aturan, serta defuzzifikasi menggunakan metode Center of Gravity (COG).

Kebutuhan Sistem:
Python 3.x
Library: pandas

Instalasi Library:
Jika pandas belum terinstal, jalankan:
pip install pandas

Struktur File:
program.py - file utama program
restoran.xlsx - data input (100 restoran)
peringkat.xlsx - output hasil program
README.txt - panduan penggunaan

Cara Menjalankan Program:

Pastikan semua file berada dalam satu folder.
Buka terminal / command prompt.
Jalankan perintah:
python program.py
Program akan:
Membaca file restoran.xlsx
Memproses data menggunakan sistem fuzzy
Menampilkan 5 restoran terbaik di terminal
Menyimpan hasil ke file peringkat.xlsx

Format Input:
File restoran.xlsx memiliki 3 kolom:

ID Restoran
Kualitas Servis (0–100)
Harga (22000–55000)

Format Output
File peringkat.xlsx berisi:
ID
Kualitas Servis
Harga
Skor Kelayakan (hasil defuzzifikasi)

Penjelasan Singkat Proses:

Fuzzifikasi:
Mengubah nilai crisp menjadi derajat keanggotaan fuzzy.
Inferensi:
Menggunakan 9 aturan dengan operator MIN (AND) dan MAX (OR).
Defuzzifikasi:
Menggunakan metode Center of Gravity (COG) dengan 1001 titik.