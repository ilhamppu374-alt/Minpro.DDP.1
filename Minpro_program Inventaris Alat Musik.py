#Nama: Muhammad Ilham Zaini
#NIM: 2509116091
#Kelas: C
#Tema: Sistem Inventaris Alat Musik

inventaris_alat = ["Gitar"
]        

while True:
    print("=== Sistem Inventaris Alat Musik ===")
    print("1. Tambah Alat Musik")
    print("2. Lihat Daftar Alat Musik")
    print("3. Hapus Menu")
    print("4. Keluar")
    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        alat_baru = input("masukkan nama alat musik yang ingin ditambah: ")
        if alat_baru in inventaris_alat:
            print(f"Alat musik {alat_baru} sudah ada di menu")
        else:
            inventaris_alat.append(alat_baru)
            print(f"Alat musik {alat_baru} telah ditambahkan.")

    elif pilihan == "2":
        if inventaris_alat:
            print("Daftar Alat Musik:")
            for alat in inventaris_alat:
                print(alat)
        else:
            (inventaris_alat) == 0
            print("Data inventaris alat musik kosong")            


    elif pilihan == "3":
        hapus_alat=(input("Alat Musik yang ingin di hapus: "))
        if hapus_alat in inventaris_alat:
            inventaris_alat.remove(hapus_alat)
            print(f"alat musik {hapus_alat} telah dihapus dari menu")
        else:
            print(f"tidak ada {hapus_alat} di dalam menu")     


    elif pilihan == "4":
        print("Terima Kasih Telah Menggunakan Program Ini!")
        break
    else:
        print("Pilihan tidak valid. Coba lagi.")                            


