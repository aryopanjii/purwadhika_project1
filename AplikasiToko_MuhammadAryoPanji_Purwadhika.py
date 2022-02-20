listbarang = [
    {
        'nama': 'iphone11',
        'stock': 20,
        'harga': 10000
    },
    {
        'nama': 'ipad4',
        'stock': 15,
        'harga': 15000
    },
    {
        'nama': 'macbookpro',
        'stock': 25,
        'harga': 20000
    }
]

cart = []

def menampilkanDaftarBarang() :
    print('Daftar Barang\n')
    print('Index\t| Nama  \t| Stock\t| Harga')
    for i in range(len(listbarang)) :
        print('{}\t| {}  \t| {}\t| {}'.format(i,listbarang[i]['nama'],listbarang[i]['stock'],listbarang[i]['harga']))

def menambahBarang() :
    namaBarang = input('Masukkan Nama Barang : ')
    stockBarang = int(input('Masukkan Stock Barang : '))
    hargaBarang = int(input('Masukkan Harga Barang : '))
    listbarang.append({
        'nama': namaBarang,
        'stock': stockBarang,
        'harga': hargaBarang
    })
    menampilkanDaftarBarang()

def menghapusBarang() :
    menampilkanDaftarBarang()
    indexBarang = int(input('Masukkan index barang yang ingin dihapus : '))
    del listbarang[indexBarang]
    menampilkanDaftarBarang()

def membeliBarang() :
    menampilkanDaftarBarang()
    while True :
        indexBarang = int(input('Masukkan index barang yang ingin dibeli : '))
        qtyBarang = int(input('Masukkan jumlah yang ingin dibeli : '))
        if(qtyBarang > listbarang[indexBarang]['stock']) :
            print('Stock tidak cukup, stock {} tinggal {}'.format(listbarang[indexBarang]['nama'],listbarang[indexBarang]['stock']))
        else :
            cart.append({
                'nama': listbarang[indexBarang]['nama'], 
                'qty': qtyBarang, 
                'harga': listbarang[indexBarang]['harga'], 
                'index': indexBarang
            })
        print('Isi Cart :')
        print('Nama\t| Qty\t| Harga')
        for item in cart :
            print('{}\t| {}\t| {}'.format(item['nama'], item['qty'], item['harga']))
        checker = input('Mau beli yang lain? (ya/tidak) = ')
        if(checker == 'tidak') :
            break

    print('Daftar Belanja :')
    print('Nama\t| Qty\t| Harga\t| Total Harga')
    totalHarga = 0
    for item in cart :
        print('{}\t| {}\t| {}\t| {}'.format(item['nama'], item['qty'], item['harga'], item['qty'] * item['harga']))
        totalHarga += item['qty'] * item['harga']    
    while True :
        print('Total Yang Harus Dibayar = {}'.format(totalHarga))
        jmlUang = int(input('Masukkan jumlah uang : '))
        if(jmlUang > totalHarga) :
            kembali = jmlUang - totalHarga
            print('Terima kasih \n\nUang kembali anda : {}'.format(kembali))
            for item in cart :
                listbarang[item['index']]['stock'] -= item['qty']
            cart.clear()
            break
        elif(jmlUang == totalHarga) :
            print('Terima kasih')
            for item in cart :
                listbarang[item['index']]['stock'] -= item['qty']
            cart.clear()
            break
        else :
            kekurangan = totalHarga - jmlUang
            print('Uang anda kurang sebesar {}'.format(kekurangan))

while True :
    pilihanMenu = input('''
        Selamat Datang di Penjualan Barang di Toko Bahagia

        List Menu :
        1. Menampilkan Daftar Barang
        2. Menambah Barang
        3. Menghapus Barang
        4. Membeli Barang
        5. Exit Program

        Masukkan angka Menu yang ingin dijalankan : ''')

    if(pilihanMenu == '1') :
        menampilkanDaftarBarang()
    elif(pilihanMenu == '2') :
        menambahBarang()
    elif(pilihanMenu == '3') :
        menghapusBarang()
    elif(pilihanMenu == '4') :
        membeliBarang()
    elif(pilihanMenu == '5') :
        break
    
