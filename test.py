# # # Soal: Aplikasi Buku di Perpustakaan
# # # Buatlah aplikasi sederhana untuk sistem buku di perpustakaan dengan fitur-fitur berikut:
# # # Menampilkan daftar buku yang tersedia
# # # User ditawarkan ingin mencari buku dengan filter atau tidak
# # # kalau iya maka:
# # # Terdapat opsi untuk filter berdasarkan
# # # Penerbit
# # # Tahun diterbitkan
# # # status available atau tidak
# # # kalau tidak ke main menu
# # # Menambahkan buku baru
# # # Menghapus buku
# # # Exit Aplikasi

# # list_buku = [
# #     {"penerbit": "Gramedia Pustaka Utama", "judul": "Laut Bercerita", "tahun_diterbitkan": 2017, "dipinjam": 15, "status": "Tersedia"},
# #     {"penerbit": "Erlangga", "judul": "Filosofi Teras", "tahun_diterbitkan": 2018, "dipinjam": 22, "status": "Dipinjam"},
# #     {"penerbit": "Bentang Pustaka", "judul": "Bumi", "tahun_diterbitkan": 2014, "dipinjam": 30, "status": "Tersedia"},
# #     {"penerbit": "Mizan", "judul": "Negeri 5 Menara", "tahun_diterbitkan": 2009, "dipinjam": 18, "status": "Tersedia"},
# #     {"penerbit": "GagasMedia", "judul": "Critical Eleven", "tahun_diterbitkan": 2015, "dipinjam": 25, "status": "Dipinjam"},
# #     {"penerbit": "Bukune", "judul": "Catatan Juang", "tahun_diterbitkan": 2017, "dipinjam": 10, "status": "Tersedia"},
# #     {"penerbit": "Noura Books", "judul": "Dilan: Dia adalah Dilanku Tahun 1990", "tahun_diterbitkan": 2014, "dipinjam": 40, "status": "Dipinjam"},
# #     {"penerbit": "Deepublish", "judul": "Metode Penelitian Kualitatif", "tahun_diterbitkan": 2016, "dipinjam": 12, "status": "Tersedia"},
# #     {"penerbit": "Andi Publisher", "judul": "Belajar Python untuk Pemula", "tahun_diterbitkan": 2021, "dipinjam": 8, "status": "Tersedia"},
# #     {"penerbit": "Penerbit Buku Kompas", "judul": "Sapiens: Riwayat Singkat Umat Manusia", "tahun_diterbitkan": 2011, "dipinjam": 35, "status": "Dipinjam"},
# # ]

# # def tambah_buku():
# #     penerbit = str(input("Masukkan nama penerbit: "))
# #     judul = str(input("Masukkan judul buku: "))
# #     while True:
# #         tahun_terbit = str(input("Masukkan tahun terbit: "))
# #         if tahun_terbit.isdigit() == True:
# #             break
# #         else:
# #             print("Masukkan hanya angka")
# #     while True:
# #         dipinjam = str(input("Berapa kali buku ini sudah dipinjam: "))
# #         if dipinjam.isdigit() == True:
# #             break
# #         else:
# #             print("Masukkan hanya angka")
# #     while True:
# #         print('Status peminjaman\n1. Tersedia\n2. Dipinjam')
# #         status = str(input("Pilih status peminjaman buku: "))
# #         if status == '1':
# #             status = 'Tersedia'
# #             break
# #         elif status == '2':
# #             status = 'Dipinjam'
# #             break
# #         elif status.isdigit() == True:
# #             print('Hanya masukkan pilihan yang tersedia')
# #         else:
# #             print('Hanya bisa masukkan angka')
# #     buku_baru = {
# #     "penerbit": penerbit,
# #     "judul": judul,
# #     "tahun_diterbitkan": int(tahun_terbit),
# #     "dipinjam": int(dipinjam),
# #     "status": status,
# #     }
# #     list_buku.append(buku_baru)

# # def menghapus_buku():
# #     judul_dihapus = str(input("Masukkan judul buku yang ingin dihapus: "))
# #     cek_buku = 0
# #     indexing = 0
# #     for i in list_buku:
# #         if i['judul'] == judul_dihapus:
# #             cek_buku += 1
# #             del list_buku[indexing]
# #             print(f'Buku berjudul {i['judul']} berhasil dihapus')
# #             indexing += 1
# #         else:
# #             indexing += 1
# #     if cek_buku == 0:
# #         print("Buku tidak ditemukan")

