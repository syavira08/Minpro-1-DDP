# Minpro-1-DDP
Syavira Firnanda Prawiro 2509116072

# Sistem Jadwal Layanan Dokter 
Program sederhana berbasis python ini dirancang untuk melihat dan menampilkan jadwal dokter berdasarkan spesialisnya, program ini juga dapat menambah jadwal dokter berdasarkan spesialisnya pada sebuah rumah sakit.

## Fitur
- Melihat jadwal dokter spesialis : 
  - Gigi
  - Anak
  - Mata
- Menambahkan jadwal baru sesuai spesialis dan hari
- Menampilkan error jika input salah

## Flowchart Sistem Jadwal Layanan Dokter
![Flowchart Minpro 1](https://github.com/user-attachments/assets/b1ec7057-7cb1-4020-bfe2-d629f963f913)
Pada flowchart tersebut alur dimulai dari menampilkan identitas kemudian dilanjutkan dengan menampilkan menu utama, lalu user dapat memilih menu yang diinginkan yang dimana menu terdiri dari 4 pilihan yaitu:
- Lihat jadwal dokter gigi
- Lihat jadwal dokter anak
- Lihat jadwal dokter mata
- Tambah jadwal dokter
  
Berikut adalah alur masing - masing menu:
- Jika pilih lihat jadwal dokter gigi -> maka program akan menampilkan jadwal dokter gigi dan selesai, jika tidak maka lanjut ke menu berikutnya,
- Jika pilih lihat jadwal dokter anak -> maka program akan menampilkan jadwal dokter anak dan selesai, jika tidak maka lanjut ke menu berikutnya,
- Jika pilih lihat jadwal dokter mata -> maka program akan menampilkan jadwal dokter mata dan selesai, jika tidak maka lanjut ke menu berikutnya,
- Jika pilih tambah jadwal dokter -> maka program akan lanjut ke proses berikutnya
- Jika pilihannya salah/tidak ada -> maka program akan menampilkan pesan menu tidak valid dan selesai.

Proses lanjutan pilihan menu Tambah Jadwal Dokter: 
- Program akan menampilkan menu spesialis yang ingin ditambahkan jadwalnya
- Lalu user dapat memilih jenis spesialis yang ingin ditambahkan jadwalnya
- Jika menu valid -> maka dilanjutkan dengan user menentukan hari
- Lalu dilanjutkan lagi dengan user menginput nama dokter
- Lalu user juga menginput jam praktek
- Setelah itu program akan menyimpan jadwal baru ke dalam list spesialis sesuai pilihan user
- Selanjutnya akan keluar output konfirmasi bahwa jadwal berhasil ditambahkan dan program selesai.
- Sebaliknya jika menu tidak valid -> maka program akan menampilkan pesan menu tidak valid dan selesai.

## Penggunaan List & Tuple serta Conditional Statement Pada Program Sistem Jadwal Layanan Dokter 

### 1. List
Dalam program ini, list digunakan untuk menyimpan jadwal dokter tiap spesialis
```python
Dokter_gigi = [
    ["Senin : (Dokte Joko, 08.00 - 11.00) ", "(Dokter Tomo, 13.00 - 15.30) "], 
    ["Selasa : (Dokter Kiki, 08.00 - 10.00) "],
    ["Rabu : (Dokter Tomo, 07.30 - 10.00) "],
    ["Kamis : (Dokter Karin, 08.00 - 11.00) "],
    ["Jumat : (Dokter Kiki, 07.30 - 11.00) "]
]

Dokter_anak = [
    ["Senin : (Dokter Ririn, 07.00 - 11.00)", "(Dokter Nanda, 13.00 - 15.30) "],
    ["Selasa : (Dokter Lili, 08.00 - 10.00) "],
    ["Rabu : (Dokter Lili, 07.30 - 10.00) "],
    ["Kamis : (Dokter Nanda, 07.30 - 11.00) "],
    ["Jumat : (Dokter Ririn, 07.30 - 11.00) "]
]

Dokter_mata = [
    ["Senin : (Dokter Hani, 09.00 - 11.00) | ", "(Dokter Alan, 13.00 - 15.00) "],
    ["Selasa : (Dokter Dino, 13.00 - 15.00 ) "],
    ["Rabu : (Dokter Dino, 08.30 - 10.00) "]
]
```
Di dalam setiap list dokter spesialis juga terdapat list lagi yang menyimpan jadwal layanan dokter per hari.

### 2. Tuple
Dalam program ini, tuple digunakan saat menambah jadwal baru.
```python
dokter_gigi_new = (nama, jam)
Dokter_gigi[0].insert(10, dokter_gigi_new)
```

### 3. Conditional Statement
Dalam program ini terdapat beberapa bagian yang menggunakan conditional statement/percabangan yaitu antara lain:
- Mengecek menu utama yang dipilih (pilih_menu)
- Mengecek spesialis yang dipilih (pilih_spesialis)
- Mengecek hari praktik yang dipilih (pilih_hari)
- Menangani input tidak valid

Berikut adalah salah satu contoh penggunaan conditional statement dalam program ini:
```python
pilih_hari = input("Tentukan Hari: ")
            if pilih_hari == "senin":
                nama = input("Nama Dokter: ")
                jam = input("Jam Praktik: ")
                dokter_mata_new = (nama, jam)
                Dokter_mata[0].insert(10, dokter_mata_new)
                print("Anda telah berhasil menambahkan jadwal dokter mata: ", Dokter_mata[0])
            elif pilih_hari == "selasa":
                nama = input("Nama Dokter: ")
                jam = input("Jam Praktik: ")
                dokter_mata_new = (nama, jam)
                Dokter_mata[1].insert(10, dokter_mata_new)
                print("Anda telah berhasil menambahkan jadwal dokter mata: ", Dokter_mata[1])
            elif pilih_hari == "rabu":
                nama = input("Nama Dokter: ")
                jam = input("Jam Praktik: ")
                dokter_mata_new = (nama, jam)
                Dokter_mata[2].insert(10, dokter_mata_new)
                print("Anda telah berhasil menambahkan jadwal dokter mata: ", Dokter_mata[2])
            else:
                print("Terdapat Kesalahan")
```
Tujuan penggunaan conditional statement pada contoh tersebut adalah untuk menambahkan jadwal sesuai hari yang diinginkan oleh user.

## Penjelasan Output dalam Semua Kondisi 
Dalam program sistem jadwal layanan dokter terdapat beberapa kondisi yang bergantung pada pilihan user yaitu antara lain:

### 1. Kondisi pertama: Jika user memilih nomor 1 pada menu utama
