# 📱 Sistem Kasir Otomatis Gadget-Verse

Program berbasis Python sederhana untuk menentukan persentase diskon belanja pelanggan secara otomatis di Gadget-Verse berdasarkan status keanggotaan, total nilai belanja, dan kepemilikan kupon.

## 🚀 Fitur Utama
* **Cek Keanggotaan & Kupon**: Mengombinasikan logika status member dan kevalidan kupon untuk keuntungan maksimal.
* **Diskon Bertingkat**: Menghitung secara otomatis apakah pelanggan berhak mendapatkan diskon besar, diskon standar, atau tidak mendapatkan diskon sama sekali.

## 📋 Ketentuan Diskon Toko
1. **Diskon Super 30%**:
   * Pelanggan sudah menjadi member.
   * Total belanja $\ge$ Rp 1.500.000.
   * Memiliki kupon yang valid.
2. **Diskon 10%**:
   * Pelanggan sudah menjadi member.
   * Total belanja $\ge$ Rp 500.000.
3. **Tidak Mendapatkan Diskon**:
   * Jika tidak memenuhi salah satu kondisi di atas.

## 💻 Cara Menjalankan
Jalankan file Python ini di lingkungan kamu (seperti Pydroid 3), sesuaikan nilai variabel di baris atas untuk simulasi, dan program akan langsung menampilkan hasil kalkulasi diskon di layar terminal.