# # def tampilkan_buku(data):
# #     print('List Buku\n===========================================================================================================================')
# #     for i in data:
# #         print(f'Judul: {i["judul"]}, Penerbit: {i["penerbit"]}, Tahun Terbit: {i["tahun_diterbitkan"]}, Dipinjam: {i["dipinjam"]} kali, Status: {i["status"]}')

# # def filter_penerbit(keyword):
# #     print(f'Pencarian Penerbit berdasarkan kata kunci: {keyword.lower()}\n===========================================================================================================================')
# #     count = 0
# #     for i in list_buku:
# #         if keyword.lower() in i['penerbit'].lower():
# #             count += 1
# #             print(f'Judul: {i["judul"]}, Penerbit: {i["penerbit"]}, Tahun Terbit: {i["tahun_diterbitkan"]}, Dipinjam: {i["dipinjam"]} kali, Status: {i["status"]}')
# #     if count == 0:
# #         print("Maaf kami tidak dapat menemukan hasil berdasarkan kata kunci yang digunakan")
# #     else:
# #         print(f'=========================================================================================================================== \nTerdapat {count} buku berdasarkan filter yang digunakan')

# # def filter_tahun_terbit(keyword):
# #     print(f'Pencarian Tahun Terbit berdasarkan kata kunci: {keyword}\n===========================================================================================================================')
# #     count = 0
# #     for i in list_buku:
# #         if str(keyword) in str(i['tahun_diterbitkan']):
# #             count += 1
# #             print(f'Judul: {i["judul"]}, Penerbit: {i["penerbit"]}, Tahun Terbit: {i["tahun_diterbitkan"]}, Dipinjam: {i["dipinjam"]} kali, Status: {i["status"]}')
# #     if count == 0:
# #         print("Maaf kami tidak dapat menemukan hasil berdasarkan kata kunci yang digunakan")
# #     else:
# #         print(f'=========================================================================================================================== \nTerdapat {count} buku berdasarkan filter yang digunakan')

# # def filter_ketersediaan(keyword):
# #     keyword = keyword.lower()
# #     count = 0 
# #     print(f'Pencarian berdasarkan ketersediaan: \n===========================================================================================================================')
# #     if keyword == '1':
# #         for i in list_buku:
# #             if i["status"] == "Tersedia":
# #                 count += 1
# #                 print(f'Judul: {i["judul"]}, Penerbit: {i["penerbit"]}, Tahun Terbit: {i["tahun_diterbitkan"]}, Dipinjam: {i["dipinjam"]} kali, Status: {i["status"]}')
# #     elif keyword == "2":
# #         for i in list_buku:
# #             if i["status"] == "Dipinjam":
# #                 count += 1
# #                 print(f'Judul: {i["judul"]}, Penerbit: {i["penerbit"]}, Tahun Terbit: {i["tahun_diterbitkan"]}, Dipinjam: {i["dipinjam"]} kali, Status: {i["status"]}')
# #     print(f'=========================================================================================================================== \nTerdapat {count} buku berdasarkan filter yang digunakan')

# # def halaman_filter():
# #     while True:
# #                 print("Pilih filter berdasarkan:")
# #                 print("1. Penerbit")
# #                 print("2. Tahun Terbit")
# #                 print("3. Status Ketersediaan")
# #                 pilih_filter = str(input("Masukkan angka sesuai filter yang diinginkan: "))
# #                 if pilih_filter == "1":
# #                     keyword_filter = str(input("Masukkan kata kunci untuk filter Penerbit: "))
# #                     filter_penerbit(keyword_filter)
# #                     kembali_halaman_filter()
# #                 elif pilih_filter == "2":
# #                     while True:
# #                         keyword_filter = str(input("Masukkan kata kunci untuk filter Tahun Terbit: "))
# #                         if keyword_filter.isdigit() == True:
# #                             filter_tahun_terbit(keyword_filter)
# #                             kembali_halaman_filter()
# #                         else:
# #                             print('Hanya menerima format angka')
# #                 elif pilih_filter == "3":
# #                     print("Pilih filter")
# #                     print("1. Tersedia")
# #                     print("2. Sedang Dipinjam")
# #                     while True:
# #                         keyword_filter = str(input("Pilih filter ketersediaan sesuai yang diinginkan: "))
# #                         if keyword_filter == '1' or keyword_filter == '2':
# #                             filter_ketersediaan(keyword_filter)
# #                             kembali_halaman_filter()
# #                         else:
# #                             print("Harap masukkan pilihan yang sesuai dengan pilihan yang ada")
                    
