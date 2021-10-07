#Author : PRINAFSIKA (21081010278)
import math 
import fractions
import pyfiglet
import os

os.system('color 6')
intro = pyfiglet.figlet_format("Trigonometri", font = "standard")
intronama = pyfiglet.figlet_format("By : Kelompok 5", font = "standard")

print(intro)
print(intronama)

print('1. Penghitungan Segitiga')
print('2. Penghitungan Sudut Istimewa')
menu = int(input('Masukkan Pilihan : '))

if menu == 1:
    print('--- Penghitungan Segitiga ---')
    print('')
    print('Sin = Depan / Miring')
    print('Cos = Samping / Miring')
    print('Tan = Depan / Samping')
    print('')
    print('1. Sin')
    print('2. Cos')
    print('3. Tan')

    pilihan = int(input('Masukkan Pilihan : '))

    if pilihan == 1:
        os.system('cls')
        os.system('color a')
        print('Sin = Depan / Miring')
        print('')

        pilihanSindepan = int(input('Masukkan Sisi Depan : '))
        pilihanSinmiring = int(input('Masukkan Sisi Miring : '))
        hasilSin = pilihanSindepan/pilihanSinmiring
        f = fractions.Fraction(hasilSin)
        print('Hasil :', hasilSin)
        print('Hasil Dalam Pecahan :', f)

    elif pilihan == 2:
        os.system('cls')
        os.system('color a')
        print('Cos = Samping / Miring')
        print('')

        pilihanCossamping = int(input('Masukkan Sisi Samping : '))
        pilihanCosmiring = int(input('Masukkan Sisi Miring : '))
        hasilSin = pilihanCossamping/pilihanCosmiring
        f = fractions.Fraction(hasilSin)
        print('Hasil :', hasilSin)
        print('Hasil Dalam Pecahan :', f)

    elif pilihan == 3:
        os.system('cls')
        os.system('color a')
        print('Sin = Depan / Samping')
        print('')

        pilihanTandepan = int(input('Masukkan Sisi Depan : '))
        pilihanTanSamping = int(input('Masukkan Sisi Samping : '))
        hasilSin = pilihanTandepan/pilihanTanSamping
        f = fractions.Fraction(hasilSin)
        print('Hasil :', hasilSin)
        print('Hasil Dalam Pecahan :', f)

elif menu == 2:
    print('a')
