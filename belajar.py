print("SISTEM KASIR OTOMATIS GADGET-VERSE")
sudah_menjadi_member=True
total_belanja_pembeli=1500000
memiliki_kupon_valid=True
if sudah_menjadi_member and total_belanja_pembeli >=1500000 and memiliki_kupon_valid:
	print("Selamat! Anda mendapatkan diskon super 30%")
elif sudah_menjadi_member and total_belanja_pembeli >=500000: 
	print("Selamat! Anda mendapatkan diskon 10%")
else:
	print("Maaf Anda tidak mendapatkan diskon")