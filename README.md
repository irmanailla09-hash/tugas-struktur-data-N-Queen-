# tugas-struktur-data-N-Queen-
Program ini berisi 3 algoritma rekursif dan backtracking, yaitu:

N-Queen
Knight’s Tour
Knapsack

Program juga memiliki menu agar pengguna bisa memilih algoritma yang ingin dijalankan.

1. N-QUEEN
Pengertian

N-Queen adalah permainan menempatkan ratu (Queen) di papan catur berukuran N×N agar tidak saling menyerang.

Ratu dalam catur bisa menyerang:

horizontal
vertikal
diagonal

Jadi program harus mencari posisi yang aman untuk semua ratu.

Fungsi aman_queen()
def aman_queen(papan, baris, kolom):

Fungsi ini digunakan untuk mengecek apakah posisi ratu aman atau tidak.

Cara kerja:

Program mengecek:

apakah ada ratu di kolom yang sama
apakah ada ratu di diagonal yang sama

Jika aman → True
Jika tidak aman → False

Bagian pengecekan kolom
if papan[i] == kolom:
    return False

Artinya:
Jika ada ratu lain pada kolom yang sama, maka posisi tidak aman.

Bagian pengecekan diagonal
if abs(papan[i] - kolom) == abs(i - baris):
    return False

Artinya:
Jika jarak diagonal sama, maka ratu saling menyerang.

Fungsi n_queen()
def n_queen(papan, baris, n):

Fungsi ini adalah algoritma utama rekursif dan backtracking.

Cara kerja:
Program mencoba menaruh ratu satu per satu.
Jika posisi aman → lanjut ke baris berikutnya.
Jika tidak ada posisi yang cocok → kembali ke langkah sebelumnya (backtracking).
Kondisi selesai
if baris == n:
    return True

Artinya:
Jika semua baris sudah terisi ratu, maka solusi ditemukan.

Percobaan setiap kolom
for kolom in range(n):

Program mencoba semua kolom pada baris tertentu.

Menaruh ratu
papan[baris] = kolom

Artinya:
Ratu ditempatkan pada posisi yang aman.

Fungsi jalankan_nqueen()

Fungsi ini digunakan untuk:

meminta input ukuran papan
menjalankan algoritma
menampilkan hasil
Contoh output
Q . . .
. . Q .
. Q . .
. . . Q

Huruf Q = posisi ratu
Titik . = kotak kosong

2. KNIGHT TOUR
Pengertian

Knight’s Tour adalah permainan kuda catur yang harus mengunjungi semua kotak papan tepat satu kali.

Variabel langkah kuda
langkah_x = [2, 1, -1, -2, -2, -1, 1, 2]
langkah_y = [1, 2, 2, 1, -1, -2, -2, -1]

Digunakan untuk menentukan arah gerakan kuda.

Karena kuda memiliki 8 kemungkinan gerakan.

Fungsi aman_kuda()
def aman_kuda(x, y, papan):

Fungsi ini mengecek apakah langkah kuda valid.

Dicek:
tidak keluar papan
belum pernah dikunjungi

Jika aman → True

Fungsi knight_tour()
def knight_tour(papan, x, y, langkah):

Ini adalah fungsi utama rekursif.

Kondisi selesai
if langkah == N * N:
    return True

Artinya:
Jika semua kotak sudah dikunjungi, maka selesai.

Mencoba semua langkah
for i in range(8):

Program mencoba 8 arah gerakan kuda.

Menandai langkah
papan[next_x][next_y] = langkah

Artinya:
Kotak ditandai sudah dikunjungi.

Backtracking
papan[next_x][next_y] = -1

Jika langkah gagal, program kembali ke langkah sebelumnya.

Fungsi jalankan_knight()

Digunakan untuk:

membuat papan
meminta posisi awal
menjalankan algoritma
menampilkan hasil
Contoh hasil
0 59 38 ...

Angka menunjukkan urutan langkah kuda.

3. KNAPSACK
Pengertian

Knapsack adalah masalah memilih kombinasi barang agar total berat sesuai target.

Data barang
barang = [2, 5, 6, 9, 12, 14, 20]

Daftar berat barang yang tersedia.

Fungsi knapsack()
def knapsack(index, total, target, pilihan):

Fungsi ini mencari kombinasi barang menggunakan rekursif.

Kondisi berhasil
if total == target:

Artinya:
Jika total berat sama dengan target, kombinasi ditemukan.

Menampilkan hasil
print("Kombinasi ditemukan:", pilihan)

Program menampilkan kombinasi yang cocok.

Kondisi berhenti
if total > target or index >= len(barang):
    return

Program berhenti jika:

total melebihi target
semua barang sudah dicek
Ambil barang
knapsack(
    index + 1,
    total + barang[index],
    target,
    pilihan + [barang[index]]
)

Artinya:
Program mencoba memasukkan barang.

Tidak ambil barang
knapsack(
    index + 1,
    total,
    target,
    pilihan
)

Artinya:
Program mencoba tanpa mengambil barang.

4. MENU PROGRAM

Bagian ini digunakan untuk memilih algoritma.

while True:

Program akan terus berjalan sampai pengguna memilih keluar.

Pilihan menu
1. N-Queen
2. Knight Tour
3. Knapsack
4. Keluar
Jika pengguna memilih 1
jalankan_nqueen()

Program menjalankan N-Queen.

Jika pengguna memilih 2
jalankan_knight()

Program menjalankan Knight Tour.

Jika pengguna memilih 3
jalankan_knapsack()

Program menjalankan Knapsack.

Jika memilih 4
print("Program selesai")

Program berhenti.
