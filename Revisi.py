jenis=input("Pilih Jenis Laporan [Kehilangan/Fasilitas Umum(FU)] :")
if jenis=="Kehilangan" or jenis=="kehilangan":
    nik=input("Masukan NIk Anda : ")
    nama=input("Masukkan Nama Anda : ")
    import datetime
    tanggal = datetime.datetime.now()
    alamat=input("Alamat : ")
    hilang=input("Laporan Kehilangan : ")


    print ("====================================================================")
    print ("NIK yang Anda Masukkan adalah : "+nik)
    print ("Nama yang Anda Masukkan adalah : "+nama)
    print("Tanggal Laporan :" , tanggal)
    # print ("Tanggal yang Anda Masukkan adalah : "+tanggal)
    print ("Alamat yang Anda Masukkan adalah : "+alamat)
    print ("Laporan yang Anda Masukkan adalah : "+hilang)
    print ("====================================================================")

    check=input("""Tulis "Benar" jika input benar Tulis "Salah" Jika sebaliknya :""")
    if check == "Benar" or check =="benar":
        print("Selesai")
    elif check == "Salah" or check == "salah":
        print()
    else:
        print("Coba Input Ulang")

elif jenis=="Fasilitas Umum" or jenis=="FU":
    nik=input("Masukan NIk Anda : ")
    nama=input("Masukkan Nama Anda : ")
    import datetime
    tanggal = datetime.datetime.now()
    alamat=input("Alamat : ")
    fu=input("Laporan Fasilitas Umum : ")


    print ("====================================================================")
    print ("NIK yang Anda Masukkan adalah : "+nik)
    print ("Nama yang Anda Masukkan adalah : "+nama)
    print("Tanggal Laporan :" , tanggal)
    # print ("Tanggal yang Anda Masukkan adalah : "+tanggal)
    print ("Alamat yang Anda Masukkan adalah : "+alamat)
    print ("Laporan yang Anda Masukkan adalah : "+fu)
    print ("====================================================================")
    
    check=input("""Tulis "Benar" jika input benar Tulis "Salah" Jika sebaliknya :""")
    if check == "Benar" or check =="benar":
        print("Selesai")
    elif check == "Salah" or check == "salah":
        print()
    else:
        print("Coba Input Ulang")
else:
    print("Tidak ada yang di pilih")
