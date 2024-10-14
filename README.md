# Mini-Project-Dasar-Dasar--Praktikum-Jasa-Jastip

![diagram minpro 2 drawio (1)](https://github.com/user-attachments/assets/6b152f89-745c-4edf-a2e8-7bfa2584f4a4)

Penjelasan kode dan output

### Import Library

![image](https://github.com/user-attachments/assets/d27028aa-84d8-488c-a67b-2aacdbf8fe25)

Untuk import pretty table agar pretty table dapat digunakan

### Data Akun dan List Untuk Database

![image](https://github.com/user-attachments/assets/ea58383e-8328-49ec-9808-1d39283d3013)

akun dan nim itu sebagai akun dan id admin, sedangkan list merupakan list barang yang bisa kita edit, di list menggunakan dictionary agar proses pengupdate-an lebih mudah, sedangkan belanjaan merupakan list kosong yang nantinya akan kita isi dengan barang yang dibeli oleh user

### Menu Login

![image](https://github.com/user-attachments/assets/1d67477e-29c0-46d7-a2f2-b1d8f8beb5ed)

menu login untuk proses login agar kita bisa membedakan admin dengan user, jika id dan pass sama seperti diatas maka akun akan terdetect sebagai admin, sedangkan jika akun tidak sesuai ataupun password tidak sesuai maka akun akan terdetect sebagai user, jika pilihan 2 maka akan keluar dari program

output:

![image](https://github.com/user-attachments/assets/92400cdf-173f-4b09-b0b7-9653dc054ad7)

### Function Lihat (Admin)

![image](https://github.com/user-attachments/assets/9bb0758c-870c-458e-9264-4eab2908a20e)

Untuk melihat barang yang dijual menggunakan pretty table agar list berbentuk table dan menggunakan perulangan for agar list jadi kebawah

### Function Lihat (User dan Admin)

![image](https://github.com/user-attachments/assets/069448ad-c653-4762-9c2a-d9d239b637c4)

Untuk melihat barang yang dibeli seperti keranjang belanjaan shopee

### Function tambahkan item

![image](https://github.com/user-attachments/assets/8156b1af-f5cf-4ea8-85ff-d37a64a48d24)

Untuk menambah item yang dijual, kita harus menambahkan variabel di () agar variabel dapat terbaca, begitu juga di kode kode lainnya

### Function Update

![image](https://github.com/user-attachments/assets/aa88bb82-c105-401b-8886-83a93d7e1ebb)

Untuk update item jika pilihan dari input = 1, maka item yang di update adalah item yang dijual dan jika pilihan input = 2, maka item yang di update adalah item yang sudah terbeli, jika tidak ada item di list atau id salah maka akan muncul output "Barang tidak ditemukan"

### Function Hapus (Admin)

![image](https://github.com/user-attachments/assets/20cb8d04-ea3f-4ff8-8fd1-4204cc145b36)

Untuk menghapus barang yang dijual, jika tidak barang yang dijual, jika tidak ada barang atau id salah "ID barang tidak ditemukan"

### Function Hapus (User)

![image](https://github.com/user-attachments/assets/69a9cd62-201e-4d37-9e0c-9181a9c8d610)

Untuk menghapus barang yang dibeli oleh user

### Function Beli

![image](https://github.com/user-attachments/assets/19e8fd4a-157f-4d07-bdd7-4a3cc4f152ce)

Untuk membeli barang, sistemnya jika barang berhasil dibeli dan ditaro ke keranjang belanjaan maka stok barang akan berkurang dengan kode item_2["Jumlah barang"] += 1 dan belanjaan.append untuk menambah belanjaan ke list belanjaan

### Function Login user

![image](https://github.com/user-attachments/assets/d4cc1c86-530c-47b9-900c-aca050d508b2)

Akun anda ter detect sebagai user, disini bisa memilih 4 pilihan

output:

![image](https://github.com/user-attachments/assets/e90ade0f-4472-4917-9ae3-c76a536ef9c1)

### Pilihan 1-4 (User)

![image](https://github.com/user-attachments/assets/33c107f6-cf03-4abf-a775-d2f0de721c8a)

Jika kita memilih pilihan 1: kita bisa meihat dan membeli barang dengan id yang kita input 

Jika kita memilih pilihan 2: kita bisa menghapus barang yang sudah kita beli menggunakan id yang kita input

Jika kita memilih pilihan 3: kita bisa melihat barang yang sudah ktia beli dan total harganya

Jika kita memilih pilihan 4: kita akan logout dan kembali ke menu login

output:

pilihan 1:

![image](https://github.com/user-attachments/assets/b58aadf1-8513-4e45-acda-ffebfaca7abc)

pilihan 2:

![image](https://github.com/user-attachments/assets/120d9ea4-edcb-400b-b5b8-3bdeeaf803fe)

pilihan 3:

![image](https://github.com/user-attachments/assets/e11917a5-fd0b-43fe-874f-5ffaf773ce3c)

### Login admin

![image](https://github.com/user-attachments/assets/8fdc12f9-701d-4e53-aa02-0a0e8b8b2071)

Akun anda terdetect sebagai admin, disini bisa memilih 5 pilihan

output:

![image](https://github.com/user-attachments/assets/27c0d39a-123e-4365-ae94-74643016ea63)

### Pilihan 1-5 user

![image](https://github.com/user-attachments/assets/dabd1143-9be6-4a3d-adb2-29ab8b671a4b)

Jika kita memilih pilihan 1: akan muncul 2 pilihan lagi untuk melihat barang yang dijual dan barang yang sudah terjual

Jika kita memilih pilihan 2: kita bisa menambahkan barang dengan memasukan nama, harga dan jumlah

Jika kita memilih pilihan 3: akan muncul 2 pilihan lagi untuk meng-update barang yang dijual atau terjual dengan memasukan nama, harga dan jumlah

Jika kita memilih pilihan 4: kita bisa menghapus barang yang dijual dengan id barang

Jika kita memilih pilihan 5: kita akan kembali ke menu login

output:

Pilihan 1.1 :

![image](https://github.com/user-attachments/assets/88187de0-cdf6-4dcb-ac15-e99e36b5dce0)

Pilihan 1.2 :

![image](https://github.com/user-attachments/assets/493e4d44-b4ea-44b0-b801-e8bc00c67b85)


Pilihan 2:

![image](https://github.com/user-attachments/assets/03f5b688-2768-45b1-8d17-29c8743832ec)

Pilihan 3.1

![image](https://github.com/user-attachments/assets/deb2eafd-a050-4e36-a4cd-020fead4b256)

Pilihan 3.2

![image](https://github.com/user-attachments/assets/d7bb989a-e127-47b3-bb2f-de7d795e2b7c)

Pilihan 4

![image](https://github.com/user-attachments/assets/6c9aa970-1a02-4185-990f-0bb7c611cc18)


































