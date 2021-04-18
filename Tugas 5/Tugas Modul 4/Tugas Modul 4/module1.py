class barang:
    #init method
  def __init__(self, urutan, nama_barang, merk, harga_pasar ):
    self.urutan = urutan
    self.nama_barang = nama_barang
    self.merk = merk
    self.harga_pasar = harga_pasar
    print (f"Ini adalah barang ke-{urutan}")
    print (f"Barang      : {nama_barang}")
    print (f"Merk        : {merk}")
    print (f"Harga Pasar : {harga_pasar}")

