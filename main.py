#import modul yang akan digunakan
from transaction import Transaction

#Membuat menu utama dalam transaksi
print("---- Welcome Super Market Jaya ----\n")
start_program = input("Apakah anda ingin melakukan transaksi? (y/n) :").lower()

if start_program == "y":
    
    #inisialisasi boolean end_program untuk menjalankan while
    end_program = False
    
    #inisialisasi class
    trans = Transaction()
    
    #menjalankan program while untuk menayangkan menu secara berulang
    #hingga program berakhir
    while end_program == False:
        
        #print list transaksi yang dapat dilakukan
        print("\n---- Welcome Super Market Jaya ---- \n")
        print("list transaksi")
        print("--------------")
        print("1. Tambahkan Item")
        print("2. Update Item")
        print("3. Hapus Item")
        print("4. Hapus Semua Item")
        print("5. Cek Order")
        print("6. Total Bayar")
        print("7. Keluar \n")
        
        #input perintah yang ingin dijalankan
        perintah = input("Masukkan angka dari transaksi yang ingin dilakukan: \n")
        
        #case 1: penambahan item
        if perintah == "1":
            trans.add_item()
        
        #case 2: update nama item, jumlah item, harga item
        elif perintah == "2" and len(trans.dict_barang) > 0:
            #memilih apa yang ingin diupdate
            print("Pilih apa yang ingin anda update:")
            print("a. Nama Item")
            print("b. Jumlah Item")
            print("c. Harga Item \n")
            
            #input perintah update
            perintah_update = input("Masukkan pilihan (a/b/c) : ").lower()
            
            #menjalankan fungsi if untuk menjalankan perintah update yang diminta
            if perintah_update == "a":
                trans.update_item_name()
            elif perintah_update == "b":
                trans.update_item_qty()
            elif perintah_update == "c":
                trans.update_item_price()
            else:
                print("Mohon masukkan hanya a, b, dan c")
        
        #case 3: menghapus item
        elif perintah == "3" and len(trans.dict_barang) > 0:
            trans.delete_item()
        
        #case 4: menghapus seluruh item
        elif perintah == "4" and len(trans.dict_barang) > 0:
            trans.reset_transaction()
        
        #case 5: cek order yang telah dimasukan
        elif perintah == "5":
            trans.check_order()
        
        #case 6: cek total harga beserta diskon yang didapatkan
        elif perintah == "6":
            trans.total_price()
        
        #case 7: mengakhiri sesi transaksi
        elif perintah == "7":
            
            keluar = input("Apakah anda ingin mengakhiri sesi? (y/n) ").lower()
            
            if keluar == "y": #jika keluar maka memanggil fungsi total price
                trans.total_price()
                print("Terima kasih atas kunjungan anda")
                end_program = True
                
            else: #selain input y, maka akan langsung keluar dari program
                end_program = False
        
        #jika user meminta untuk update item, & hapus item tapi belum input 
        #satu item pun sama sekali, maka perintah berikut yang dijalankan
        elif perintah in ['2','3','4'] and len(trans.dict_barang) == 0:
            print("Belum ada barang yang di input")
        
        #apabila input tidak sesuai dengan angka pada menu
        else:
            print("Mohon input sesuai dengan nomor perintah")
        
        #print("\n")
        
        
elif start_program == "n": #apabila input huruf n 
    print("Anda tidak melakukan transaksi")
else : #apabila input selain y dan n
    print("Mohon input hanya menggunakan y dan n")