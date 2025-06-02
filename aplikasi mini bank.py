def utama():
    bank = {}
    menu = """
Aplikasi Mini Bank
=====================
1. Buat Akun
2. Cek Saldo
3. Setor
4. Tarik
5. Rincian Akun
6. Keluar
"""

    while True:
        print(menu)
        pilihan = input("Pilih opsi (1-6): ")

        if pilihan == "1":
            buat_akun(bank)
            nama_akun = input("Masukkan nama akun: ").strip().lower()

        elif pilihan == "2":
            cek_saldo(bank)
            nama_akun = input("Masukkan nama akun: ").strip().lower()

        elif pilihan == "3":
            setor(bank)
            nama_akun = input("Masukkan nama akun: ").strip().lower()

        elif pilihan == "4":
            tarik(bank)
            nama_akun = input("Masukkan nama akun: ").strip().lower()

        elif pilihan == "5":
            rincian_akun(bank)
            nama_akun = input("Masukkan nama akun: ").strip().lower()

        elif pilihan == "6":
            print("Terima kasih telah menggunakan Aplikasi Mini Bank. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1 hingga 6.\n")

def buat_akun(bank):
    print("\nBuat Akun")
    nama_akun = input("Masukkan nama akun: ").strip() .lower()
    if nama_akun in bank:
        print("Akun sudah terdaftar.\n")
        return
    try:
        setoran_awal = float(input("Masukkan setoran awal: "))
        if setoran_awal < 0:
         print("Setoran awal tidak boleh negatif.\n")           
        return
    except ValueError:
        print("Jumlah tidak valid.\n")
        return

    bank[nama_akun] = {
        "saldo": setoran_awal
    }
    print(f"Akun '{nama_akun}' berhasil dibuat dengan saldo {setoran_awal:.2f}.\n")

def cek_saldo(bank):
    print("\nCek Saldo")
    nama_akun = input("Masukkan nama akun: ").strip()
    akun = bank.get(nama_akun)
    if akun:
        print(f"Saldo akun '{nama_akun}': Rp {akun['saldo']:.2f}\n")
    else:
        print("Akun tidak ditemukan.\n")

def setor(bank):
    print("\nSetor")
    nama_akun = input("Masukkan nama akun: ").strip()
    akun = bank.get(nama_akun)
    if akun:
        try:
            jumlah = float(input("Masukkan jumlah setoran: "))
            if jumlah <= 0:
                print("Jumlah setoran harus lebih dari 0.\n")
                return
        except ValueError:
            print("Jumlah tidak valid.\n")
            return
        akun['saldo'] += jumlah
        print(f"Setoran sebesar Rp {jumlah:.2f} berhasil. Saldo baru: Rp {akun['saldo']:.2f}\n")
    else:
        print("Akun tidak ditemukan.\n")

def tarik(bank):
    print("\nTarik")
    nama_akun = input("Masukkan nama akun: ").strip()
    akun = bank.get(nama_akun)
    if akun:
        try:
            jumlah = float(input("Masukkan jumlah penarikan: "))
            if jumlah <= 0:
                print("Jumlah penarikan harus lebih dari 0.\n")
                return
        except ValueError:
            print("Jumlah tidak valid.\n")
            return
        if jumlah > akun['saldo']:
            print("Saldo tidak mencukupi.\n")
            return
        akun['saldo'] -= jumlah
        print(f"Penarikan sebesar Rp {jumlah:.2f} berhasil. Saldo baru: Rp {akun['saldo']:.2f}\n")
    else:
        print("Akun tidak ditemukan.\n")

def rincian_akun(bank):
    print("\nRincian Akun")
    nama_akun = input("Masukkan nama akun: ").strip()
    akun = bank.get(nama_akun)
    if akun:
        print(f"Nama Akun: {nama_akun}")
        print(f"Saldo: Rp {akun['saldo']:.2f}\n")
    else:
        print("Akun tidak ditemukan.\n")

if __name__ == "__main__":

    utama()
