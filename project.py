
# Menampilkan Isi Toko
inventory = []

def tampilkan_inventory():
    print("\n================= DAFTAR INVENTORY ==================")
    if not inventory:
        print("\n[!] Inventory masih kosong.\n")
    else:
        for i, data_inventory in enumerate(inventory, 1):
            print(f"{i}. {data_inventory['nama']} | Stok: {data_inventory['Stok']} Kg | Harga: Rp{data_inventory['Harga']:,.0f}")
    print("=====================================================\n")

#Menu Tambah Barang
def tambah_barang():
    print("\n--- Tambah Barang Baru ---")
    nama_barang = input("Masukkan Nama Buah: ").strip().capitalize()

    # Logika Cek Duplikat untuk List of Dictionaries
    if any(item.get('nama') == nama_barang for item in inventory):
        print(f"[!] Buah '{nama_barang}' sudah ada. Silakan gunakan menu Update Stok.")
        return
        
    try:
        stok_barang = int(input("Masukkan Jumlah Stok (kg): "))
        harga_barang = float(input("Masukkan Harga Satuan (Rp): "))

        if stok_barang < 0 or harga_barang < 0:
            print("[!] Stok dan Harga tidak boleh negatif.")
            return

        data_baru = {
            'nama': nama_barang,
            'Stok': stok_barang, 
            'Harga': harga_barang
        }
        
        inventory.append(data_baru)
        print(f"\n[✓] Barang '{nama_barang}' berhasil ditambahkan ke inventory.")

    except ValueError:
        print("\n[!] Input tidak valid. Pastikan Stok dan Harga adalah angka.")


### MENU UPDATE STOK ###
def update_stok():
    """Update tok barang"""
    tampilkan_inventory()
    if not inventory:
        return
    
    pilihan = input("Pilih nomor barang: ").strip() 
    stok_baru = input("Masukkan stok baru: ").strip()

    if pilihan.isdigit() and stok_baru.isdigit():
        pilihan = int(pilihan)
        stok_baru = int(stok_baru)

        if 1 <= pilihan <= len(inventory):
            inventory[pilihan -1]["Stok"] = stok_baru
            nama_barang = inventory[pilihan -1]["nama"]
            print(f"Stok {nama_barang} berhasil diupdate menjadi {stok_baru} Kg")
        else:
            print("UPS, Nomor barang tidak valid")
    else:
        print("Input Harus Angka woiiiiiii")


### LOOPING - Menu utama ###
def main_menu():
    while True:
        print("="*40)
        print("SISTEM MANAJEMEN INVENTORY TOKO BUAH")
        print("="*40)
        print("1. Tampilkan Inventory")
        print("2. Tambah Barang")
        print("3. Update Stok")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == '1':
            tampilkan_inventory()
        elif pilihan == '2':
            tambah_barang()
        elif pilihan == '3':
            update_stok()
        elif pilihan == '4':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")

# Jalankan program
if __name__ == "__main__":
    main_menu()