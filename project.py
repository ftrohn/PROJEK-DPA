## Storage ##
inventory = {}
isi_file = None

## membuat inventory baru dan file baru ##
def buat_inventory_baru():
    global isi_file
    inventory.clear()

    nama_file = input("Masukkan nama file baru (tanpa .txt) : ").strip()

    try:
        with open(f"{nama_file}.txt", "x") as file:
            pass
    except FileExistsError:
        print(f"[!] file '{nama_file}.txt' sudah ada. data tidak tersimpan\n")
        return

    while True:
        try:
            nama = input("Masukkan nama barang : ").strip().capitalize()
            stok = int(input("Masukkan stok barang : "))
            satuan = input("Masukkan satuan barang (buah, pcs, kg, dll) : ").strip().lower()

            if stok < 0:
                print("[!] stok tidak boleh negatif\n")
                continue

        except ValueError:
            print("[!] stok harus berupa angka\n")
            continue

        if nama in inventory:
            print(f"Barang '{nama}' sudah ada, silakan masukkan nama lain\n")
            continue
        else:
            inventory[nama] = (stok, satuan)
            print(f"Barang '{nama}' berhasil ditambahkan")

        lanjut = input("Tambah barang lagi? (y/n): ").strip().lower()
        print()
        if lanjut != "y":
            break

    if not inventory:
        print("Tidak ada data yang disimpan")
        return

    with open(f"{nama_file}.txt", "w") as file:
        for nama, (stok, satuan) in inventory.items():
            file.write(f"{nama},{stok},{satuan}\n")

    isi_file = nama_file
    print(f"Data berhasil disimpan di {nama_file}.txt")

## menambah inventory dari file ##
def isi_inventory_file():
    global isi_file
    inventory.clear()

    nama_file = input("Masukkan nama file (tanpa .txt) : ").strip()

    try:
        with open(f"{nama_file}.txt", "r") as file:
            for baris in file:

                nama, stok, satuan = baris.strip().split(",")
                
                if nama in inventory:
                    print(f"\n[!] Barang '{nama}' sudah ada dalam inventory barang yang lama akan diabaikan\n")
                    continue
                inventory[nama] = (int(stok), satuan)

            if not inventory:
                print(f"\n[!] File '{nama_file}.txt' kosong (gunakan opsi tambah barang)\n")
                return
            
            else:
                isi_file = nama_file
                print(f"\n[+] Inventory berhasil ditambahkan dari file '{nama_file}.txt'\n")
                return 
                except FileNotFoundError:
        print(f"\n[!] File '{nama_file}.txt' tidak ditemukan\n")
        return
## menampilkan inventory ##
def tampilkan_inventory():
    if not inventory:
        print("\n[!] Inventory kosong, gunakan opsi 1 atau 2\n")
    else:
        print("\n========== Inventory Saat Ini ==========")
        for nama, (stok, satuan) in inventory.items():
            print(f"- {nama} = {stok} {satuan}")
        print("========================================\n")

## sinpan inventory ke file ##
def simpan_ke_file():
    if not isi_file:
        print("[!] Tidak ada file aktif")
        return

    with open(f"{isi_file}.txt", "w") as file:
        for nama, (stok, satuan) in inventory.items():
            file.write(f"{nama},{stok},{satuan}\n")

## update stok barang ##
def update_stok():
    if not inventory:
        print("[!] Inventory masih kosong\n")
        return

    print("\n===== Update Stok Barang =====")
    nama = input("Masukkan nama barang : ").strip().capitalize()

    if nama in inventory:
        try:
            stok_baru = int(input("Masukkan stok baru : "))

            if stok_baru < 0:
                print("[!] Stok tidak boleh negatif\n")
                return

            inventory[nama] = (stok_baru, inventory[nama][1])
            simpan_ke_file()

            print(f"Stok '{nama}' berhasil diupdate menjadi {stok_baru} {inventory[nama][1]}\n")

        except ValueError:
            print("[!] Stok harus berupa angka\n")

    else:
        print(f"[!] Barang '{nama}' tidak ditemukan dalam inventory\n")
        
## cari barang ##
def cari_barang():
    if not inventory:
        print("[!] Inventory masih kosong\n")
        return
    
    nama = input("Masukkan nama barang yang dicari : ").strip().capitalize()
    
    if nama in inventory:
        stok, satuan = inventory[nama]
        print(f"- {nama} = {stok} {satuan}\n")

    else:
        print(f"[!] Barang '{nama}' tidak ditemukan dalam inventory\n")
        
## hapus barang ##
def hapus_barang():
    if not inventory:
        print("[!] Inventory masih kosong\n")
        return
    
    nama = input("Masukkan nama barang yang akan dihapus : ").strip().capitalize()
    
    if nama in inventory:
        del inventory[nama]
        simpan_ke_file()
        print(f"Barang '{nama}' berhasil dihapus dari inventory\n")
        return
    else:
        print(f"[!] Barang '{nama}' tidak ditemukan dalam inventory\n")
        return

## tambah barang ##
def tambah_barang():
    if not inventory:
        print("[!] Inventory masih kosong\n")
        return

    while True:
        try:
            nama = input("Masukkan nama barang : ").strip().capitalize()
            stok = int(input("Masukkan stok barang : "))
            satuan = input("Masukkan satuan barang (buah, pcs, kg, dll) : ").strip().lower()

            if stok < 0:
                print("[!] stok tidak boleh negatif\n")
                continue

        except ValueError:
            print("[!] stok harus berupa angka\n")
            continue

        if nama in inventory:
            print(f"Barang '{nama}' sudah ada, silakan masukkan nama lain\n")
            continue
        else:
            inventory[nama] = (stok, satuan)
            print(f"Barang '{nama}' berhasil ditambahkan")

        lanjut = input("Tambah barang lagi? (y/n): ").strip().lower()
        print()
        if lanjut != "y":
            break

    simpan_ke_file()
    print("[-] Data berhasil disimpan\n")

## tampilan menu ##
def menu():
    while True:
        print("======== Inventory Management ========")
        print("""1. Buat Inventory Baru
2. Ambil Inventory Dari File (txt)
3. tambah barang
4. Tampilkan Inventory saat ini
5. Update Stok Barang
6. Cari Barang
7. Hapus Barang
8. Keluar

note:
untuk ambil inventory dari file gunakan format :
Nama Barang, Stok, Satuan.
ex: pensil,20,pack.""")
        print("======================================\n")

        
        pilih = input("pilih menu : ").strip()
        
        if pilih == "1":
            buat_inventory_baru()
        elif pilih == "2" :
            isi_inventory_file()
        elif pilih == "3":
            tambah_barang()
        elif pilih == "4":
            tampilkan_inventory()
        elif pilih =="5" :
            update_stok()
        elif pilih == "6":
            cari_barang()
        elif pilih == "7":
            hapus_barang()
        elif pilih == "8":
            print("[-] keluar dari program\n")
            break
        else:
            print("[!] Tidak ada input / pilihan diluar nurul, LIHAT MENU YG TERSEDIA!!!!\n")

if __name__ == "__main__":
    menu()
