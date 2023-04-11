""" Module ini berisi perintah-perintah
    yang digunakan dalam proses transaksi
    Supermarket Jaya
    
Modul ini akan ditambahkan pada program
main.py menggunakan fungsi import module
cara pemanggilan:

    from transaction.py import Transaction
"""

from tabulate import tabulate

class Transaction:
    
    def __init__(self,):
        self.dict_barang = dict()
        self.total_harga = 0
        self.diskon = 0
        
        
    def add_item(self):
        """Fungsi untuk menambahkan item ke dalam kelas Transaction
            yang akan disimpan pada dictionary
        """
        
        #syntax input nama item, jumlah, dan harga per item
        nama_barang = input("Masukkan nama barang: ").lower()
        jumlah = input("Masukkan jumlah yang dibeli: ").lower()
        harga = input("Masukkan harga barang satuan: ").lower()
        
        try:
            #untuk memeriksa apakah input jumlah dan harga menggunakan tipe numerik
            if jumlah.isnumeric() == True and harga.isnumeric() == True:
                input_dict_barang = {nama_barang: [int(jumlah), int(harga)]}
                self.dict_barang.update(input_dict_barang)
                print(f"Barang {nama_barang} berhasil ditambahkan dengan jumlah: {jumlah}, dan harga: {harga}")
                
            elif int(jumlah) < 1 and int(harga) < 1: #untuk memeriksa apakah input jumlah & harga < 1
                print("Input jumlah dan harga < 1, input ulang")
                
            else:
                raise Exception(f"Barang {nama_barang} tidak berhasil ditambahkan, cek kembali inputan anda, jumlah: {jumlah} & harga: {harga}")
            
        except ValueError:
            print("Input harga bukan tipe data angka/integer")
            
        except Exception as e:
            print(e)
        
        
    def update_item_name(self):
        """Fungsi untuk mengupdate nama item
        """
        
        #input nama barang yang ingin diupdate dan nama barunya
        nama_lama = input("Masukkan nama barang yang ingin diupdate: ").lower()
        nama_baru = input("Masukkan nama baru: ").lower()
        
        try:
            #cek apakah nama barang yang di input ada pada dictionary
            if nama_lama in self.dict_barang.keys():
                self.dict_barang[nama_baru] = self.dict_barang[nama_lama]
                self.dict_barang.pop(nama_lama)
                
            else:
                raise Exception(f"Nama barang tidak ditemukan, input ulang nama yang ingin diganti")
                
        except Exception as e:
            print(e)
        
        
    def update_item_qty(self):
        """Fungsi untuk mengupdate jumlah item
        """
        
        #input nama barang yang ingin diganti jumlahnya beserta jumlah terbaru
        nama_barang = input("Masukkan nama barang yang ingin diupdate jumlahnya: ").lower()
        qty_baru = input("Masukkan jumlah terbaru: ").lower()
        
        try:
            #cek apakah nama barang yang di input ada pada dictionary
            if nama_barang in self.dict_barang.keys():
                
                if int(qty_baru) > 0: #cek apakah inputan jumlah > 0
                    self.dict_barang[nama_barang] = [int(qty_baru), self.dict_barang[nama_barang][1]]
                    
                else:
                    print("jumlah yang anda masukkan < 1, input ulang")
                    
            else:
                raise Exception(f"Nama barang tidak ditemukan, mohon input ulang")
            
        except ValueError:
            print("Input Jumlah bukan tipe data angka/integer")
        
        except Exception as e:
            print(e)
            
        
    def update_item_price(self):
        """Fungsi untuk mengupdate harga item
        """
        
        #input nama barang yang ingin diganti harganya beserta harga terbaru
        nama_barang = input("Masukkan nama barang yang ingin diupdate harganya: ").lower()
        price_baru = input("Masukkan harga terbaru: ").lower()
        
        try:
            #cek apakah nama barang yang di input ada pada dictionary
            if nama_barang in self.dict_barang.keys():
                
                if int(price_baru) > 0: #cek apakah inputan harga > 0
                    self.dict_barang[nama_barang] = [self.dict_barang[nama_barang][0],int(price_baru)]
                    
                else:
                    print("harga yang anda masukkan < 1, input ulang")
                    
            else:
                raise Exception(f"Nama barang tidak ditemukan, mohon input ulang")
        
        except ValueError:
            print("Input harga bukan tipe data angka/integer")
        
        except Exception as e:
            print(e)
            
        
    def delete_item(self):
        """Fungsi untuk menghapus item
        """
        
        #input nama barang yang ingin dihapus seluruh datanya
        nama_barang = input("Masukkan nama barang yang ingin dihapus: ").lower()
        
        try:
            #cek apakah nama barang yang di input ada pada dictionary
            if nama_barang in self.dict_barang.keys():
                self.dict_barang.pop(nama_barang)
                
            else:
                raise Exception(f"Nama barang tidak ditemukan, mohon input ulang")
                
        except Exception as e:
            print(e)
        
    
    def reset_transaction(self):
        """Fungsi untuk menghapus seluruh item
        """
        
        #mengubah data dict_barang menjadi dictionary kosong
        self.dict_barang = dict()
        print("Seluruh transaksi dihapus")
    
    
    def check_order(self):
        """Fungsi untuk menampilkan seluruh item
            yang ditampilkan berupa tabel menggunakan
            libraries tabulate
        """
        
        try:
            #cek apakah dictionary kosong atau tidak
            if len(self.dict_barang) > 0:
                
                #inisialisasi header tabel
                headers = ["No", "Nama Item", "Jumlah Item", "Harga/Item", "Total Harga"]
                
                #inisialisasi tabel kosong
                table = []
                
                #inisialisasi penomoran tabel
                i = 1
                
                #memasukkan nilai-nilai pada dictionary pada tabel
                #dan menambahkan penomoran serta nilai total harga per item
                for key in self.dict_barang.keys():
                    insert_row = [i, key, self.dict_barang[key][0], self.dict_barang[key][1], self.dict_barang[key][0]*self.dict_barang[key][1]]
                    i += 1
                    table.append(insert_row)
                
                #mencetak tabel menggunakan tabulate
                print(tabulate(table, headers=headers))
                
            else: #output jika dictionary kosong
                raise Exception("Data belanja kosong")
                
        except Exception as e:
            print(e)
    
    def total_price(self):
        """Fungsi untuk menghitung total harga dari seluruh
            barang yang masuk ke transaksi
        """
        
        try:
            #cek apakah dictionary kosong
            if len(self.dict_barang) > 0:
                
                #menampilkan ringkasan order
                self.check_order()
                
                #inisialisasi nilai total harga
                self.total_harga = 0
                
                #menghitung keseluruhan total harga
                for key, item in self.dict_barang.items():
                    self.total_harga += item[0] * item[1]
                
                #menentukan diskon yang didapat
                if self.total_harga > 500_000:
                    self.diskon = 10
                elif self.total_harga > 300_000:
                    self.diskon = 8
                elif self.total_harga > 200_000:
                    self.diskon = 5
                else:
                    self.diskon = 0
                
                print("\n")
                print(f"Total harga: {self.total_harga}")
                print(f"Diskon     : {self.diskon}%")
                print(f"Total bayar: {int(self.total_harga*(1-self.diskon/100))}")
                print("Silahkan transfer ke bank ABC no Rek: 123456")
                
            else:
                raise Exception("Data belanja kosong")
        except Exception as e:
            print(e)
        
        