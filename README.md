# **Capstone Project Modul 1 (Data Nilai Siswa)**
## Nabila Setya Utami (JCDSOL-016)
*Sebuah program yang dirancang untuk memudahkan user dalam mengakses data nilai siswa dalam kepentingan bidang akademik. Dalam hal ini mampu menampilkan keseluruhan dan sebagian nilai siswa, memperbaharui, menghapus, dan menambah data siswa. Serta mampu membantu memberikan perhitungan nilai akhir siswa dengan lebih cepat.*

### Stakeholders
- Guru
- Dosen
- Tutor
- Tenaga Pendidik Lainnya

## **Menu Utama**
Berikut tampilan menu utama dari program *Data Nilai Siswa Mata Pelajaran IPA (Semester Genap) SMAN 17 Makassar*. Pada menu ini user dapat memilih menu yang diinginkan yang terdiri dari 6 sub menu, dapat dilihat pada gambar di bawah ini. 

   ![image](https://github.com/user-attachments/assets/77cb2a7c-7f8d-4085-8819-83421e10ee3d)

## **Fitur-Fitur**
### **Fitur Read**
Dalam fitur read ini, user dapat melihat keseluruhan data nilai siswa dan juga dapat melihat sebagian data siswa dengan menginput NISN / Nomor Induk Siswa Nasional yg ingin dilihat detail datanya pada program yang telah dibuat.
1. Menampilkan Keseluruhan Data Siswa \n

   ![image](https://github.com/user-attachments/assets/049e6a2e-4f6e-4de7-81c6-8072c4e70523)
   ![image](https://github.com/user-attachments/assets/155b56c6-f40c-44b7-b969-d70fee18ad5d)

Pada bagian ini, user dapat melihat keseluruhan data siswa. Terdiri dari NISN, nama, kelas, nilai tugas, nilai uts, dan nilai uas. Nilai NISN di program ini sebagai kunci yang akan digunakan untuk melakukan tindakan selanjutnya pada program.

2. Menampilkan Sebagian Data Siswa 

   ![image](https://github.com/user-attachments/assets/4dd225f0-bd38-44c5-86af-6a0fdb160acd)
   ![image](https://github.com/user-attachments/assets/a4edb366-fb1d-4655-ad90-0a41d13020e8)

Sub menu ini menampilkan sebagian data siswa dengan memasukkan atau meng-*input* nisn siswa, selanjutnya akan menampilkan data siswa berupa nisn, nama, kelas, nilai tugas, nilai uts, dan nilai uas dari nisn yang telah di-*input* sebelumnya.

### **Fitur Create**
Pada fitur ini, disajikan program penambahan data siswa dengan memasukkan ke dalam dataset berupa NISN, nama siswa, kelas, nilai tugas, nilai uts, dan nilai uas yang belum pernah tersimpan di dalam dataset yang telah ada. Berikut tampilan dari fitur create atau add new data pada program Data Nilai Siswa.

   ![image](https://github.com/user-attachments/assets/539749f0-a19d-4e31-b5d9-4e61bd801956) \n
   ![image](https://github.com/user-attachments/assets/2b59f321-5e67-4be8-9837-a9ff30580cdf)
   ![image](https://github.com/user-attachments/assets/0ad31f46-0149-4ddd-b42f-80f58758e6a3)


### **Fitur Edit**
Fitur ini mampu mengubah, mengedit, atau meng-*update* data yang telah ada menjadi data baru dengan cara memilih subjek data yang ingin diperbaharui, sehingga menampilkan informasi data baru yang telah di-*update*. Dalam hal ini subjek yang bisa di ubah, yaitu nisn, nama, kelas, nilai tugas, nilai uts, dan nilai uas.

1. Menu Tampilan Mengubah Data Siswa \n
   ![image](https://github.com/user-attachments/assets/22aa0a9e-e4b8-4d8c-9c8a-c3a37811df75)
   
2. Tampilan Mengubah NISN Siswa
   ![image](https://github.com/user-attachments/assets/65809281-1473-4532-8a43-26b940f58df1)
   
3. Tampilan Mengubah Nama Siswa
   ![image](https://github.com/user-attachments/assets/a6fc6e11-e338-43b3-81c5-ccf7cd7839d9)
   
4. Tampilan Mengubah Kelas Siswa
   ![image](https://github.com/user-attachments/assets/c887f26f-653b-48ad-a79d-abca067870ad)
   
5. Tampilan Mengubah Nilai Tugas Siswa
   ![image](https://github.com/user-attachments/assets/dde25d02-97ce-421b-a0f8-34cf4adb9387)
   
6. Tampilan Mengubah Nilai UTS Siswa
   ![image](https://github.com/user-attachments/assets/16b8b359-9e2d-45db-af17-00906af7e88c)
   
7. Tampilan Mengubah Nilai UAS Siswa
   ![image](https://github.com/user-attachments/assets/25518db4-8d33-4826-afef-a99b9de640ad)
   
8. Tampilan Keseluruhan Data yang Telah Diubah
   ![image](https://github.com/user-attachments/assets/d91dc46a-f6b4-4638-9b88-8b208d73e0d7)

### **Fitur Delete**
Apabila terdapat data yang ingin dihapus oleh user, fitur ini mampu menghapus data siswa yang tersimpan dengan hanya memasukkan NISN / Nomor Induk Siswa Nasional maka data dari siswa tersebut akan terhapus. Penghapusan data satu siswa hanya bisa dilakukan sekali kesempatan.

   ![image](https://github.com/user-attachments/assets/ab097916-343d-4e7b-bc0f-6370641618e0)
   ![image](https://github.com/user-attachments/assets/ffb091b2-6002-492d-9224-95f5370ee07a)
   ![image](https://github.com/user-attachments/assets/18c9ebb8-b864-48cc-8a26-5f03a25a3f91)

### **Fitur Hitung Nilai Akhir (Tambahan)**
Fitur ini ditambahkan guna mempermudah user dalam melakukan perhitungan nilai akhir siswa tanpa perlu menghitung manual secara satu persatu. Hanya dengan memasukkan nisn dari siswa yang ingin dicari nilai akhirnya, maka akan muncul pada kolom terakhir nilai akhir dari siswa tersebut dengan menggunakan pembulatan 2 angka di belakang koma.

   ![image](https://github.com/user-attachments/assets/fa6a1ee6-46a5-4d42-ac70-0aa592c6fc2a)
   ![image](https://github.com/user-attachments/assets/1f06d183-46d6-4abc-910d-be96192d75b6)
