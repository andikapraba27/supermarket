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
- Awal <br />
![gambar](https://user-images.githubusercontent.com/31236670/231508538-0cf681ca-5f69-40c4-81f2-c94045941e3b.png)  
Import modul tabulate yang akan digunakan menampilkan ringkasan transaksi yang ada pada fungsi check_order. Class diberi nama Transaction. Inisialisasi variabel yang digunakan pada class Transaction, yang terdiri dari dict_barang, dictionary untuk menampung nama barang, jumlah dan item, dengan format, {nama_barang: [jumlah, harga]}. Variabel total_harga untuk menyimpan total harga yang dibayar, serta variabel diskon untuk menyimpan diskon yang diberikan berdasarkan kriteria pada requirement.

- add_item <br />
![gambar](https://user-images.githubusercontent.com/31236670/231505322-caffbbcd-3c69-4e32-a052-20833657f0ac.png)  
fungsi add_item digunakan untuk menambahkan item ke dalam kelas Transaction. Pertama, fungsi akan meminta input nama_barang, jumlah, dan harga. Lalu fungsi akan masuk ke bagian try-except. Pada bagian try akan dijalankan pemeriksaan sebagai berikut:
  * apakah inputan jumlah dan harga berupa numerik, apabila iya, maka data dimasukkan ke dalam dict_barang
  * apakah inputan jumlah & harga < 1, apabila iya, maka pesan input ulang akan ditampilkan, dan data tidak dimasukkan
  * apabila inputan jumlah & harga tidak bertipe numerik, maka akan menampilkan raise Exception.
  
 Pada bagian except, akan dicek 2 hal, yaitu apabila ValueError ketika inputan harga/jumlah bukan numerik, dan Exception lainnya yang berasal dari raise. 

- update_item_name <br />
![gambar](https://user-images.githubusercontent.com/31236670/231784276-04486f5f-a897-4801-a575-fdd95b14171f.png)
Pada fungsi update_item_name, pertama kali dilakukan perintah input untuk memasukkan nama barang yang ingin diganti, dan nama baru dari barang tersebut. Lalu dilanjutkan pada proses try-except. Pada bagian try, akan dicek apakah nama lama (nama barang yang ingin diganti) ada pada dictionary dict_barang, yang merupakan kumpulan dari transaksi yang telah diinput sebelumnya. Apabila nama barang ada, maka dimasukkan input dictionary baru menggunakan key dengan nama baru, dengan values yaitu jumlah dan harga sama dengan values dari key pada nama lama. Lalu dict dengan nama lama dihapus menggunakan syntax pop(). Pada bagian else, ketika nama barang tidak ada pada dictionary, maka raise akan mencetak pesan input ulang nama lama, yang nantinya akan diprint pada bagian except. 

- update_item_qty <br />
![gambar](https://user-images.githubusercontent.com/31236670/231785746-0c91b3bb-9199-444c-b314-8daae4afc471.png)
Pada fungsi update_item_qty, pertama kali dilakukan perintah input untuk memasukkan nama barang yang ingin diganti jumlahnya, dan jumlah baru dari barang tersebut. Lalu dilanjutkan pada proses try-except. Pada bagian try, akan dicek apakah nama barang ada pada dictionary dict_barang. Apabila nama barang ada, maka values qty/jumlah yang ada pada bagian values dictionary diganti dengan qty_baru, dengan cara mengganti nilai pada list pada index ke-0, sedangkan harga masih memakai nilai lama dari dict_barang sebelumnya dengan memanggil self.dict_barang[nama_barang][1]. Lalu dilakukan pemeriksaan pada else, yaitu apabila qty_baru yang diinput nilainya < 1, sehingga kustomer harus input ulang. Pada bagian else selanjutnya, ketika nama barang tidak ada pada dictionary, maka raise akan mencetak pesan input ulang nama lama, yang nantinya akan diprint pada bagian except. Except lainnya yaitu ValueError di print ketika inputan pada qty_baru tidak bertipe numerik. 

- update_item_price <br />
![gambar](https://user-images.githubusercontent.com/31236670/231787171-9570ac2f-18f5-4d0a-9d91-1711eeb4e242.png)
Pada fungsi update_item_price, pertama kali dilakukan perintah input untuk memasukkan nama barang yang ingin diganti harganya, dan harga baru dari barang tersebut. Lalu dilanjutkan pada proses try-except. Pada bagian try, akan dicek apakah nama barang ada pada dictionary dict_barang. Apabila nama barang ada, maka values harga yang ada pada bagian values dictionary diganti dengan price_baru, dengan cara mengganti nilai pada list pada index ke-1, sedangkan qty/jumlah masih memakai nilai lama dari dict_barang sebelumnya dengan memanggil self.dict_barang[nama_barang][0]. Lalu dilakukan pemeriksaan pada else, yaitu apabila price_baru yang diinput nilainya < 1, sehingga kustomer harus input ulang. Pada bagian else selanjutnya, ketika nama barang tidak ada pada dictionary, maka raise akan mencetak pesan input ulang nama lama, yang nantinya akan diprint pada bagian except. Except lainnya yaitu ValueError di print ketika inputan pada qty_baru tidak bertipe numerik. 

- delete_item <br />
![gambar](https://user-images.githubusercontent.com/31236670/231787833-dcc773c2-5407-41f2-ac59-f42dcff0c153.png)
Pada fungsi delete_item, dilakukan input nama barang yang ingin dihapus. Lalu pada bagian try, dicek apakah nama barang ada pada dict_barang. Apabila ada, maka barang tersebut dihapus menggunakan fungsi pop() yang terikat pada tipe data dictionary. Jika nama barang tidak ada, maka except akan menampilkan pesan dari Exception yang ada pada Raise. 

- reset_transaction <br />
![gambar](https://user-images.githubusercontent.com/31236670/231789059-3cd2ad72-1002-46c3-aceb-a4d63643008e.png)
Pada fungsi reset_transaction, digunakan untuk menghapus seluruh item. Hal ini dilakukan dengan menimpa dict_barang dengan dictionary kosong, yaitu dict(). Lalu diprint pesan bahwa seluruh transaksi dihapus.

- check_order <br />
![gambar](https://user-images.githubusercontent.com/31236670/231789516-fca31ddd-ee80-4ed1-811d-1ee0aefd9e6c.png)
Pada fungsi check_order, digunakan untuk menampilkan seluruh item yang telah diinput ke tabel. Pertama pada block try, akan dicek apakah dict_barang ada isinya atau tidak. Jika ada, maka pertama kita akan menginisialiasi header tabel, yang terdiri dari No, Nama item, jumlah item, harga/item, dan total harga. Lalu inisialisasi list table kosong, yang nantinya digunakan untuk menampung barang-barang yang ada di dict_barang.

![gambar](https://user-images.githubusercontent.com/31236670/231790349-4db1e959-3a58-41aa-838a-045aea5d7f5a.png)
Lalu dilakukan inisialisasi i = 1, yang akan digunakan untuk penomoran tabel pada kolom "No". Selanjutnya dilakukan proses looping for, dengan menggunakan nilai key pada dict_barang. Digunakan variabel dummy bernama insert_row yang didalmnya berupa list [], yang terdiri dari No yaitu variabel i, nama barang menggunakan key, jumlah barang menggunakan values dict_barang dengan index ke-0, harga barang dengan index ke-1, lalu total harga dengan mengalikan jumlah barang dan harga. variabel i dilakukan increment, untuk proses selanjutnya. Insert row dimasukkan ke dalam list table kosong sebelumnya, sehingga list table ini akan berisi kumpulan list dari dict_barang yang sudah disusun sesuai dengan header table yang telah didefinisikan sebelumnya. Table ini dimasukkan ke dalam fungsi tabulate, dengan headers sebelumnya, dan di print. Hasil yang didapat nanti berupa tabel yang terdiri dari keseluruhan transaksi yang digunakan. Pada bagian else, jika panjang dict_barang masih kosong, pesan data belanja kosong akan ditayangkan. 

- total_price <br />
![gambar](https://user-images.githubusercontent.com/31236670/231792989-2d355f58-ff59-4687-a7b5-f6c85350ad50.png)
Pada fungsi total_price, akan dicek pada block try dan if jika dict_barang kosong atau tidak. Jika tidak, maka akan ditampilkan tabel ringkasan order menggunakan fungsi check_order. Inisialisasi total_harga dengan nilai 0, lalu masuk ke proses for looping pada key dan item dari dict_barang. Pada variable total_harga dilakukan increment dengan menambah perkalian antara item[0] (jumlah) dengan item[1] (harga).

![gambar](https://user-images.githubusercontent.com/31236670/231793791-6235d897-fb21-4311-bf5c-a501cdba23e5.png)
selanjutnya akan dicek diskon berapa yang akan didapat. Jika total_harga lebih dari 500,000 maka diskon yang didapat 10%. Jika total_harga lebih dari 300,000 maka diskon yang didapat 8%. Jika total_harga lebih dari 200,000 maka diskon yang didapat 5%, dan jika total harga di bawah 200,000 maka tidak mendapatkan diskon. Nilai total_harga, diskon yang didapat, serta total yang harus dibayarkan diprint, dan optional, bisa ditambahkan pesan untuk transfer pada rekening tertentu. Harga yang harus dibayar dihitung menggunakan fungsi total_harga dikalikan dengan nilai 1 dikurangi diskon yang dibagi 100. Apabila panjang dict_barang 0, maka pesan data belanja kosong akan di print.


### main.py
Pada program main.py, berisi perintah-perintah yang berkaitan dengan menu yang dapat dipilih.

![gambar](https://user-images.githubusercontent.com/31236670/231795530-4326af80-b703-4e15-8967-a16a1bf58657.png)
Pertama, import file transaction.py dengan fungsi from transaction import Transaction. Membuat menu utama dalam transaksi, dengan print pesan welcome, dan syntax input yang dimasukkan ke dalam variable start_program. apabila kustomer input string y, maka program akan terus berjalan.

![gambar](https://user-images.githubusercontent.com/31236670/231796433-3530ee78-1b7e-4405-9f28-27b80f91f92a.png)
Ketika kustomer input string "y", maka akan masuk block if. Di dalamnya, diinisialisasi variabel end_program = false. Variabel ini akan digunakan untuk menjalankan loop While. Selanjutnya dibuat suatu kelas, bernama trans yang menggunakan class Transaction(). Lalu masuk ke dalam loop While menggunakan variabel end_program. While ini akan terus dijalankan hingga nilai end_program berubah menjadi True. Di dalam while di print list transaksi yang dapat dilakukan, terdiri dari 7 perintah dari tambahkan item hingga keluar. 

![gambar](https://user-images.githubusercontent.com/31236670/231797368-bf5cfaba-d129-45e7-b779-8d09d4ba4649.png)
Selanjutnya kustomer akan diminta untuk input angka dari transaksi yang ingin dilakukan dari nomor 1-7. Angka ini akan dimasukkan ke dalam variabel perintah. Jika perintah == 1, maka dipanggil fungsi add_item(). Jika perintah == 2, dan panjang dict_barang > 0, maka kustomer akan diperlihatkan 3 pilihan, yaitu apakah ingin mengupdate nama item, jumlah item, atau harga item. 

![gambar](https://user-images.githubusercontent.com/31236670/231798063-2f949595-5ba7-4922-98c1-c2b49794e913.png)
Kustomer akan diminta untuk menginput pilihan a/b/c yang dimasukkan ke variable perintah_update. Jika perintah_update == a, maka dipanggil fungsi update_item_name. Jika perintah_update == b, maka dipanggil fungsi update_item_qty. Jika perintah_update == c, maka dipanggil fungsi update_item_price. Jika perintah_update selain a/b/c, maka diprint perintah untuk memasukkan hanya a, b, dan c. 

![gambar](https://user-images.githubusercontent.com/31236670/231798772-466ccd1c-c836-4f59-9758-ed96a491ea62.png)
Jika perintah == 3 dan panjang dict_barang > 0, maka dipanggila fungsi delete_item. Jika perintah == 4, maka dipanggil fungsi reset_transaction. Jika perintah == 5, maka dipanggil fungsi check_order. Jika perintah == 6, maka dipanggil fungsi total_price. 

![gambar](https://user-images.githubusercontent.com/31236670/231799401-317d98db-370d-4d52-b14b-7c58b78e0d41.png)
Jika perintah == 7, maka pertama akan diminta input apakah anda ingin mengakhiri sesi? (y/n). Jika kustomer input string y, maka akan dipanggil fungsi total_price untuk menayangkan rangkuman transaksi. Lalu diprint terima kasih atas kunjungan anda, dan variabel end_program berubah nilainya menjadi True, sehingga program akan keluar dari loop while. Jika kustomer input selain y, maka loop while masih berjalan. 

![gambar](https://user-images.githubusercontent.com/31236670/231800111-6bc859e8-bcfe-4cf3-a2c9-946563b33caa.png)
Pada bagian ini, dicek jika inputan perintah ada di dalam list 2, 3, dan 4, dan panjang dari dict_barang == 0. Maka di print bahwa belum ada barang yang dimasukkan pada dict_barang. Terakhir, apabila inputan nomor tidak ada yang sesuai dari angka 1-7, maka print input sesuai dengan nomor perintah ditayangkan. 

![gambar](https://user-images.githubusercontent.com/31236670/231800786-ecc05b0c-9f1d-4f74-bdeb-cfe8ba9a5372.png)
Jika variabel start_program pada awal file main.py bernilai "n", maka di print anda tidak melakukan transaksi. Lalu jika inputan selain y dan n, maka di print untuk hanya input menggunakan y dan n.


## Hasil Test Case

### Test 1
Kustomer akan memasukkan nilai-nilai sebagai berikut:
* Nama item: Ayam Goreng, Qty: 2, Harga = 20000,
* Nama item: Pasta Gigi, Qty:3; Harga = 15000

Output: <br />
![gambar](https://user-images.githubusercontent.com/31236670/231802538-0c95e691-cd43-4e58-a9a0-940b40bbebc0.png)
![gambar](https://user-images.githubusercontent.com/31236670/231802766-e8453504-7573-4c55-84e6-ef122c044715.png)
![gambar](https://user-images.githubusercontent.com/31236670/231802864-98f384d8-7a0a-4685-bf78-fe88ddb226b7.png)

### Test 2
Kustomer ingin menghapus item Pasta Gigi. 

Output: <br />
![gambar](https://user-images.githubusercontent.com/31236670/231803155-d16757a0-4ed6-45e1-816e-431c04ede8ca.png)
![gambar](https://user-images.githubusercontent.com/31236670/231803256-fc67a8c4-0e3d-4c8e-a5dd-a95dfc515321.png)

### Test 3
Kustomer ingin menghapus seluruh transaksi.

output: <br />
![gambar](https://user-images.githubusercontent.com/31236670/231803639-d8b592b2-7e16-49e0-8db0-90495a9c1344.png)

### Test 4
Kustomer selesai berbelanja, akan menghitung total belanja yang harus dibayarkan.

Output: <br />
![gambar](https://user-images.githubusercontent.com/31236670/231804469-9a2870fd-6c58-482b-92be-07fa83fb70cb.png)

### Test 5 (Bonus)
Jika ingin mengganti nama, jumlah, dan harga. Masukkan saja jika mi instan ingin beli dengan jumlah 50 dengan harga barunya 5000. 

Output: <br />
![gambar](https://user-images.githubusercontent.com/31236670/231805332-9737aa2e-7846-4b33-a421-de86ef454b1f.png)
![gambar](https://user-images.githubusercontent.com/31236670/231805189-164b6cc0-ac26-4278-bf58-948fa1fa85d8.png)
![gambar](https://user-images.githubusercontent.com/31236670/231805485-6f2d85a2-ecd1-42c1-88c6-95ee05551cd6.png)


## Conclusion/Future Work
Pada project self service Supermarket ini digunakan class Transaction yang terdiri dari beberapa fungsi seperti add_item (menambahkan item), update_item_name (mengupdate nama item), update_item_qty (mengupdate jumlah item), update_item_price (mengupdate harga item), delete_item (menghapus 1 item), reset_transaction (menghapus seluruh item), check_order (cek ringkasan order), dan total_price (cek harga yang harus dibayarkan dan diskon yang didapat). Diimplementasikan juga block try-except untuk mempermudah user dalam memahami kesalahan apa yang dilakukan, sehingga kedepannya ketika menginput hal yang sama dapat menghindari kesalahan tersebut.

Pada future work, program ini dapat digabungkan dengan sistem front end seperti webpage sebagai tempat input data-data tersebut, dan digabungkan dengan program ini yang nantinya akan dimasukkan ke dalam suatu database yang berisi ringkasan dari transaksi yang telah dimasukkan. Syntax-syntax input dapat dihilangkan. Daftar barang-barang dapat ditayangkan beserta harganya, sehingga user hanya menginput jumlah yang ingin dibeli. Daftar barang dan harga juga dapat disimpan dalam database, dan dapat dipanggil oleh sistem front end. 
