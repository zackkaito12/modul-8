FILE_NAME = 'zack.txt'

def baca_data():
    data = {}
    try:
        with open(FILE_NAME, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.strip():
                    judul, penulis, penerbit, tahun = line.strip().split('|')
                    data[judul] = {
                        'penulis': penulis,
                        'penerbit': penerbit,
                        'tahun': tahun
                    }
    except FileNotFoundError:
        pass
    return data

def simpan_data(data):
    with open(FILE_NAME, 'w') as file:
        for judul, info in data.items():
            file.write(f"{judul}|{info['penulis']}|{info['penerbit']}|{info['tahun']}\n")

def tampilkan_data(data):
    if not data:
        print("Belum ada buku yang disimpan.")
    else:
        for index, (judul, info) in enumerate(data.items(), start=1):
            print(f"{index}. Judul: {judul}")
            print(f"   Penulis: {info['penulis']}")
            print(f"   Penerbit: {info['penerbit']}")
            print(f"   Tahun Terbit: {info['tahun']}")
            print("")

def inpu_data(data):
    judul = input("Masukkan judul buku: ")
    penulis = input("Masukkan nama penulis: ")
    penerbit = input("Masukkan nama penerbit: ")
    tahun = input("Masukkan tahun terbit: ")
    data[judul] = {
        'penulis': penulis,
        'penerbit': penerbit,
        'tahun': tahun
    }
    simpan_data(data)
    print(f"Buku '{judul}' telah ditambahkan.")

def hapus_data(data):
    judul = input("Masukkan judul buku yang ingin dihapus: ")
    if judul in data:
        del data[judul]
        simpan_data(data)
        print(f"Buku '{judul}' telah dihapus.")
    else:
        print(f"Buku '{judul}' tidak ditemukan.")

def menu():
    data = baca_data()
    while True:
        print("\nMenu:")
        print("1. Tampilkan daftar buku")
        print("2. Tambah buku")
        print("3. Hapus buku")
        print("4. Keluar")
        choice = input("Pilih menu (1/2/3/4): ")

        if choice == '1':
            tampilkan_data(data)
        elif choice == '2':
            inpu_data(data)
        elif choice == '3':
            hapus_data(data)
        elif choice == '4':
            print("Terima kasih! Sampai jumpa.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    menu()
