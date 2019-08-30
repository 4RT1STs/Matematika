#RECODE BOLEH TAPI JANGAN NGACO!!
#Gunakan Tools ini untuk orang Bego!!
#Belajar itu Mudah!!
m = '\033[91m'
h = '\033[92m'
k = '\033[93m'
p = '\033[0m'

#import
import time, os
from getpass import getpass as oh
from math import *

sel = "   >>> "

def enter():
	oh('\n   [Tekan Enter Untuk Kembali]')
	home()

banner = m + """┌┬┐┌─┐┌┬┐┬ ┬┌─┐┌─┐┬ ┬┌┐┌┌┬┐┌─┐┬─┐
│││├─┤ │ ├─┤│  │ ││ ││││ │ ├┤ ├┬┘
┴ ┴┴ ┴ ┴ ┴ ┴└─┘└─┘└─┘┘└┘ ┴ └─┘┴└─""" + p + "\n		Version : Remake 0.1\n		Author By : Maulana S.A\n\n"

def pangkat():
	os.system('clear')
	print(banner)
	print("   1). Pangkatkan")
	print("   2). Unpangkat")
	print("   0). Kembali")
	pilih = int(input('   >>> '))
	if pilih == 1:
		pangkatkeun()
	elif pilih == 2:
		unpangkat()
	elif pilih == 0:
		home()
	else:
		 pangkat()
	
def pangkatkeun():
	a1 = float(input('   [?] Angka berapa yg ingin dipangkatkan: '))
	a2 = float(input('   [?] Dipangkatkan ke berapa: '))
	hasil = a1 ** a2
	print("   [+] Hasil dari " + str(a1) + " pangkat " + str(a2) + " adalah: " + h + str(hasil) + p)
	enter()

def unpangkat():	
	angka = 0
	a1 = float(input('   [?] Angka hasil perpangkatan: '))
	a2 = float(input('   [?] Pangkat berapa: '))
	while angka < a1:
		angka += 1
		ss = angka ** a2
		if ss == a1:
			print("   [+] Hasilnya: " + h + str(angka) + p)
			break
	else:
		print("   [!] Tidak Ada Hasil Ditemukan")
	enter()

def kpk():
	penentu = 0
	a1 = int(input('   [?] Angka pertama: '))
	a2 = int(input('   [?] Angka kedua: '))
	a3 = []
	a4 = []
	a5 = 0
	a6 = 0
	if a1 > a2:
		jangkau = a1
	else:
		jangkau = a2
	for s1 in range(jangkau):
		a5 += a1
		a3.append(a5)
	for s2 in range(jangkau):
		a6 += a2
		a4.append(a6)
	for s3 in a3:
		if penentu != 0:
			break
		for s4 in a4:
			if s4 == s3:
				print("   [+] KPK-nya adalah: " + h + str(s3) + p)
				penentu += 1
	enter()

def fpb():
	a1 = int(input('   [?] Angka pertama: '))
	a2 = int(input('   [?] Angka kedua: '))
	hasil = gcd(a1,a2)
	print("   [+] FPB-nya adalah: " + h + str(hasil) + p)
	enter()
	
def lipat():
	os.system('clear')
	print(banner)
	print("   1). Mencari KPK")
	print("   0). Kembali")
	pilih = int(input(sel))
	if pilih == 1:
		kpk()
	elif pilih == 0:
		home()
	else:
		lipat()	
			
def persen():
	os.system('clear')
	print(banner)
	print("   1). Persen ke Bilangan")
	print("   2). Bilangan ke Persen")
	print("   0). Kembali")
	pilih = int(input(sel))
	if pilih == 0:
		home()
	elif pilih == 1:
		per2bil()
	elif pilih == 2:
		bil2per()
	else:
		persen()

def per2bil():
	a1 = float(input("   [?] Berapa totalnya: "))
	a2 = float(input("   [?] Berapa persen yg ingin ditampilkan (ex: 20)\n   : "))
	hasil = a1 * a2 / 100
	print("   [+] Hasilnya: " + h + str(hasil) + p)
	enter()
	
def bil2per():
	a1 = float(input("   [?] Berapa totalnya: "))
	a2 = float(input("   [?] Berapa jumlah yg ingin diperserkan: "))
	hasil = a2 * 100 / a1
	print("   [+] Hasilnya: " + h + str(hasil) + "%" + p)
	enter()
	
def faktor():
	os.system('clear')
	print(banner)
	print("   1). Mencari FPB")
	print("   2). Faktorial")
	print("   3). Faktorisasi Prima")
	print("   0). Kembali")
	pilih = int(input(sel))
	if pilih == 0:
		home()
	elif pilih == 1:
		fpb()
	elif pilih == 2:
		fak()
	elif pilih == 3:
		fprima()
	else:
		faktor()
	
def fak():
	hasil = int(input("   [?] Berapa angkanya: "))
	if hasil > 15:
		oh('   [Kamu Yakin? Enter Untuk Melanjutkan]')
	tai = 1
	for s in range(1, hasil + 1):
		tai *= s
	print("   [+] Faktorial dari " +str(hasil) + " adalah: " + h + str(tai) + p)
	enter()

def fprima():
	a1 = int(input("   [?] Berapa angkanya: "))
	a2 = a1
	factorlist = []
	n_list = []
	n_list.append(a1)
	loop = 2
	while loop <= a1:
		if a1 % loop == 0:
			a1 /= loop
			factorlist.append(loop)
			n_list.append(int(a1))
		else:
			loop += 1
	print("   [+] Faktorisasi prima dari " + str(a2) + " adalah: ")
	print("   " + h + str(factorlist) + p + "\n")
	print("   [+] Riwayat Angka: ")
	print("   " + h + str(n_list) + p)
	enter()

def home():
	os.system('clear')
	print(banner)
	print("   1). Perpangkatan")
	print("   2). Kelipatan")
	print("   3). Faktor")
	print("   4). Persentase")
	print("   5). Lainnya")
	print("   0). Keluar")
	pilih = int(input(sel))
	if pilih == 1:
		pangkat()
	elif pilih == 2:
		lipat()
	elif pilih == 3:
		faktor()
	elif pilih == 4:
		persen()
	elif pilih == 5:
		lainnya()
	elif pilih == 0:
		print("   [!] Keluar")
	else:
		home()

exec(open('other.py').read())


try:
	home()
except:
	print("   [!] Terjadi Error")
	time.sleep(1)
	print("   [!] Memulai Ulang Program")
	time.sleep(0.5)
	os.system('python mathC.py')
