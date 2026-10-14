"""labirin (tanpa Subprogram)"""
# input
N = int(input("Masukkan ukuran labirin: "))
matrix = []
for i in range(N):
    col = [0]*N
    matrix += [col]

for y in range(N):
    for x in range(N):
        val = int(input(f'Apakah koordinat ({x},{y}) bisa dilewati (1) atau tidak (0): '))
        matrix[y][x] = val

# proses
# inisialisasi pointer dan arahnya
status_sisi = [[-1,-1], [-1,-1], [-1,-1], [-1,-1]]
# cari titik awal di sisi atas
for i in range(N):
    if matrix[0][i] == 1:
        status_sisi[0] = [i,0]
        break
# cari titik awal di sisi bawah
for i in range(N):
    if matrix[N-1][i] == 1:
        status_sisi[1] = [i,N-1]
        break
# cari titik awal di sisi kiri
for i in range(N):
    if matrix[i][0] == 1:
        status_sisi[2] = [0,i]
        break
# cari titik awal di sisi kanan
for i in range(N):
    if matrix[i][N-1] == 1:
        status_sisi[3] = [N-1, i]
        break

# tentukan endpoint
endpoints = []
for i in range(4):
    if status_sisi[i] != [-1,-1]:
        endpoints += [status_sisi[i]]

# tentukan titik mulai
pointer = endpoints[0]
direction = [0,0,0,0]
# cek apakah titik mulai terletak di titik sudut persegi labirin
if (pointer[0] == 0) and (pointer[1] == 0):
    direction = [0,1,1,0]
elif (pointer[0] == 0) and (pointer[1] == N-1):
    direction = [1,1,0,0]
elif (pointer[0] == (N-1)) and (pointer[1] == 0):
    direction = [0,0,1,1]
elif (pointer[0] == (N-1)) and (pointer[1] == (N-1)):
    direction = [1,0,0,1]
elif (0 < pointer[0] < (N-1)) and (pointer[1] == 0):
    direction = [0,1,1,1]
elif (0 < pointer[0] < (N-1)) and (pointer[1] == (N-1)):
    direction = [1,1,1,0]