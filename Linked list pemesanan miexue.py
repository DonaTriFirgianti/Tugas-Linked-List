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

# Menghitung total harga dari semua node di linked list
def hitung_total(self):
  total = 0 # Menyimpan total harga
  current = self.head # Selama node tidak None
    total += current.harga # Menambanhkan harga node ke total
    current = current.nest # Berpindah ke node berikutnya
  return total # Mengembalikan total harga

# Membuat objek Linked list
pesanan = Linkedlist()

# Membuat menu miexue
menu = {
  "Mixue Ice Cream": 5000,
  "Boba Shake": 16000,
  "Mi Sundae": 14000,
  "Mi Ganas": 11000,
  "Creamy Mango Boba": 22000
}

# Membuat fungsi untuk menampilkan menu
def tampilkan_menu():
  print("Menu Miexue:")
  for nama, harga in menu.items():
    print(nama, "->", harga, "rupiah")

# Membuat fungsi  untuk menerima input dari pengguna
def input_pesan():
  tampilkan_menu() # Menampilkan menu
  print("Silahkan masukkan nama menu yang ingin anda pesan")
  print("Ketik 'selesai' jika sudah selesai memesan")
  while True: # Mengulang sampai pengguna selesai
    nama = input("Pesan: ") # Menerima input nama menu
    if nama == "selesai": # Jika pengguna selesai
       break # Keluar dari Loop
    elif nama in menu: # Jika nama menu valid
       harga = menu[nama] # Mendapatkan harga menu
       pesanan.tambah_pesanan(nama, harga) # Menambahkan pesanan ke Linked List
    else: # Jika nama menu tidak valid
        print("Menu tidak tersedia, silahkan coba lagi") # Memberi pesan error

# Membua fungsi untuk menampilkandan membayar pesanan
def bayar_pesanan():
  print("Pesanan Anda adalah:")
  pesanan.tampilkan_pesanan() # Menampilkan pesanan
  total = pesanan.hitung_total() # Menghitung total harga
  print("Total biaya yang harus dibayarkan adalah", total, "rupiah") # Menampilkan total harga

# Memanggil fungsi input_pesan
input_pesan()

# Memanggil fungsi bayar_pesanan
bayar_pesanan()
