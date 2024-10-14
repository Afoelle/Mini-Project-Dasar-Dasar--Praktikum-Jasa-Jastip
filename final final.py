from prettytable import PrettyTable

akun = "rapi"
nim = 1
barang = [
    {"id barang": 1, "Nama barang": "Kaos Gucci", "Harga barang": 1500000, "Jumlah barang": 10},
    {"id barang": 2, "Nama barang": "Jaket Supreme", "Harga barang": 2500000, "Jumlah barang": 5},
    {"id barang": 3, "Nama barang": "Sepatu Nike Air Max", "Harga barang": 3000000, "Jumlah barang": 8},
    {"id barang": 4, "Nama barang": "Topi Adidas", "Harga barang": 500000, "Jumlah barang": 12},
    {"id barang": 5, "Nama barang": "Sweater Off-White", "Harga barang": 4500000, "Jumlah barang": 4},
    {"id barang": 6, "Nama barang": "Tas Louis Vuitton", "Harga barang": 10000000, "Jumlah barang": 3},
    {"id barang": 7, "Nama barang": "Kemeja Tommy Hilfiger", "Harga barang": 1200000, "Jumlah barang": 9},
    {"id barang": 8, "Nama barang": "Celana Levi's", "Harga barang": 800000, "Jumlah barang": 15},
    {"id barang": 9, "Nama barang": "Jas Calvin Klein", "Harga barang": 5000000, "Jumlah barang": 2},
    {"id barang": 10, "Nama barang": "Sweatpants Puma", "Harga barang": 600000, "Jumlah barang": 10}
]
belanjaan = []

def lihat():
    if not barang:
        print("Belum ada barang tersedia")
    else:
        print("============================ LIST BARANG ===========================")
        table = PrettyTable(["ID Barang", "Nama Barang", "Harga Barang", "Jumlah Barang"])
        for x in barang:
            table.add_row([x["id barang"], x["Nama barang"], x["Harga barang"], x["Jumlah barang"]])
        print(table)

def lihat_belanjaan():
    if not belanjaan:
        print("Belum ada barang tersedia")
    else:
        print("============================ LIST BARANG ===========================")
        table = PrettyTable(["ID Barang", "Nama Barang", "Harga Barang", "Jumlah Barang"])
        total_pembelian = 0
        for x in belanjaan:
            table.add_row([x["id barang"], x["Nama barang"], x["Harga barang"], x["Jumlah barang"]])
            total_pembelian += x["Harga barang"] * x["Jumlah barang"]  
        print(table)
        print(f"Total Pembelian: Rp {total_pembelian}")

def tambah(nama, harga, jumlah):
    id = len(barang) + 1
    barang.append({"id barang": id, "Nama barang": nama, "Harga barang": int(harga), "Jumlah barang": int(jumlah)})
    print("Barang berhasil ditambahkan")

def update(pilihan_update, id, nama, harga, jumlah):
    if pilihan_update == "1":
        for item in barang:
            if item["id barang"] == id:
                item["Nama barang"] = nama
                item["Harga barang"] = int(harga)
                item["Jumlah barang"] = int(jumlah)
                print(f"Barang dengan ID {id} berhasil diperbarui di daftar barang.")
                return
    elif pilihan_update == "2": 
        for item in belanjaan:
            if item["id barang"] == id:
                item["Nama barang"] = nama
                item["Harga barang"] = int(harga)
                item["Jumlah barang"] = int(jumlah)
                print(f"Barang dengan ID {id} berhasil diperbarui di daftar belanjaan.")
                return
    print("Barang tidak ditemukan.")

def hapus(id):
    for item in barang:
        if item["id barang"] == id:
            barang.remove(item)
            print(f"Barang dengan ID {id} berhasil dihapus.")
            print("")
            return
    print("ID barang tidak ditemukan")

def hapus_belanjaan(id):
    for item in belanjaan:
        if item["id barang"] == id:
            belanjaan.remove(item)  
            print(f"Barang dengan ID {id} berhasil dihapus dari belanjaan.")
            return
    print("ID barang tidak ditemukan di belanjaan.")

