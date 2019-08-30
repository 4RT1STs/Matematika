def lainnya():
	os.system('clear')
	print(banner)
	print("   1). Derajat ke Radian")
	print("   2). Radian ke Derajat")
	print("   3). Cek Bilangan Prima")
	print("   4). Menghitung Rata2")
	print("   0). Kembali")
	pilih = int(input('   >>> '))
	if pilih == 1:
		der2ra()
	elif pilih == 2:
		ra2der()
	elif pilih == 3:
		cek_prima()
	elif pilih == 4:
		rata2()
	elif pilih == 0:
		home()
	else:
		 lainnya()
	
def der2ra():
	a1 = float(input("   [?] Berapa derajatnya: "))
	hasil = radians(a1)
	print("   [+] Radian dari " + str(a1) + "° adalah: ")
	print("   " + h + str(hasil) + p)
	enter()

def ra2der():
	a1 = float(input("   [?] Berapa radiannya: "))
	hasil = degrees(a1)
	print("   [+] Derajat dari radian " + str(a1) + " adalah: ")
	print("   " + h + str(hasil) + "°" + p)
	enter()

def cek_prima():
	a1 = int(input("   [?] Berapa angkanya: "))
	for s in range(2,a1):
		if a1 % s == 0:
			print("   [+] Hasilnya: " + m + "False" + p)
			print("   [+] " + str(a1) + " bukan bilangan prima")
			break
	else:
		print("   [+] Hasilnya: " + h + "True" + p)
		print("   [+] " + str(a1) + " adalah bilangan prima")
	enter()

def rata2():
	angka = 0
	a1 = str(input("   [?] Masukan angkanya, pisahkan dgn koma (ex: 30,20,10)\n   : ")).split(",")
	jumlah = len(a1)
	for s in a1:
		angka += int(s)
	hasil = float(angka) / jumlah
	print("   [+] Jumlah: " + h + str(jumlah) + p)
	print("   [+] Rata2nya adalah: " + h + str(hasil) + p)
	enter()