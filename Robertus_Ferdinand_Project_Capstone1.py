#Project Data Buku
from tabulate import tabulate
import sys

#region greeting / pembukaan pada saat program berjalan
def greetings():
    print("Selamat Datang di Gudang perpusatakaan\nKami menyediakan berbagai koleksi buku yang menarik untuk kamu baca\nJangan ragu untuk mengeksplorasi buku yang kami miliki :)\n")
#endregion

#region dictionary buku
gudang_buku = {
    "BOOK01":{"Judul": "Laskar Pelangi", "Penulis": "Andrea", "Tahun Pembuatan": "2001", "Penerbit": "Gramedia","Status":"Available", "Negara Penerbit": "Indonesia"},
    "BOOK02":{"Judul": "Book Of New York", "Penulis": "Hafiz", "Tahun Pembuatan": "2005", "Penerbit": "Gramedia","Status":"Available", "Negara Penerbit": "Indonesia"},
    "BOOK03":{"Judul": "Jakarta", "Penulis": "Haniff", "Tahun Pembuatan": "2006", "Penerbit": "Gramedia","Status":"Available", "Negara Penerbit": "Indonesia"},
    "BOOK04":{"Judul": "Why? : Bumi berbentuk bulat", "Penulis": "Jason", "Tahun Pembuatan": "2003", "Penerbit": "Gramedia","Status":"Available", "Negara Penerbit": "Indonesia"},
    "BOOK05":{"Judul": "Manusia Ikan", "Penulis": "Denny", "Tahun Pembuatan": "2002", "Penerbit": "Gramedia","Status":"Available", "Negara Penerbit": "Indonesia"},
    "BOOK06":{"Judul": "Hidup Sederhana", "Penulis": "Vanessa", "Tahun Pembuatan": "1991", "Penerbit": "Gramedia","Status":"Available", "Negara Penerbit": "Indonesia"},
    "BOOK07":{"Judul": "How To Manage Currency", "Penulis": "Graham", "Tahun Pembuatan": "1998", "Penerbit": "Gramedia","Status":"Available", "Negara Penerbit": "Indonesia"},
    "BOOK08":{"Judul": "Book Of Capitalism", "Penulis": "Benjamin", "Tahun Pembuatan": "1999", "Penerbit": "Gramedia","Status":"Available", "Negara Penerbit": "Indonesia"}
}
#endregion

#region Filter Function / menampilkan seluruh buku
def menampilkan_keseluruhan_buku():
    #Menampilkan keselurahan buku
    if gudang_buku:
        print("Berikut daftar-daftar buku yang tersedia yaa !")
        data_buku = []
        index = 1
        for key, buku in gudang_buku.items():
            data_buku.append([
                index,
                key,
                buku["Judul"],
                buku["Penulis"],
                buku["Tahun Pembuatan"],
                buku["Penerbit"],
                buku["Status"],
                buku["Negara Penerbit"]
            ])
            index += 1
        
        print(tabulate(data_buku, headers=["Nomor", "Id Buku", "Judul Buku", "Penulis Buku", "Tahun Pembuatan Buku", "Penerbit Buku", "Availability Buku", "Negara Penerbit"], tablefmt="grid"))
    else:
        print("Data tidak ada")

def menampilkan_buku_sesuai_filter_by_tahun():
    if gudang_buku:
        while True:
            try:
                pilih_tahun = str(input("Silahkan masukan tahun buku yang kamu ingin cari: ")).strip()
                hasil_pencarian = [
                    [      
                        key,
                        buku["Judul"],
                        buku["Penulis"],
                        buku["Tahun Pembuatan"],
                        buku["Penerbit"],
                        buku["Status"],
                        buku["Negara Penerbit"]
                    ]

                    for key, buku in gudang_buku.items() if buku["Tahun Pembuatan"] == pilih_tahun
                ]
                if hasil_pencarian:
                    print("\nBuku yang kamu cari tersedia:\n")
                    print(tabulate(hasil_pencarian, headers=["BookId","Judul Buku", "Penulis Buku", "Tahun Pembuatan Buku", "Penerbit Buku", "Availability Buku", "Negara Penerbit"], tablefmt="grid"))
                else:
                    print("\nMohon maaf buku yang kamu cari tidak tersedia!\n")
                    return menampilkan_buku_sesuai_filter()
                
                cari_lagi = input("Apakah ada buku yang masih ingin kamu cari ? (Y/N): ").strip().lower()
                if cari_lagi != 'y':
                    return menampilkan_buku_sesuai_filter()
            except ValueError:
                print("Silahkan masukan judul buku yang valid!")
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"{e}")
    else:
        print("Data tidak ada")

