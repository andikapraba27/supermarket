# Python Project: Self-service Supermarket

## Latar Belakang
Suatu perusahaan super market membuat rencana untuk memperbaiki proses bisnisnya. Rencana tersebut adalah dengan membuat kasir self-service. Kasir self-service dibutuhkan untuk menggaet customer yang berada di kota lainnya untuk dapat melakukan transaksi pada super market tersebut. Dampak dari proses bisnis ini adalah menambah jumlah transaksi, dan mendapatkan potensi profit yang lebih dari customer yang berbeda domisili. 
Problem yang dapat timbul dari project ini adalah jika customer tidak paham dengan alur dari system self-service ini. Maka dari itu, untuk mempermudah proses pemasukan transaksi, disusun sebuah algoritma yang mudah dipahami, dengan customer hanya memasukkan angka-angka syntax, yang mewakili fitur-fitur yang akan digunakan, contoh: 1. Menambah item, 2. Update item, 3. Menghapus item dan lain-lain. 

## Requirement/Objective
Super market ini membutuhkan suatu sistem kasir. Pada sistem ini customer dapat memasukkan nama barang, jumlah barang, dan harga barang secara mandiri. Fungsi-fungsi yang dibutuhkan antara lain:
- Membuat sebuah class untuk menghimpun seluruh metode yang diperlukan Transaction()
- Membuat suatu metode add_item untuk menambahkan nama item, jumlah item, dan harga item ke dalam transaksi
- Membuat fungsi update_item_name, apabila kustomer ingin mengganti nama item apabila ada kesalahan input dan lain-lain
- Membuat fungsi update_item_qty, apabila kustomer ingin mengganti jumlah item yang dibeli
- Membuat fungsi update_item_price, apabila kustomer ingin mengganti harga dari item
- Membuat fungsi delete_item untuk menghapus 1 item yang tidak diinginkan
- Membuat fungsi reset_transaction untuk menghapus seluruh transaksi yang telah dilakukan
- Membuat fungsi check_order untuk melihat ringkasan dari transaksi yang telah dimasukkan
- Membuat fungsi total_price untuk menghitung berapa harga total yang harus dibayarkan, beserta diskon yang didapatkan.
  - apabila total harga > 500,000, maka mendapatkan diskon 10%
  - apabila total_harga antara 300,000 dan 500,000, maka mendapatkan diskon 8%
  - apabila total_harga antara 200,000 dan 300,000, maka mendapatkan diskon 5%
  - apabila total_harga di bawah 200,000, maka tidak mendapatkan diskon.

Fungsi check_order menggunakan module yang harus ditambahkan pada awal pembentukan file.py, yaitu:
- tabulate \
  modul ini digunakan untuk menampilkan seluruh transaksi berupa tabel

## Alur Program/Flowchart
Berikut merupakan alur program/flowchart dari program:
1.	Pertama, akan meminta user untuk memilih apakah akan melakukan transaksi.
2.	Apabila user akan bertransaksi pilih Yes (y), jika tidak pilih No (n).
3.	Jika pilih n, maka program akan mengeluarkan pesan “terima kasih sudah berbelanja”
4.	Jika pilih y, maka program akan masuk ke main program dengan beberapa pilihan syntax sebagai berikut:


No  | Fungsi
--- | ------------------
1   | Input/tambah Item
2   | Update Item
3   | Hapus Item
4   | Hapus semua Item
5   | Cek Order
6   | Total Bayar
7   | Keluar


5.	Program main tersebut akan dimasukkan ke dalam suatu while, sehingga Langkah-langkah tersebut dapat dipilih hingga user selesai input keseluruhan data.
6.	Pada input item, akan diperiksa secara langsung apakah inputan yang dimasukan oleh user sudah sesuai dengan tipe data nama barang, jumlah, dan harga. Apabila tidak sesuai maka pesan input error akan keluar. Item tersebut akan dimasukkan ke dalam sebuah dictionary dengan format: dict = { nama_barang: [jumlah, harga] }
7.	Pada update item, akan memerlukan user untuk memasukkan nama barang yang ingin di update, lalu bisa memilih apakah ingin mengupdate item, jumlah, atau harga item. Apabila input dari user tidak sesuai, maka pesan error akan ditampilkan.


