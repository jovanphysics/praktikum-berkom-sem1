import time
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
    print('================================')

# proses
start_time = time.perf_counter()
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
avail_move = [0,0,0,0]
forbidden_move = [0,0,0,0]
clockwise = True
change_clockwise = 0
# jalankan iterasi 
while pointer != endpoints[1]:
    change_clockwise += 1
    print(f'Titik x: {pointer[0]}, y: {pointer[1]} berhasil dilewati')
    # cek arah yang tersedia
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
        direction = [1,1,0,1]
    elif (pointer[0] == 0) and (0 < pointer[1] < (N-1)):
        direction = [1,1,1,0]
    elif (pointer[0] == (N-1)) and (0 < pointer[1] < (N-1)):
        direction = [1,0,1,1]
    else:
        direction = [1,1,1,1]

    # cek apakah bisa dilewati
    i = 0
    while(i < 4):
        if direction[i] == 1:
            if (i == 0) and (forbidden_move[i] == 0):
                bukan_dinding = int(matrix[pointer[1]-1][pointer[0]] == 1)
                avail_move[i] = bukan_dinding
            elif (i == 1) and (forbidden_move[i] == 0):
                bukan_dinding = int(matrix[pointer[1]][pointer[0]+1] == 1)
                avail_move[i] = bukan_dinding
            elif (i == 2) and (forbidden_move[i] == 0):
                bukan_dinding = int(matrix[pointer[1]+1][pointer[0]] == 1)
                avail_move[i] = bukan_dinding
            elif (i == 3) and (forbidden_move[i] == 0):
                bukan_dinding = int(matrix[pointer[1]][pointer[0]-1] == 1)
                avail_move[i] = bukan_dinding
        else:
            avail_move[i] = 0
        i += 1
    # Jika jalan buntu
    if avail_move == [0,0,0,0]:
        i = 0
        while(i < 4):
            if direction[i] == 1:
                if i == 0:
                    bukan_dinding = int(matrix[pointer[1]-1][pointer[0]] == 1)
                    avail_move[i] = bukan_dinding
                elif i == 1:
                    bukan_dinding = int(matrix[pointer[1]][pointer[0]+1] == 1)
                    avail_move[i] = bukan_dinding
                elif i == 2:
                    bukan_dinding = int(matrix[pointer[1]+1][pointer[0]] == 1)
                    avail_move[i] = bukan_dinding
                else:
                    bukan_dinding = int(matrix[pointer[1]][pointer[0]-1] == 1)
                    avail_move[i] = bukan_dinding
            else:
                avail_move[i] = 0
            i += 1  

    # Pilih jalur
    if clockwise:
        j = 0
        while (j < 4):
            if avail_move[j] == 1:
                if j == 0:
                    pointer[1] -= 1
                    forbidden_move = [0,0,1,0]
                    break
                elif j == 1:
                    pointer[0] += 1
                    forbidden_move = [0,0,0,1]
                    break
                elif j == 2:
                    pointer[1] += 1
                    forbidden_move = [1,0,0,0]
                    break
                else:
                    pointer[0] -= 1
                    forbidden_move = [0,1,0,0]
                    break
            j += 1
    else:
        j = 3
        while (j >= 0):
            if avail_move[j] == 1:
                if j == 0:
                    pointer[1] -= 1
                    forbidden_move = [0,0,1,0]
                    break
                elif j == 1:
                    pointer[0] += 1
                    forbidden_move = [0,0,0,1]
                    break
                elif j == 2:
                    pointer[1] += 1
                    forbidden_move = [1,0,0,0]
                    break
                else:
                    pointer[0] -= 1
                    forbidden_move = [0,1,0,0]
                    break
            j -= 1

    if (change_clockwise % 3) == 0:
        clockwise = not clockwise
        
print(f'Titik x: {pointer[0]}, y: {pointer[1]} berhasil dilewati')
end_time = time.perf_counter()
execution_time = end_time - start_time
print('Labirin Diselesaikan!')
print(f"Waktu eksekusi: {execution_time:.6f} detik")              