def menampilkan_buku_sesuai_filter_by_id():  
    if gudang_buku:
        while True:
            try:
                pilih_buku = str(input("Silahkan masukan buku id yang kamu inginkan: ")).strip().upper()
                if pilih_buku in gudang_buku:
                    buku = gudang_buku[pilih_buku]
                    hasil_pencarian = [
                        [      
                            pilih_buku,
                            buku["Judul"],
                            buku["Penulis"],
                            buku["Tahun Pembuatan"],
                            buku["Penerbit"],
                            buku["Status"],
                            buku["Negara Penerbit"]
                        ]
                    ]
                    print(tabulate(hasil_pencarian, headers=["BookId", "Judul Buku", "Penulis Buku", "Tahun Pembuatan Buku", "Penerbit Buku", "Availability Buku", "Negara Penerbit"], tablefmt="grid"))
                else:
                    print("Mohon maaf buku yang kamu cari tidak ada!")
                    return menampilkan_buku_sesuai_filter()
                cari_lagi = input("Apakah ada buku yang masih ingin kamu cari ? (Y/N): ").strip().lower()
                if cari_lagi != 'y':
                    return menampilkan_buku_sesuai_filter()

            except ValueError:
                print("Silahkan masukan judul buku yang valid!")
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"{e}")
    else:
        print("data tidak ada")
       
def menampilkan_buku_sesuai_filter_by_judul():
    if gudang_buku:
        while True:
            try:
                pilih_buku = str(input("Silahkan masukan judul buku yang kamu inginkan: ")).strip().title()
                hasil_pencarian = [
                    [      
                        key,
                        buku["Judul"],
                        buku["Penulis"],
                        buku["Tahun Pembuatan"],
                        buku["Penerbit"],
                        buku["Status"],
                        buku["Negara Penerbit"]
                    ]

                    for key, buku in gudang_buku.items() if pilih_buku in buku["Judul"].lower()
                ]
                if hasil_pencarian:
                    print("\nBuku yang kamu cari tersedia:\n")
                    print(tabulate(hasil_pencarian, headers=["Id","Judul Buku", "Penulis Buku", "Tahun Pembuatan Buku", "Penerbit Buku", "Availability Buku", "Negara Penerbit"], tablefmt="grid"))
                else:
                    print("\nMohon maaf buku yang kamu cari tidak tersedia!\n")
                    return menampilkan_buku_sesuai_filter()
                
                cari_lagi = input("Apakah ada buku yang masih ingin kamu cari ? (Y/N): ").strip().lower()
                if cari_lagi == 'y':
                    return menampilkan_buku_sesuai_filter()
        
            except ValueError:
                print("Silahkan masukan judul buku yang valid!")
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"{e}")
    else:
        print("data tidak ada")

def menampilkan_buku_sesuai_filter():
    if gudang_buku:
        while True:
            print('\n')
            print("1. Menampilkan buku sesuai BookId")
            print("2. Menampilkan buku sesuai Judul Buku")
            print("3. Menampilkan buku sesuai tahun penerbit")
            print("4. Kembali ke menu buku")
            try:
                pilihan = int(input("Silahkan masukan yang kamu inginkan ya (1-3): "))
                if pilihan == 1:
                    menampilkan_buku_sesuai_filter_by_id()
                elif pilihan == 2:
                    menampilkan_buku_sesuai_filter_by_judul()
                elif pilihan == 3:
                    menampilkan_buku_sesuai_filter_by_tahun()
                elif pilihan == 4:
                    return menu_buku()
                else:
                    print("Silahkan masukan angka yang valid yaa")

            except ValueError:
                print("Silahkan masukan angka yang valid yaa!")
            except KeyboardInterrupt:
                return menu_buku()
            except Exception as e:
                print(f"{e}")
    else:
        print("data tidak ada")

def menu_buku():
     while True:
         print("\nSilahkan pilih opsi buku yang kamu inginkan: ")
         print("1. Tampilkan seluruh buku")
         print("2. Mencari buku yang spesifik")
         print("3. Kembali ke menu utama")

         try:
             pilihan = int(input("Silahkan masukan pilihan yang diinginkan (1-3): "))

             if pilihan == 1:
                menampilkan_keseluruhan_buku()
             elif pilihan == 2:
                menampilkan_buku_sesuai_filter()
             elif pilihan == 3:
                return menu_utama()
             else:
                print("\nSilahkan masukan angka yang valid yaa (1-3)!")
         except ValueError:
             print("\nSilahkan masukan angka yang valid yaa!")
         except KeyboardInterrupt:
                break
         except Exception as e:
             print(f"{e}")
