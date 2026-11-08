import time
import matplotlib.pyplot as plt
import numpy as np
""" Newton Raphson (Simulasi) """
plt.style.use('dark_background')
# definisi fungsi
def function(x, coefs):
    value = 0.0
    for i in range(len(coefs)):
        value += coefs[i] * (x**i)
    return value

def gradient(x, coefs):
    value = 0.0
    for i in range(1, len(coefs)):
        value += i * coefs[i] * (x**(i - 1))
    return value

def absol(x):
    value = (x >= 0) * x + (x < 0) * (-x)
    return value

def gradient_line_gen(x, x1, coefs):
    return gradient(x1, coefs)*x - gradient(x1, coefs)*x1 + function(x1, coefs)

def cari_batas_kiri(grad_lines):
    minimums = []
    for i in range(len(grad_lines)):
        minimums.append(min(grad_lines[i][0]))
    return min(minimums)

def cari_batas_kanan(grad_lines):
    maximums = []
    for i in range(len(grad_lines)):
        maximums.append(max(grad_lines[i][0]))
    return max(maximums)

# program utama
# input
N = int(input('Masukkan derajat polinomial: '))
N += 1
coefs = [0]*N
for i in range(N):
    if(i == 0):
        val = float(input('Masukkan nilai konstanta: '))
    else:
        val = float(input(f'Masukkan nilai koefisien x^{i}: '))

    coefs[i] = val

x_init = float(input('Masukkan tebakan awal x: '))
x = x_init
gradient_lines = []
absis_singgung = []
ordinat_singgung = []
epsilon = 1e-4
k = 0
max_iter = 1e6
save_image = input('Simpan hasil simulasi (y/n)? > ')
# proses iterasi
start_time = time.perf_counter()
err = False
while True:
    k += 1
    val = function(x, coefs)
    grad = gradient(x, coefs)
    if grad == 0:
        print('Newton-Raphson gagal: turunan = 0')
        err = True
        break

    x_new = x - (val / grad)
    X = np.linspace(x_new-1, x+1, 100)
    gradient_lines.append([X, gradient_line_gen(X, x, coefs)])
    absis_singgung.append(x)
    ordinat_singgung.append(val)
    print(f'Iterasi ke-{k} --> Nilai x: {x_new:.6f}    Gradien: {grad:.6f}')
    if (absol(x_new - x) < epsilon) and (absol(val) < epsilon):
        print(f'Akar ditemukan: {x_new:.6f}')
        print(f'Jumlah iterasi: {k}')
        break
    elif k >= max_iter:
        print(f'\nGAGAL: Akar tidak ditemukan setelah {k} iterasi.')
        err = True
        break

    x = x_new

end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Waktu eksekusi: {execution_time:.6f} detik")
if err:
    quit()
# gambar kurva
print('Menggambar kurva...')
batas_kiri = cari_batas_kiri(gradient_lines)
batas_kanan = cari_batas_kanan(gradient_lines)
X = np.linspace(batas_kiri, batas_kanan, 1000)
y_pol = function(X, coefs)
plt.figure(figsize=(10,9))
plt.plot(X, y_pol, color='#FE2C55', linewidth=2)
plt.axhline(0, color='white', linewidth=2)
plt.scatter(absis_singgung, ordinat_singgung, s=20, c="#25F4EE")
for lines in gradient_lines:
    plt.plot(lines[0], lines[1], color='#7DF9FF', linestyle='--', linewidth=1)
for i in range(len(absis_singgung)):
    plt.vlines(x=absis_singgung[i], ymin=0, ymax=ordinat_singgung[i], color='#8B008B', linewidth=2, linestyles='--')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Simulasi Algoritma Newton-Raphson')
plt.grid(True)
plt.rcParams['axes.linewidth'] = 10
if save_image.strip().lower() == 'y':
    plt.savefig('no1/ss_newton_raphson.png', dpi=300, edgecolor='none')
plt.show()