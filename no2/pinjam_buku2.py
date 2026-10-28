import time
"""Pinjam Buku (Tanpa Subprogram)"""
# program utama
# input
N = int(input("Masukkan ukuran labirin: "))
matrix = []
for i in range(N):
    col = [0]*N
    matrix += [col]

for y in range(N):
    for x in range(N):
        val = int(input(f'Masukkan isi matrix graph untuk koordinat ({x},{y}): '))
        matrix[y][x] = val
    print('================================')