#endregion

#region Add Books / Include main menu for add books choices
def tambah_buku():
    while True:
        try:
            masukan_id = str(input("Silahkan masukan id baru yang kamu inginkan yaa: ")).strip().upper()
            if masukan_id in gudang_buku:
                print("Id yang kamu masukan telah tersedia")
            while True:
                masukan_judul = input("Silahkan masukan judul baru yang kamu inginkan yaa: ").strip().title()
                masukan_penulis = input("Masukan penulis dari buku tersebut yaa: ").strip().title()
                masukan_tahun = input("Masukan tahun pembuatan dari buku tersebut yaa: ").strip()
                masukan_penerbit = input("Masukan penerbit dari buku tersebut: ").strip().title()
                masukan_status = "Available"
                masukan_negara_penerbit = "Indonesia"
                
                print("\n Konfirmasi input data buku")
                print(f"Id Buku : {masukan_id}")
                print(f"Judul: {masukan_judul}")
                print(f"Penulis: {masukan_penulis}")
                print(f"Tahun pembuatan: {masukan_tahun}")
                print(f"Penerbit Buku: {masukan_penerbit}")
                print(f"Status: {masukan_status}")
                print(f"Negara Penerbit: {masukan_negara_penerbit}")

                input_validasi = input("Apakah kamu yakin dengan data yang kamu input ? (Y/N)").lower()
                if input_validasi == 'y':
                    gudang_buku[masukan_id]={
                        "Judul":masukan_judul,
                        "Penulis":masukan_penulis,
                        "Tahun Pembuatan": masukan_tahun,
                        "Penerbit": masukan_penerbit,
                        "Status": masukan_status,
                        "Negara Penerbit": masukan_negara_penerbit
                    }
                    print("Data berhasil di input")
                else:
                    print("Silahkan masukan kembali yaa")
                tambah_lagi = input("\nApakah kamu ingin menambahkan buku lainnya ? (Y/N)").strip().lower()
                if tambah_lagi != "y":
                    return tambah_buku_menu()
        except ValueError:
            print("Mohon masukan id dengan kombinasi huruf dan angka yaa!")
        except KeyboardInterrupt:
            return tambah_buku_menu()
        except Exception as e:
            print(f"{e}")

def tambah_buku_menu():
    if gudang_buku:
        while True:
            print("\n1. Tambah Buku")
            print("2. Kembali ke menu utama")
            try:
                pilihan = int(input("Silahkan masukan pilihan kamu (1-2):"))
                if pilihan == 1:
                    tambah_buku()
                elif pilihan == 2:
                    return menu_utama()
                else:
                    print("\nSilahkan masukan angka yang sesuai yaa (1-2)")
            except ValueError:
                print("\nSilahkan masukan angka yang valid ya!")
            except KeyboardInterrupt:
                return menu_utama()
            except Exception as e:
                print(f"{e}")
    else:
        print("Data tidak ada")

#endregion

#region hapus buku / main menu hapus buku

def hapus_buku():
    if gudang_buku:
        while True:
            try:   
                masukan_id = str(input("\nSilahkan masukan buku id yang ingin kamu hapus yaa: ")).upper().strip()
                if masukan_id in gudang_buku:
                    buku = gudang_buku[masukan_id]
                    hasil_pencarian = [
                        [
                            masukan_id,
                            buku["Judul"],
                            buku["Penulis"],
                            buku["Tahun Pembuatan"],
                            buku["Penerbit"],
                            buku["Status"],
                            buku["Negara Penerbit"]
                        ]
                    ]
                    print(tabulate(hasil_pencarian, headers=["Book Id", "Judul", "Penulis", "Tahun", "Penerbit", "Status", "Negara"], tablefmt="grid"))

                    validasi_akhir = input("Apakah kamu yakin ingin menghapus data tersebut ? (Y/N)").lower().strip()
                    if validasi_akhir == 'y':
                        del gudang_buku[masukan_id]
                        print(f"Buku dengan ID {masukan_id} telah berhasil di hapus")
                    else:
                        print("Dibatalkan")
                else:
                    print("\nData tidak ditemukan\n")
                hapus_lagi = input("Apakah ada buku lain yang ingin dihapus kembali ? (Y/N)").lower()
                if hapus_lagi != 'y':
                    return hapus_buku_menu()
            except ValueError:
                print("\nSilahkan masukan id yang valid ya, berikut dengan huruf dan angkanya!")
            except KeyboardInterrupt:
                return hapus_buku_menu()
            except Exception as e:
                print(f"{e}")
        
