# Program simulasi mesin ATM

# Set PIN dan saldo awal
pin_terdaftar = "1234"
saldo = 1000000  # saldo awal (misalnya 1 juta)

# Autentikasi PIN
pin = input("Masukkan PIN Anda: ")
if pin != pin_terdaftar:
    print("PIN salah. Akses ditolak.")
else:
    while True:
        print("\n=== MENU ATM ===")
        print("1. Cek Saldo")
        print("2. Tarik Tunai")
        print("3. Setor Uang")
        print("4. Keluar")
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            print(f"Saldo Anda saat ini: Rp{saldo}")
        elif pilihan == "2":
            jumlah = int(input("Masukkan jumlah yang akan ditarik: "))
            if jumlah > saldo:
                print("Saldo tidak cukup.")
            else:
                saldo -= jumlah
                print(f"Penarikan berhasil. Sisa saldo: Rp{saldo}")
        elif pilihan == "3":
            jumlah = int(input("Masukkan jumlah yang akan disetor: "))
            saldo += jumlah
            print(f"Setoran berhasil. Saldo baru: Rp{saldo}")
        elif pilihan == "4":
            print("Terima kasih telah menggunakan ATM kami.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")