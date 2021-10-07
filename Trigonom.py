#Author : PRINAFSIKA (21081010278)
import math 
from prettytable import PrettyTable
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
print('3. Menghitung Sudut Custom')
menu = int(input('Masukkan Pilihan : '))
 
if menu == 1:
    os.system('cls')
    print('--- Penghitungan Segitiga ---')
    print('')
    print('Sin = Depan / Miring')
    print('Cos = Samping / Miring')
    print('Tan = Depan / Samping')
    print('')
    print('1. Sin')
    print('2. Cos')
    print('3. Tan')

    pilihansatu = int(input('Masukkan Pilihan : '))

    if pilihansatu == 1:
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

    elif pilihansatu == 2:
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

    elif pilihansatu == 3:
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
    os.system('cls')
    print('--- Penghitungan Sudut Istimewa ---')
    tabelinfo = PrettyTable(["Sudut", "0°", "30°", "45°", "60°", "90°"])
    tabelinfo.add_row(["Sin", "0", "1/2", "1/2 √2", "1/2 √3", "1"])
    tabelinfo.add_row(["Cos", "1", "1/2 √3", "1/2 √2", "1/2", "0"])
    tabelinfo.add_row(["Tan", "0", "1/√3", "1", "√3", "∞"])

    print(tabelinfo)
    pilihandua = int(input('Press 0 to exit : '))  

elif menu == 3:
    sudut = int(input('Masukkan Sudut yang ingin dicari : '))
    os.system('cls')
    tabelinfos = PrettyTable(["Kuadran", "Derajat", "Keterangan"])
    tabelinfos.add_row(["1", "0° < x < 90°", "Semua (Positif)"])
    tabelinfos.add_row(["2", "90° < x < 180°", "Hanya Sin (Positif)"])
    tabelinfos.add_row(["3", "180° < x < 270°", "Hanya Tan (Positif)"])
    tabelinfos.add_row(["4", "270° < x < 360°", "Hanya Cos (Positif)"])
    print(tabelinfos)
    print("Sudut yang ingin anda cari adalah", sudut)
    kuadran = int(input('Sudut tersebut berada pada Kuadran : '))

    if kuadran == 1:
        print('Dalam Kuadran 1 sudut 180° akan dikurang dengan sudut anda')
        tambahkurang = (180-sudut)
        print('180 -', sudut, '=', tambahkurang)

    elif kuadran == 2:
        print('Dalam Kuadran 2 sudut 180° akan ditambah dengan sudut anda')
        tambahkurang = (180+sudut)
        print('180 +', sudut, '=', tambahkurang)

    elif kuadran == 3:
        print('')
        print('Dalam Kuadran 3 sudut 180° akan ditambah dengan total menjadi sudut anda.')
        print('Misal Sudut anda 210°. maka 180 ditambah 30 agar menjadi 210')
        print('')
        print('Sudut anda adalah :', sudut)
        tambah = int(input('Masukan tambahan : '))
        os.system('cls')
        tabelspesial = PrettyTable(["Sudut", "0°", "30°", "45°", "60°", "90°"])
        tabelspesial.add_row(["Sin", "-0", "-1/2", "-1/2 √2", "-1/2 √3", "-1"])
        tabelspesial.add_row(["Cos", "-1", "-1/2 √3", "-1/2 √2", "-1/2", "-0"])
        tabelspesial.add_row(["Tan", "0", "1/√3", "1", "√3", "∞"])
        print(tabelspesial)
        print('Maka sudut yang anda cari adalah', tambah,'°')

    elif kuadran == 4:
        print('')
        print('Dalam Kuadran 4 sudut 270° akan ditambah dengan total menjadi sudut anda.')
        print('Misal Sudut anda 300°. maka 270 ditambah 30 agar menjadi 300')
        print('')
        print('Sudut anda adalah :', sudut)
        tambah = int(input('Masukan tambahan : '))
        os.system('cls')
        print('KETENTUAN : APABILA SUDUT ANDA SIN GANTI DENGAN COS, COS GANTI DENGAN SIN')
        tabelspesial = PrettyTable(["Sudut", "0°", "30°", "45°", "60°", "90°"])
        tabelspesial.add_row(["Sin", "-0", "-1/2", "-1/2 √2", "-1/2 √3", "-1"])
        tabelspesial.add_row(["Cos", "1", "1/2 √3", "1/2 √2", "1/2", "0"])
        tabelspesial.add_row(["Tan", "-0", "-1/√3", "-1", "-√3", "-∞"])

        tabelket = PrettyTable(["Sudut", "Keterangan"])
        tabelket.add_row(["Sin", "Semua Negatif"])
        tabelket.add_row(["Cos", "Positif"])
        tabelket.add_row(["Tan", "Semua Negatif"])
        print(tabelket)
        print(tabelspesial)

        print('Maka sudut yang anda cari adalah', tambah,'°')
