# Dictionary di Python
# Dictionary adalah tipe data yang menyimpan data dalam bentuk pasangan key-value
# Format: {key: value, key: value, key: value}

my_dictionary = {'nilai': 89, 'nama': 'Faroja', 'Alamat': 'Tangerang Selatan', 'umur': 19}

# Akses Data dalam Dictionary
# Untuk mengakses data di dalam dictionary, kita menggunakan **key** sebagai acuan, bukan index
print(my_dictionary['nilai'])  # Output: 89
print(my_dictionary['nama'])   # Output: Faroja

# Menggunakan method .get() juga bisa untuk mengakses data dengan key
print(my_dictionary.get('nama'))  # Output: Faroja
print(my_dictionary.get('nilai'))  # Output: 89

# Mengubah data dalam Dictionary
# Untuk mengubah nilai, kita menggunakan key yang sudah ada dan mengubah nilainya
my_dictionary['nilai'] = 120
print(my_dictionary['nilai'])  # Output: 120

# Menambahkan data baru ke dalam Dictionary
my_dictionary['Peliharaan'] = 'Kucing'
print(my_dictionary)  # Output: {'nilai': 120, 'nama': 'Faroja', 'Alamat': 'Tangerang Selatan', 'umur': 19, 'Peliharaan': 'Kucing'}

# Menghapus data dalam Dictionary
# Menghapus data dengan key tertentu
del my_dictionary['Peliharaan']  # Menghapus key 'Peliharaan'
# Menggunakan pop untuk menghapus key dengan cara lain
my_dictionary.pop('nilai')  # Menghapus key 'nilai' beserta value-nya
# Menghapus item terakhir dengan popitem (tidak perlu key)
my_dictionary.popitem()  # Menghapus item terakhir yang ada di dictionary
print(my_dictionary)  # Output: {'nama': 'Faroja', 'Alamat': 'Tangerang Selatan', 'umur': 19}

# Menghapus seluruh isi dictionary
my_dictionary.clear()  # Semua key dan value dalam dictionary akan terhapus
print(my_dictionary)  # Output: {}

# Kesimpulan:
# Dictionary mirip dengan list dan tuple dalam beberapa cara, tetapi berbeda karena akses menggunakan key, bukan index.

# Menggunakan Dictionary
my_dictionary = {'nilai': 89, 'nama': 'Faroja', 'Alamat': 'Tangerang Selatan', 'umur': 19}

# Jenis-jenis Looping pada Dictionary:
# Looping dengan mengakses key secara langsung
for key in my_dictionary:
    print(f'{key} = {my_dictionary[key]}')

# Looping dengan .keys() untuk mendapatkan keys
for key in my_dictionary.keys():
    print(f'Key dalam dictionary: {key}')

# Looping dengan .values() untuk mendapatkan values
for value in my_dictionary.values():
    print(f'Value dalam dictionary: {value}')

# Looping dengan .items() untuk mendapatkan pasangan key dan value
for key, value in my_dictionary.items():
    print(f'Key: {key}, Value: {value}')

# Mengecek apakah suatu key ada dalam dictionary
if 'nama' in my_dictionary:
    print('Key "nama" ada dalam dictionary')

# Mengecek apakah key ada menggunakan .keys()
if 'nama' in my_dictionary.keys():
    print('Key "nama" ada dalam dictionary')

# Mengecek apakah value ada dalam dictionary
if 'Faroja' in my_dictionary.values():
    print('Value "Faroja" ada dalam dictionary')

# Menggunakan len() untuk menghitung jumlah pasangan key-value dalam dictionary
print(len(my_dictionary))  # Output: 4 (jumlah pasangan key-value dalam dictionary)

# Menyalin (copy) dictionary
my_dictionary_2 = my_dictionary.copy()  # Membuat salinan dari dictionary
my_dictionary_2.clear()  # Menghapus semua isi dari dictionary salinan
print(my_dictionary_2)  # Output: {}
print(my_dictionary)  # Output: {'nilai': 89, 'nama': 'Faroja', 'Alamat': 'Tangerang Selatan', 'umur': 19}

# Tanpa menggunakan method copy, hanya mereferensikan dictionary yang sama
my_dictionary_2 = my_dictionary
my_dictionary_2.clear()  # Menghapus semua isi dictionary yang terreferensikan
print(my_dictionary_2)  # Output: {}
print(my_dictionary)  # Output: {}

# Dictionary dalam Dictionary (nested dictionary)
my_dictionary_3 = {
    'Alamat': {'Sauyunan', 'Tangerang', 'Sukabumi'},
    'Nama': {'Faroja', 'Farhan', 'Fikri'},
    'Nilai': {88, 90, 100}
}
print(my_dictionary_3)  # Output: {'Alamat': {'Sauyunan', 'Tangerang', 'Sukabumi'}, 'Nama': {'Faroja', 'Farhan', 'Fikri'}, 'Nilai': {88, 90, 100}}
