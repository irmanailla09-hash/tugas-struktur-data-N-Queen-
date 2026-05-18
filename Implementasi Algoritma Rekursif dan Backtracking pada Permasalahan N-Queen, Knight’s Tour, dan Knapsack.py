# ==============================
# PROGRAM REKURSIF & BACKTRACKING
# 1. N-Queens
# 2. Knight's Tour
# 3. Knapsack
# ==============================

# =====================================
# 1. N-QUEENS
# =====================================

def aman_queen(papan, baris, kolom):
    for i in range(baris):
        if papan[i] == kolom:
            return False

        if abs(papan[i] - kolom) == abs(i - baris):
            return False

    return True


def n_queen(papan, baris, n):
    if baris == n:
        return True

    for kolom in range(n):
        if aman_queen(papan, baris, kolom):
            papan[baris] = kolom

            if n_queen(papan, baris + 1, n):
                return True

    return False


def jalankan_nqueen():
    n = int(input("Masukkan ukuran papan N-Queen: "))
    papan = [-1] * n

    if n_queen(papan, 0, n):
        print("\nSolusi N-Queen:\n")

        for i in range(n):
            for j in range(n):
                if papan[i] == j:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")
            print()
    else:
        print("Tidak ada solusi")


# =====================================
# 2. KNIGHT TOUR
# =====================================

N = 8

langkah_x = [2, 1, -1, -2, -2, -1, 1, 2]
langkah_y = [1, 2, 2, 1, -1, -2, -2, -1]


def aman_kuda(x, y, papan):
    return 0 <= x < N and 0 <= y < N and papan[x][y] == -1


def knight_tour(papan, x, y, langkah):
    if langkah == N * N:
        return True

    for i in range(8):
        next_x = x + langkah_x[i]
        next_y = y + langkah_y[i]

        if aman_kuda(next_x, next_y, papan):
            papan[next_x][next_y] = langkah

            if knight_tour(papan, next_x, next_y, langkah + 1):
                return True

            papan[next_x][next_y] = -1

    return False


def jalankan_knight():
    papan = [[-1 for i in range(N)] for j in range(N)]

    x = int(input("Masukkan posisi awal x (0-7): "))
    y = int(input("Masukkan posisi awal y (0-7): "))

    papan[x][y] = 0

    if knight_tour(papan, x, y, 1):
        print("\nHasil Knight Tour:\n")

        for baris in papan:
            for angka in baris:
                print(f"{angka:2}", end=" ")
            print()
    else:
        print("Tidak ada solusi")


# =====================================
# 3. KNAPSACK
# =====================================

barang = [2, 5, 6, 9, 12, 14, 20]


def knapsack(index, total, target, pilihan):
    if total == target:
        print("Kombinasi ditemukan:", pilihan)
        return

    if total > target or index >= len(barang):
        return

    # ambil barang
    knapsack(
        index + 1,
        total + barang[index],
        target,
        pilihan + [barang[index]]
    )

    # tidak ambil barang
    knapsack(
        index + 1,
        total,
        target,
        pilihan
    )


def jalankan_knapsack():
    target = int(input("Masukkan target berat: "))

    print("\nKombinasi yang cocok:")
    knapsack(0, 0, target, [])


# =====================================
# MENU PROGRAM
# =====================================

while True:
    print("\n===== MENU =====")
    print("1. N-Queen")
    print("2. Knight Tour")
    print("3. Knapsack")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        jalankan_nqueen()

    elif pilihan == "2":
        jalankan_knight()

    elif pilihan == "3":
        jalankan_knapsack()

    elif pilihan == "4":
        print("Program selesai")
        break

    else:
        print("Pilihan tidak valid")