def beli(id):
    for item in barang:
        if item["id barang"] == id:
            if item["Jumlah barang"] > 0:
                item["Jumlah barang"] -= 1  
                for item_2 in belanjaan:
                    if item_2["id barang"] == id:
                        item_2["Jumlah barang"] += 1
                        print(f"Barang dengan ID {id} berhasil ditambahkan ke belanjaan.")
                        return
                belanjaan.append({
                    "id barang": item["id barang"],
                    "Nama barang": item["Nama barang"],
                    "Harga barang": item["Harga barang"],
                    "Jumlah barang": 1
                })
                print(f"Barang dengan ID {id} berhasil dibeli.")
            else:
                print("Stok barang tidak mencukupi.")
            return
    print("ID barang tidak ditemukan")

def login_user(akun_2):
    while True:
        print(f"\nSelamat datang {akun_2}")
        print("================== MENU =====================")
        menu = ["Selamat datang di jasa jastip Surabaya - Samarinda", "1. Beli barang", "2. Hapus Barang", "3. Lihat Pesanan", "4. Logout"]
        for i in menu:
            print(i)
        pilihan_2 = input("Silahkan Masukan Pilihan: ")
        print("=============================================")

        if pilihan_2 == "1": # beli
            print("")
            lihat()
            id = int(input("Masukan id barang yang ingin dibeli: "))
            beli(id)
            continue
        
        elif pilihan_2 == "2": # hapus
            print("")
            lihat_belanjaan()
            id = int(input("Masukan id yang ingin dihapus: "))
            hapus_belanjaan(id)
            continue
            
        elif pilihan_2 == "3": # lihat
            print("")
            lihat_belanjaan()
            continue

        elif pilihan_2 == "4": # logout
            menu_login()

def login_admin():
    print("Login admin berhasil\n")
    while True:
        print("=================MENU ADMIN==================")
        menu = ["1. Lihat barang", "2. Tambahkan barang", "3. Update barang yang dijual", "4. Hapus barang", "5. Logout"]
        for i in menu:
            print(i)
        print("==============================================")
        pilihan_3 = input("Masukan Pilihan: ")

        if pilihan_3 == "1": # lihat barang
            print("")
            print("1. Barang yang dijual \n2. Barang yang terjual")
            pilihan = input("Masukan Pilihan: ")
            print("")
            if pilihan == "1": 
                lihat()
                print("")
            elif pilihan == "2":
                lihat_belanjaan()
                print("")
            continue
        
        elif pilihan_3 == "2": # input barang
            nama = input("Masukan nama barang: ")
            harga = input("Masukan harga barang: ")
            jumlah = input("Masukan jumlah barang: ")
            tambah(nama, harga, jumlah)
            print("")
            continue
        
        elif pilihan_3 == "3": # update barang
            print("")
            print("1. Update barang jualan")
            print("2. Update barang yang terjual")
            pilihan_update = input("Masukan Pilihan: ")
            if pilihan_update == "1":
                print("")
                lihat()
                id = int(input("Masukan id barang yang ingin di update: "))
                nama = input("Masukan nama baru: ")
                harga = input("Masukan harga baru: ")
                jumlah = input("Masukan jumlah baru: ")
                update(pilihan_update, id, nama, harga, jumlah)
            elif pilihan_update == "2":
                print("")
                lihat_belanjaan()
                id = int(input("Masukan id barang yang ingin di update: "))
                nama = input("Masukan nama baru: ")
                harga = input("Masukan harga baru: ")
                jumlah = input("Masukan jumlah baru: ")
                update(pilihan_update, id, nama, harga, jumlah)
            continue

        elif pilihan_3 == "4": # hapus barang
            print("")
            lihat()
            id = int(input("Masukan id barang yang ingin dihapus: "))
            hapus(id)
            continue

        elif pilihan_3 == "5": # logout
            menu_login()

def menu_login():
    print("================== LOGIN =====================")
    Login = ["Selamat datang di program jastip", "1. Login", "2. Keluar"]
    for i in Login:
        print(i)
    print("==============================================")
    pilihan_1 = int(input("Masukan Pilihan: "))

    if pilihan_1 == 1:
        print("\nLogin Akun")
        akun_2 = input("Masukan Nama: ")
        nim_2 = int(input("Masukan Password (angka): "))
        if akun_2 != akun or nim_2 != nim:
            login_user(akun_2)
        else:
            login_admin()
    elif pilihan_1 == 2:
        print("Sampai jumpa lagi")
        exit()
    else:
        print("Angka yang anda masukan tidak valid, coba ulangi kembali")
        menu_login()

menu_login()
