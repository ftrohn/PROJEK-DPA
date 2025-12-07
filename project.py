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

## menampilkan inventory ##

## sinpan inventory ke file ##

## update stok barang ##

## cari barang ##

## hapus barang ##

## tampilan menu ##