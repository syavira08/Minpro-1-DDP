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
<img width="1348" height="1079" alt="Screenshot 2025-09-14 133223" src="https://github.com/user-attachments/assets/18d49150-9bc3-4b57-91c5-b1ff876a9e6c" />
Berdasarkan gambar tersebut dapat dilihat bahwa program akan menampilkan jadwal dokter spesialis gigi jika user memilih nomor 1. 

### 2. Kondisi kedua: Jika user memilih nomor 2 pada menu utama 
<img width="1403" height="1076" alt="Screenshot 2025-09-14 133357" src="https://github.com/user-attachments/assets/46451ce8-e4a7-46bb-b7ec-2be76832c289" />
Berdasarkan gambar tersebut dapat dilihat bahwa program akan menampilkan jadwal dokter spesialis anak jika user memilih nomor 2.

### 3. Kondisi ketiga: Jika user memilih nomor 3 pada menu utama 
<img width="1402" height="1079" alt="Screenshot 2025-09-14 133512" src="https://github.com/user-attachments/assets/c818a749-ad1d-4da2-af36-851ae3e8d49c" />
Berdasarkan gambar tersebut dapat dilihat bahwa program akan menampilkan jadwal dokter spesialis mata jika user memilih nomor 3.

### 4. Kondisi keempat : Jika user memilih nomor 4 pada menu utama
<img width="1407" height="1079" alt="Screenshot 2025-09-14 135242" src="https://github.com/user-attachments/assets/bec2653e-d262-4282-905f-52f6cc24e0f4" />
Berdasarkan gambar tersebut, jika user memilih menu nomor 4 yaitu tambah jadwal dokter maka akan terbagi menjadi beberapa kondisi lagi yaitu sebagai berikut:

#### 4.1 Kondisi pertama : Jika user memilih nomor 1 pada menu spesialis
<img width="1405" height="1079" alt="Screenshot 2025-09-14 140240" src="https://github.com/user-attachments/assets/d85b9137-e1c9-4cee-b987-c9d76057a63a" />
Berdasarkan gambar tersebut, dapat dilihat bahwa jika user memilih nomor 1 pada menu spesialis yaitu dokter gigi maka program akan menambahkan jadwal baru yang data nya sudah dilengkapi oleh user ke dalam list jadwal dokter gigi sesuai dengan hari yang sudah ditentukan.

#### 4.2 Kondisi kedua : Jika user memilih nomor 2 pada menu spesialis
<img width="1405" height="1079" alt="Screenshot 2025-09-14 142155" src="https://github.com/user-attachments/assets/37edefff-d076-46e4-8f45-0cec9d410d38" />
Berdasarkan gambar tersebut, dapat dilihat bahwa jika user memilih nomor 2 pada menu spesialis yaitu dokter anak maka program akan menambahkan jadwal baru yang data nya sudah dilengkapi oleh user ke dalam list jadwal dokter anak sesuai dengan hari yang sudah ditentukan.

#### 4.3 Kondisi ketiga : Jika user memilih nomor 3 pada menu spesialis
<img width="1403" height="1079" alt="Screenshot 2025-09-14 143444" src="https://github.com/user-attachments/assets/6254f086-6215-440c-957a-0745bbb34106" />
Berdasarkan gambar tersebut, dapat dilihat bahwa jika user memilih nomor 3 pada menu spesialis yaitu dokter mata maka program akan menambahkan jadwal baru yang data nya sudah dilengkapi oleh user ke dalam list jadwal dokter mata sesuai dengan hari yang sudah ditentukan.

#### 4.4 Kondisi keempat : Jika user memilih opsi yang tidak terdapat pada menu spesialis 
<img width="1008" height="1022" alt="Screenshot 2025-09-14 144118" src="https://github.com/user-attachments/assets/eb54c8ff-39e3-40b9-b3bb-677f5ea1e7ff" />
Berdasarkan gambar tersebut, dapat dilihat bahwa jika user memilih opsi yang tidak terdapat dalam menu spesialis maka program akan menampilkan pesan bahwa menu tidak valid. Kondisi ini menjadi kondisi terakhir dari kondisi keempat pada menu utama 

### 5. Kondisi kelima : Jika user memilih opsi yang tidak terdapat pada menu utama
<img width="1006" height="1020" alt="Screenshot 2025-09-14 145004" src="https://github.com/user-attachments/assets/6f4803f4-091e-4d15-a959-25dbc018e1dd" />
Berdasarkan gambar tersebut, dapat dilihat bahwa jika user memilih opsi yang tidak terdapat dalam menu utama maka program akan menampilkan pesan bahwa menu tidak valid. Kondisi ini menjadi kondisi terakhir dari menu utama.










