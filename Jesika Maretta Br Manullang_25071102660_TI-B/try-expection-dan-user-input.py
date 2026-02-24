while True:
    try:
        print("=== Pendaftaran Black Bulls ===")
        
        nama = input("Masukkan nama Anda: ")
        mana = float(input("Masukkan jumlah mana Anda: "))
        level = int(input("Masukkan level kekuatan Anda: "))
        
        if mana < 0:
            print("Mana tidak boleh negatif!\n")
            continue
        
        if level <= 0:
            print("Level harus lebih dari 0!\n")
            continue
        
        skor = mana * level
        
        print("\n=== HASIL SELEKSI ===")
        print("Nama:", nama)
        print("Total Kekuatan:", skor)
        
        if skor >= 500:
            print("Selamat! Anda diterima di Black Bulls! ")
        else:
            print("Maaf, kekuatan Anda belum cukup untuk Black Bulls.")
        
        break
        
    except ValueError:
        print("Input tidak valid! Mana dan level harus berupa angka.\n")