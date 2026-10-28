import time
"""Pinjam Buku (Tanpa Subprogram)"""
# program utama
# input
N = int(input("Masukkan jumlah orang: "))
matrix = []
umur = [0 for _ in range(N)]
umur_tersedia = []
for i in range(N):
    col = [0]*N
    matrix += [col]

for y in range(N):
    for x in range(N):
        val = int(input(f'Masukkan isi matrix graph umur untuk koordinat ({x},{y}): '))
        matrix[y][x] = val
    print('================================')

for i in range(N):
    val_umur = int(input(f'Masukkan umur untuk index {i}: '))
    umur[i] = val_umur

pointer = int(input('Masukkan index tempat awal buku berada: '))
for i in range(N):
    if matrix[pointer][i] == 1:
        umur_tersedia += [umur[i]]

for i in range(len(umur_tersedia)):
    for j in range(i, len(umur_tersedia)):
        buffer = umur_tersedia[i]
        umur_tersedia[i] = umur_tersedia[j]
        umur_tersedia[j] = buffer
