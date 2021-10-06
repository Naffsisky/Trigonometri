#Author : PRINAFSIKA (21081010278)
from math import pi, radians, degrees, sin, cos, tan, asin, acos, atan
import pyfiglet
import os

os.system('color 6')
intro = pyfiglet.figlet_format("Trigonometri", font = "standard")
intronama = pyfiglet.figlet_format("By : Kelompok 5", font = "standard")

print(intro)
print(intronama)

print('--- Konsep Kuadran ---')
print('')
print('Pada kuadran I (0 – 90), semua nilai sin, tan dan cos bernilai positif')
print('Pada kuadran II (90 – 180), hanya sin bernilai positif')
print('Pada kuadran II (180 – 270), hanya tan bernilai positif')
print('Pada kuadran II (270 – 360), hanya cos bernilai positif')
print('')
print('1. Sin')
print('2. Cos')
print('3. Tan')

pilihan = int(input('Masukkan Pilihan : '))

if pilihan == 2:
    os.system('cls')
    os.system('color a')
    print('Ini adalah penghitungan nilai Cos')
    print('Masukan nilai Cos dan angka terdekat (0,90,180,360), Misal ')
    print('Nilai Cos 210. Maka masukan Nilai Cos 180 dan Angka terdekat 30. 180 + 30 menjadi 210')
    pilihanCos = int(input('Masukkan Nilai Cos : '))
    tambahanCos = int(input('Masukan Angka terdekat :'))
    if tambahanCos >= 360:
        hitungCos = (pilihanCos + tambahanCos)
        print(hitungCos)

    elif tambahanCos >= 180:
        hitungCos = (pilihanCos + tambahanCos)
        print(hitungCos)

    elif tambahanCos >= 90:
        hitungCos = (pilihanCos + tambahanCos)
        print(hitungCos)

    elif tambahanCos >= 0:
        hitungCos = (pilihanCos + tambahanCos)
        print(hitungCos)

    else: print('gagal')
        
else: exit()
