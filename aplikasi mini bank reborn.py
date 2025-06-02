def create_account(account_number, initial_balance):
  """Membuat akun bank baru."""
  accounts[account_number] = {
      "saldo": initial_balance,
      "riwayat_transaksi": []
  }
  print(f"Akun {account_number} berhasil dibuat dengan saldo awal {initial_balance}")

def deposit(account_number, amount):
  """Melakukan deposit ke akun."""
  if account_number in accounts:
      accounts[account_number]["saldo"] += amount
      accounts[account_number]["riwayat_transaksi"].append(f"Deposit: +{amount}")
      print(f"Deposit {amount} berhasil ke akun {account_number}")
  else:
      print(f"Akun {account_number} tidak ditemukan.")

def withdraw(account_number, amount):
  """Melakukan penarikan dari akun."""
  if account_number in accounts:
      if accounts[account_number]["saldo"] >= amount:
          accounts[account_number]["saldo"] -= amount
          accounts[account_number]["riwayat_transaksi"].append(f"Penarikan: -{amount}")
          print(f"Penarikan {amount} berhasil dari akun {account_number}")
      else:
          print("Saldo tidak cukup.")
  else:
      print(f"Akun {account_number} tidak ditemukan.")

def check_balance(account_number):
  """Melihat saldo akun."""
  if account_number in accounts:
      print(f"Saldo akun {account_number}: {accounts[account_number]['saldo']}")
  else:
      print(f"Akun {account_number} tidak ditemukan.")

def print_transaction_history(account_number):
  """Melihat riwayat transaksi akun."""
  if account_number in accounts:
      print(f"Riwayat transaksi akun {account_number}:")
      for transaksi in accounts[account_number]["riwayat_transaksi"]:
          print(transaksi)
  else:
      print(f"Akun {account_number} tidak ditemukan.")

# Inisialisasi
accounts = {}

# Main loop
while True:
  print("\nMini Bank - Pilih tindakan:")
  print("1. Buat akun")
  print("2. Deposit")
  print("3. Tarik")
  print("4. Lihat saldo")
  print("5. Lihat riwayat transaksi")
  print("6. Keluar")

  choice = input("Pilih tindakan (1-6): ")

  if choice == "1":
    account_number = input("Masukkan nomor rekening: ")
    initial_balance = float(input("Masukkan saldo awal: "))
    create_account(account_number, initial_balance)
  elif choice == "2":
    account_number = input("Masukkan nomor rekening: ")
    amount = float(input("Masukkan jumlah deposit: "))
    deposit(account_number, amount)
  elif choice == "3":
    account_number = input("Masukkan nomor rekening: ")
    amount = float(input("Masukkan jumlah penarikan: "))
    withdraw(account_number, amount)
  elif choice == "4":
    account_number = input("Masukkan nomor rekening: ")
    check_balance(account_number)
  elif choice == "5":
    account_number = input("Masukkan nomor rekening: ")
    print_transaction_history(account_number)
  elif choice == "6":
    print("Terima kasih!")
    break
  else:
    print("Pilihan tidak valid. Silakan coba lagi.")