def hapus_buku_menu():
    while True:
        print("\n Silahkan pilih menu yang diinginkan !")
        print("1. Menghapus buku sesuai book id")
        print("2. Kembali ke menu utama")
        try:
            pilihan = int(input("Silahkan pilih opsi yang kamu inginkan yaa (1-2): "))
            if pilihan == 1:
                hapus_buku()
            elif pilihan == 2:
                return menu_utama()
            else:
                print("Silahkan pilih opsi yang valid ya (1-2)")
        except ValueError:
            print("Silahkan masukan angka yang valid yaa")
        except KeyboardInterrupt:
            return menu_utama()
        
#endregion

#region update buku / main menu update buku
def update_buku():
    if gudang_buku:
        while True:
            masukan_id = str(input("Silahkan masukan id buku yang ingin diupdate: ")).strip().upper()
            if masukan_id in gudang_buku:
                buku = gudang_buku[masukan_id]
                hasil_pencarian = [
                    [
                        masukan_id,
                        buku["Judul"],
                        buku["Penulis"],
                        buku["Tahun Pembuatan"],
                        buku["Penerbit"],
                        buku["Status"],
                        buku["Negara Penerbit"]
                    ]
                ]
                print(tabulate(hasil_pencarian, headers=["BookId", "Judul Buku", "Penulis", "Tahun Pembuatan", "Penerbit", "Status", "Negara Penerbit"], tablefmt="grid"))
                validasi_update_1 = input("Apakah ingin melanjutkan untuk mengupdate buku ini ? (Y/N)").lower()
                if validasi_update_1 == 'y':
                    masukan_kolom = input("Pilih kolom yang ingin di update: ").strip().title()
                    if masukan_kolom in buku:
                        isi_baru_dari_kolom = input("Masukan isi baru yang diinginkan pada kolom tersebut: ").strip().title()
                        buku[masukan_kolom] = isi_baru_dari_kolom
                        hasil_pencarian = [
                            [
                                masukan_id,
                                buku["Judul"],
                                buku["Penulis"],
                                buku["Tahun Pembuatan"],
                                buku["Penerbit"],
                                buku["Status"],
                                buku["Negara Penerbit"]
                            ]
                        ]
                    print(tabulate(hasil_pencarian, headers=["BookId", "Judul Buku", "Penulis", "Tahun Pembuatan", "Penerbit", "Status", "Negara Penerbit"], tablefmt="grid"))
                else:
                    break
            else:
                print("Data tidak ditemukan!")

            update_lagi = input("Apakah ingin mengupdate buku kembali? (Y/N)").lower()
            if update_lagi != 'y':
                return update_buku_menu()
def update_buku_menu():
    if gudang_buku:
        while True:
            print("Update Buku!")
            print("1. Update Book by Id")
            print("2. Kembali ke menu utama")
            try:
                pilihan = int(input("Silahkan pilih opsi yang kamu inginkan yaa (1-2): "))
                if pilihan == 1:
                    update_buku()
                elif pilihan == 2:
                    return menu_utama()
                else:
                    print("Silahkan masukan angka yang valid yaa (1-2)\n")
            except ValueError:
                print("Silahkan masukan angka yang valid yaa!")
            except KeyboardInterrupt:
                return menu_utama()
            except Exception as e :
                print(f"{e}")
#endregion

#region exit Function
def keluar():
    print("\nTerima kasih telah mengunjungi buku perpusatakaan kami. Sampai jumpa !")
    sys.exit()
#endregion

def menu_utama():
    greetings()
    while True:
        print("\nSilahkan pilih menu yang kamu inginkan!")
        print("1. Melihat buku")
        print("2. Tambah koleksi buku baru")
        print("3. Update koleksi buku")
        print("4. Hapus koleksi buku")
        print("5. Keluar")
        try:
            pilihan = int(input("Masukan Pilihan yang diinginkan (1-4): "))
            if pilihan == 1:
                menu_buku()
            elif pilihan == 2:
                print("Selamat datang di menu untuk menambahkan buku!\n")
                tambah_buku_menu()
            elif pilihan == 3:
                #update_judul buku()
                update_buku_menu()
            elif pilihan == 4:
                hapus_buku_menu()
            elif pilihan == 5:
                keluar()
            else:
                print("\nMohon Masukan angka yang valid yaa !")
        except ValueError:
            print("\nPilihan kamu tidak sesuai, mohon masukan kembali pilihan menu yang diinginkan")
        except KeyboardInterrupt:
            print("\nTerima kasih telah mengunjungi. Sampai jumpaa!")
            break
        except Exception as e:
            print(f"{e}")
            break
menu_utama()
            

