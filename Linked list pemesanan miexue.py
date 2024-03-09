# Membuat kelas Node untuk menyimpan nama, menu, dan harga
class Node:
  def __init__(self, nama, harga):
    self.nama = nama
    self.harga = harga
    self.next = None

# Membuat kelas LinkedList untuk menyimpan dan mengelola pesanan
class LinkedList:
  def __init__(self):
    self.head = None # Menunjuk ke node pertama
    self.tail = None # Menunjuk ke node terakhir
    self.size = 0 # Menyimpan jumlah node

  # Menambahkan node baru ke akhir linked list
  def tambah_pesanan(self, nama, harga):
    new_node = Node(nama, harga) # Membuat node baru
    if self.head is None: # Jika linked list kosong 
      self.head = new_node # Membuat node baru sebagai head
      self.tail = new_node # Membuat node baru sebagai tail
    else: # Jika linked list tidak kosong
      self.tail.next = new_node # Menyambungkan node baru ke node terakhir
      self.tail = new_node # Membuat node baru sebagai tail
    self.size += 1 # Menambahkan ukuran linked list

  # Menampilkan semua node di linked list
  def tampilkan_pesanan(self):
    current = self.head # Menunjuk ke node pertama
    while current is not None: # Selama node tidak None
      print(current.nama, current.harga, "rupiah") # Mencetak nama dan harga node
      current = current.next # Berpindah ke node berikutnya
      