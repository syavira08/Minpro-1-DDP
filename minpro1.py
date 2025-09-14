print("----------------------------------")
print("Nama : Syavira Firnanda Prawiro")
print("NIM : 2509116072")
print("Kelas : B")
print("----------------------------------")

print("Sistem Jadwal Layanan Dokter")
print("-----------------------------")
print("Selamat Datang di Sistem Layanan Jadwal Dokter Rumah Sakit Gembira")
print("Silahkan pilih menu di bawah ini :")
print("1. Lihat Jadwal Dokter Spesialis Gigi")
print("2. Lihat Jadwal Dokter Spesialis Anak")
print("3. Lihat Jadwal Dokter Spesialis Mata")
print("4. Tambah Jadwal Dokter")
pilih_menu = input("Pilih Menu (1/2/3/4): ")

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

if pilih_menu == "1":
    print(Dokter_gigi[0])
    print(Dokter_gigi[1])
    print(Dokter_gigi[2])
    print(Dokter_gigi[3])
    print(Dokter_gigi[4])

elif pilih_menu == "2":
    print(Dokter_anak[0])
    print(Dokter_anak[1])
    print(Dokter_anak[2])
    print(Dokter_anak[3])
    print(Dokter_anak[4])

elif pilih_menu == "3":
    print(Dokter_mata[0])
    print(Dokter_mata[1])
    print(Dokter_mata[2])

elif pilih_menu == "4":
        print("Silahkan pilih spesialis terlebih lebih dulu")
        print("1. Dokter Gigi")
        print("2. Dokter Anak")
        print("3. Dokter Mata")
        pilih_spesialis = input("Pilih spesialis (1/2/3): ")
        if pilih_spesialis == "1":
            pilih_hari = input("Tentukan Hari: ")
            if pilih_hari == "senin":
                nama = input("Nama Dokter: ")
                jam = input("Jam Praktik: ")
                dokter_gigi_new = (nama, jam)
                Dokter_gigi[0].insert(10, dokter_gigi_new)
                print("Anda telah berhasil menambahkan jadwal dokter gigi: ", Dokter_gigi[0])
            elif pilih_hari == "selasa":
                nama = input("Nama Dokter: ")
                jam = input("Jam Praktik: ")
                dokter_gigi_new = (nama, jam)
                Dokter_gigi[1].insert(10, dokter_gigi_new)
                print("Anda telah berhasil menambahkan jadwal dokter gigi: ", Dokter_gigi[1])
            elif pilih_hari == "rabu":
                nama = input("Nama Dokter: ")
                jam = input("Jam Praktik: ")
                dokter_gigi_new = (nama, jam)
                Dokter_gigi[2].insert(10, dokter_gigi_new)
                print("Anda telah berhasil menambahkan jadwal dokter gigi: ", Dokter_gigi[2])
            elif pilih_hari == "kamis":
                nama = input("Nama Dokter: ")
                jam = input("Jam Praktik: ")
                dokter_gigi_new = (nama, jam)
                Dokter_gigi[3].insert(10, dokter_gigi_new)
                print("Anda telah berhasil menambahkan jadwal dokter gigi: ", Dokter_gigi[3])
            elif pilih_hari == "jumat":
                nama = input("Nama Dokter: ")
                jam = input("Jam Praktik: ")
                dokter_gigi_new = (nama, jam)
                Dokter_gigi[4].insert(10, dokter_gigi_new)
                print("Anda telah berhasil menambahkan jadwal dokter gigi: ", Dokter_gigi[4])
            else:
                print("Terdapat Kesalahan")
        elif pilih_spesialis == "2":
            pilih_hari = input("Tentukan Hari: ")
            if pilih_hari == "senin":
                nama = input("Nama Dokter: ")
                jam = input("Jam Praktik: ")
                dokter_anak_new = (nama, jam)
                Dokter_anak[0].insert(10, dokter_anak_new)
                print("Anda telah berhasil menambahkan jadwal dokter anak: ", Dokter_anak[0])
            elif pilih_hari == "selasa":
                nama = input("Nama Dokter: ")
                jam = input("Jam Praktik: ")
                dokter_anak_new = (nama, jam)
                Dokter_anak[1].insert(10, dokter_anak_new)
                print("Anda telah berhasil menambahkan jadwal dokter anak: ", Dokter_anak[1])
            elif pilih_hari == "rabu":
                nama = input("Nama Dokter: ")
                jam = input("Jam Praktik: ")
                dokter_anak_new = (nama, jam)
                Dokter_anak[2].insert(10, dokter_anak_new)
                print("Anda telah berhasil menambahkan jadwal dokter anak: ", Dokter_anak[2])
            elif pilih_hari == "kamis":
                nama = input("Nama Dokter: ")
                jam = input("Jam Praktik: ")
                dokter_anak_new = (nama, jam)
                Dokter_anak[3].insert(10, dokter_anak_new)
                print("Anda telah berhasil menambahkan jadwal dokter anak: ", Dokter_anak[3])
            elif pilih_hari == "jumat":
                nama = input("Nama Dokter: ")
                jam = input("Jam Praktik: ")
                dokter_anak_new = (nama, jam)
                Dokter_anak[4].insert(10, dokter_anak_new)
                print("Anda telah berhasil menambahkan jadwal dokter anak: ", Dokter_anak[4])
            else:
                print("Terdapat Kesalahan")
        elif pilih_spesialis == "3":
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
        else:
            print("Menu tidak valid, silahkan coba lagi")
else:
    print("Menu tidak valid, silahkan coba lagi")