Pilih  | Fungsi
------ | ------------------
a      | Update nama item
b      | Update jumlah item
c      | Update harga item


8.	Hapus item, akan memerlukan inputan nama barang yang ingin dihapus. Apabila nama barang tidak ditemukan, maka pesan error akan ditampilkan.
9.	Hapus semua item akan menghapus seluruh item pada dictionary.
10.	Pada cek order, pada requirement dari proyek yang diberikan, ada ketentuan mengenai apakah input yang dimasukkan sudah sesuai apa tidak, namun, karena error tersebut telah dimasukkan pada fungsi lainnya, seperti input item dan update item. Untuk mengeluarkan table diperlukan libraries tabulate, untuk memberikan tampilan yang user friendly. Apabila user ingin melihat order, namun belum memasukkan order satupun, maka program akan mengeluarkan pesan error. 
11.	Pada check out dan bayar, user dapat melihat ringkasan pesanannya, dan rincian total harga yang harus dibayar serta diskon yang diperoleh. Apabila user melakukan check out tanpa input satupun, maka pesan data belanja kosong akan ditampilkan.
12.	Untuk Langkah pada nomor 7 (Keluar) merupakan perintah untuk keluar atau batal untuk melakukan transaksi sehingga program akan selesai berjalan. Kustomer akan ditanya kembali apakah ingin keluar dari program dengan mengetik y atau n, ketik y jika ingin keluar, apabila kustomer menginput n dan kata-kata lain, program masih berjalan. 


## Penjelasan Code
Pada project ini, terdapat 2 file yang dibuat, yaitu transaction.py dan main.py. transaction.py merupakan file python yang berisi modul class Transaction yang berisi syntax-syntax yang digunakan dalam memproses transaksi kustomer. Sedangkan file main.py berisi syntax-syntax yang berkaitan dengan menu transaksi yang bisa dilakukan oleh kustomer, dengan memanfaatkan perintah-perintah yang ada pada modul transaction.py . Pertama, akan dijelaskan mengenai file transaction.py

### transaction.py
- Awal /
![gambar](https://user-images.githubusercontent.com/31236670/231508538-0cf681ca-5f69-40c4-81f2-c94045941e3b.png)
Import modul tabulate yang akan digunakan menampilkan ringkasan transaksi yang ada pada fungsi check_order. Class diberi nama Transaction. Inisialisasi variabel yang digunakan pada class Transaction, yang terdiri dari dict_barang, dictionary untuk menampung nama barang, jumlah dan item, dengan format, {nama_barang: [jumlah, harga]}. Variabel total_harga untuk menyimpan total harga yang dibayar, serta variabel diskon untuk menyimpan diskon yang diberikan berdasarkan kriteria pada requirement.

- add_item /
![gambar](https://user-images.githubusercontent.com/31236670/231505322-caffbbcd-3c69-4e32-a052-20833657f0ac.png)
fungsi add_item digunakan untuk menambahkan item ke dalam kelas Transaction. Pertama, fungsi akan meminta input nama_barang, jumlah, dan harga. Lalu fungsi akan masuk ke bagian try-except. Pada bagian try akan dijalankan pemeriksaan sebagai berikut:
  * apakah inputan jumlah dan harga berupa numerik, apabila iya, maka data dimasukkan ke dalam dict_barang
  * apakah inputan jumlah & harga < 1, apabila iya, maka pesan input ulang akan ditampilkan, dan data tidak dimasukkan
  * apabila inputan jumlah & harga tidak bertipe numerik, maka akan menampilkan raise Exception.
  
 Pada bagian except, akan dicek 2 hal, yaitu apabila ValueError ketika inputan harga/jumlah bukan numerik, dan Exception lainnya yang berasal dari raise. 





