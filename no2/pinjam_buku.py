import time
"""Pinjam Buku (dengan Subprogram)"""
# definisi fungsi
def cari_kandidat(koneksi, umur, sudah_pinjam, N):
    # pindah peminjam
    i = 0
    kandidat = -1
    umur_min = 999999
    while i < N:
        # cek koneksi dan status pinjam
        if (koneksi[i] == 1) and (sudah_pinjam[i] == 0):
            # Cek umur termuda
            if umur[i] < umur_min:
                umur_min = umur[i]
                kandidat = i
        i += 1
    return kandidat  
# program utama
# input
N = int(input("Masukkan jumlah orang: "))
matrix = []
umur = [0 for _ in range(N)]
sudah_pinjam = [0 for _ in range(N)]
riwayat_pinjam = []
for i in range(N):
    col = [0]*N
    matrix += [col]

for y in range(N):
    for x in range(N):
        val = int(input(f'Masukkan isi matrix ketetanggaan untuk koordinat ({x},{y}): '))
        matrix[y][x] = val
    print('================================')

for i in range(N):
    val_umur = int(input(f'Masukkan umur untuk index {i}: '))
    umur[i] = val_umur

index_pinjam = int(input('Masukkan index tempat awal buku berada: '))
awal = time.perf_counter()
sudah_pinjam[index_pinjam] = 1
riwayat_pinjam += [index_pinjam]
top = 0
print('Urutan index peminjaman buku: ', end='')
print(index_pinjam, end='')
while True:
    koneksi = matrix[index_pinjam]
    kandidat = cari_kandidat(koneksi, umur, sudah_pinjam, N)
    if kandidat != -1:
        index_pinjam = kandidat
        sudah_pinjam[index_pinjam] = 1
        riwayat_pinjam += [index_pinjam]
        top += 1
        print(" ->", index_pinjam, end="")
    else:
        # Pengecekan apakah semua orang sudah pernah meminjam
        jumlah = 0
        for items in sudah_pinjam:
            jumlah += items
        # selesai hanya jika semua orang sudah pernah meminjam dan buku kembali ke peminjam asal
        if top == 0 and jumlah == N:
            break
        # Jika belum selesai tapi mentok, backtrack ke orang sebelumnya
        top -= 1
        index_pinjam = riwayat_pinjam[top]
        print(" ->", index_pinjam, end="")

akhir = time.perf_counter()
eks = akhir - awal
print(f'\n\nWaktu eksekusi: {eks} detik.')