# # def kembali_ke_menu_utama():
# #     kembali = str(input("Ketik Y untuk kembali ke menu utama: "))
# #     if kembali.lower() == 'y':
# #         start()
# #     else: 
# #         print("masukan sesuai format")
# #         kembali_ke_menu_utama()

# # def kembali_halaman_filter():
# #     print("Kembali ke:")
# #     while True:
# #         pilih_halaman = str(input("1. Menu utama\n2. Pilih filter lainnya\n Masukkan pilihan sesuai pilihan yang ada: "))
# #         if pilih_halaman == "1":
# #             start()
# #         elif pilih_halaman =="2":
# #             halaman_filter()

# # def start():
# #     print("Selamat datang dalam aplikasi Perpustakan Online Purwadhika\n===========================================================================================================================")
# #     print("1. Tampilkan list buku yang ada pada perpustakaan")
# #     print("2. Menambahkan buku baru")
# #     print("3. Menghapus buku")
# #     print("4. Keluar")
# #     while True:
# #         pilihan_menu_utama = str(input("Masukkan angka sesuai pilihan yang diinginkan: "))
# #         if pilihan_menu_utama == "1":
# #             while True:
# #                 lanjut_filter = str(input("Apakah anda ingin mengaktifkan filter terhadap list buku yang ada (Y/N)? "))
# #                 if lanjut_filter.lower() == "y":
# #                     halaman_filter()
# #                 elif lanjut_filter.lower() == "n":
# #                     tampilkan_buku(list_buku)
# #                     kembali_ke_menu_utama()
# #                 else :
# #                     print("Masukkan sesuai format yang diminta")
# #         elif pilihan_menu_utama == "2":
# #             tambah_buku()
# #             print("Buku berhasil ditambahkan")
# #             kembali_ke_menu_utama()
# #         elif pilihan_menu_utama == "3":
# #             menghapus_buku()
# #             kembali_ke_menu_utama()
# #         elif pilihan_menu_utama == "4":
# #             print('Menutup aplikasi')
# #             break
# #         elif pilihan_menu_utama.isdigit() == False :
# #             print("Format hanya bisa berisi angka")
# #         else :
# #             print("Masukkan hanya angka sesuai pilihan yang ada")

# # start()

# from tabulate import tabulate
# list_buku= [
#     {
#         "Penerbit" : "John Lenon",
#         "Judul buku" : "JohnDoe",
#         "Tahun diterbitkan" : "2011",
#         "Jumlah dipinjam" : "10",
#         "Status" : "Booked"
#     }
# ]


# #contoh implementasi tabulate
# def menampilkan_list_buku():
#     # Ubah list buku ke format list of lists untuk tabulate
#     # Library tabulate memang mengharuskan data harus berbentuk list dalam list
#     data = []
#     index = 0
#     for buku in list_buku:
#         data.append([
#             index,  # Index buku
#             buku["Penerbit"],  # Penerbit buku
#             buku["Judul buku"],  # Judul buku
#             buku["Tahun diterbitkan"],  # Tahun diterbitkan
#             buku["Jumlah dipinjam"],  # Jumlah buku yang dipinjam
#             buku["Status"]  # Status ketersediaan buku
#         ])
#         index += 1  # Increment index setiap kali loop
#     # Cetak tabel
#     print("Daftar Buku\n")
#     print(tabulate(data, headers=["Index", "Penerbit", "Judul Buku", "Tahun", "Dipinjam", "Status"], tablefmt="grid"))
#     print()
#     print(data)

# menampilkan_list_buku()

# my_list = []
# for i in range (1, 6):
#     if i == 3:
#         continue
#     my_list.append(i)
# print(my_list)


phrase = "Skill Accelerator Bootcamp"
print(phrase[2:24])



