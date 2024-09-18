# CAPSTONE PROJECT MODULE 1 
# NABILA SETYA UTAMI (JCDSOL-016)
# Data Nilai Siswa Mata Pelajaran IPA (Semester Genap) SMAN 17 Makassar

import emoji
from tabulate import tabulate 

# <><><><><><><><><><><><><><><><><><><><><><><><> INISIASI DATA <><><><><><><><><><><><><><><><><><><><><><><><>

dataSiswa = [
    {
        'NISN':20241001, 
        'Nama':'Azzahra Zalfa', 
        'Kelas Siswa': 'MIA 1', 
        'NilaiTugas': 83, 
        'NilaiUTS': 64, 
        'NilaiUAS': 77
    },
    {
        'NISN':20231777, 
        'Nama':'Dinda Ismayanti', 
        'Kelas Siswa':'MIA 2', 
        'NilaiTugas': 80, 
        'NilaiUTS': 67, 
        'NilaiUAS': 89
    },
    {
        'NISN':20221835, 
        'Nama':'Andi Ary Jindar', 
        'Kelas Siswa': 'MIA 2', 
        'NilaiTugas': 75, 
        'NilaiUTS': 55, 
        'NilaiUAS': 80
    },
    {
        'NISN':20211019, 
        'Nama':'Isabela Utami',  
        'Kelas Siswa': 'MIA 3', 
        'NilaiTugas': 90, 
        'NilaiUTS': 87, 
        'NilaiUAS': 93
    },
    {
        'NISN':20211011, 
        'Nama':'Muh Abdullah Rasyad', 
        'Kelas Siswa': 'MIA 3', 
        'NilaiTugas': 80, 
        'NilaiUTS': 83, 
        'NilaiUAS': 88
    }
]

dataSiswa_update = dataSiswa.copy()
nomor = 0 

# Fungsi Input NISN
def input_nisn():
    while True:
        global nomor
        nomor = input('\nMasukkan NISN / Nomor Induk Siswa Nasional (8 Digit): ')
        if nomor.isdigit() == True:
            if int(len(nomor)) != 8:
                print('\nMaaf, NISN (Nomor Induk Siswa Nasional) Harus Terdiri dari 8 Angka')
            else:
                nomor = int(nomor)
            break
        else:
            print('\nMaaf, NISN (Nomor Induk Siswa Nasional) Harus Terdiri dari 8 Angka') 

# Fungsi Inputan Tidak Sesuai
def wrong_choice():
    print('\nMaaf, Pilihan yang Anda Masukkan Salah 🙏🏻')

# Fungsi Data Kosong
def data_kosong():
    print('\nMaaf, Data Siswa yang Anda Masukkan Tidak Ada 🙏🏻')   


# <><><><><><><><><><><><><><><><><><><><><><><><><> Bagian Menu 1 --> Menampilkan Seluruh atau Sebagian Data <><><><><><><><><><><><><><><><><><><><><><><><>
# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> MENAMPILKAN DATA SISWA <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

#Fungsi Menampilkan Seluruh Data
def view_menu():
    while True:
        try:
            print('\nData Nilai Siswa Mata Pelajaran IPA (Semester Genap) di SMAN 17 Makassar')
            print(tabulate(dataSiswa_update , headers = 'keys', tablefmt = 'fancy_grid'))
        except:
            print('Maaf, Data Siswa Yang Anda Masukan Salah 🙏🏻')
        break

def read_menu():
    menu = {
        'MENU MENAMPILKAN SELURUH ATAU SEBAGIAN DATA SISWA' : ['1. Menampilkan Semua Data Siswa\n2. Data Siswa Berdasarkan NISN\n3. Kembali ke Menu Utama']
    }
    print(tabulate(menu, headers = 'keys', tablefmt = 'fancy_grid'))

    baca_data = input('Silakan Pilih Salah Satu Menu (1-3): ')

    if baca_data == '1': 
        if len(dataSiswa_update) == 0:
            data_kosong()
            read_menu()
        else:
            view_menu()
            read_menu()
    elif baca_data == '2': 
        if len(dataSiswa_update) == 0:
            data_kosong()
            read_menu()
        else:
            input_nisn()
            for data_update in dataSiswa_update:
                if data_update['NISN'] == nomor:
                    print(f'\nBerikut adalah Data Siswa dengan NISN {nomor}')
                    print(f'''
    NISN : {data_update['NISN']}
    Nama Lengkap : {data_update['Nama']}
    Kelas : {data_update['Kelas Siswa']}
    Nilai Tugas : {data_update['NilaiTugas']}
    Nilai UTS : {data_update['NilaiUTS']}
    Nilai UAS : {data_update['NilaiUAS']}    
                    ''')
                break
            if data_update['NISN'] != nomor:
                data_kosong()
            read_menu()
    elif baca_data == '3':
        menu_utama()
    else:
        wrong_choice()
        read_menu()

# Fungsi Cek Data Nama dan Kelas
def cek_nama():
    while True:
        global nama_lengkap
        nama_lengkap = input('\nSilakan Masukkan Nama Lengkap Siswa: ')
        if nama_lengkap.replace(' ','').isalpha() == True:
            return(nama_lengkap)
            break
        print('\nMaaf, Inputan Anda Tidak Valid.\n Silakan Masukkan Ulang 🙏🏻😊.')

def cek_kelas():
    while True:
        global kelas_baru
        kelas_baru = input('\nSilakan Masukkan Kelas Siswa (cth: MIA 4): ')
        if kelas_baru.replace(' ','') == True:
            return(kelas_baru)
            break
        print('\nMaaf, Inputan Anda Tidak Valid.\n Silakan Masukkan Ulang 🙏🏻😊.')  

# Fungsi Cek Nilai Tugas
def cek_tugas():
    while True:
        global nilai_tugas
        nilai_tugas = input('\nSilakan Masukkan Nilai Tugas (0-100): ')
        if nilai_tugas.isnumeric() == True:
            if int(nilai_tugas) >= 0 and int(nilai_tugas) <= 100:
                return(nilai_tugas)
                break
            else:
                print('\nMaaf, Nilai Tugas Melebihi Batas.\nSilakan Masukan Ulang Nilai Tugas Dengan Rentang (0-100) 🙏🏻😊')
        else: 
            print('\nMaaf, Data yang Anda Input Tidak Benar.\nSilakan Memasukkan Ulang Nilai UTS Siswa 🙏🏻😊')

# Fungsi Cek Nilai UTS
def cek_uts():
    while True:
        global nilai_uts
        nilai_uts = input('\nSilakan Masukkan Nilai UTS (0-100): ')
        if nilai_uts.isnumeric() == True:
            if int(nilai_uts) >= 0 and int(nilai_uts) <= 100:
                return(nilai_uts)
                break
            else:
                print('\nMaaf, Nilai UTS Melebihi Batas.\nSilakan Masukan Ulang Nilai UTS Dengan Rentang (0-100) 🙏🏻😊')
        else: 
            print('\nMaaf, Data yang Anda Input Tidak Benar.\nSilakan Memasukkan Ulang Nilai UTS Siswa 🙏🏻😊')

# Fungsi Cek Nilai UAS
def cek_uas():
    while True:
        global nilai_uas
        nilai_uas = input('\nSilakan Masukkan Nilai UAS (0-100): ')
        if nilai_uas.isnumeric() == True:
            if int(nilai_uas) >= 0 and int(nilai_uas) <= 100:
                return(nilai_uas)
                break
            else:
                print('\nMaaf, Nilai UAS Melebihi Batas.\nSilakan Masukan Ulang Nilai UAS Dengan Rentang (0-100) 🙏🏻😊')
        else: 
            print('\nMaaf, Data yang Anda Input Tidak Benar.\nSilakan Memasukkan Ulang Nilai UAS Siswa 🙏🏻😊')

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> MENAMBAHKAN DATA SISWA <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

def add_menu():
    menu = {
        'MENU MENAMBAHKAN DATA SISWA' : ['1. Menambahkan Data Siswa\n2. Kembali ke Menu Utama']
    }
    print(tabulate(menu, headers = 'keys', tablefmt = 'fancy_grid'))

    tambah_data = input('Silakan Pilih Salah Satu Menu (1/2): ')

    if tambah_data == '1':
        input_nisn()
        for data_update in dataSiswa_update :
            if data_update['NISN'] == nomor:
                print(f'Maaf, Data dengan NISN {nomor} Sudah Tersedia.')
                break
        if data_update['NISN'] != nomor:
            nama_lengkap = cek_nama().capitalize()
            kelas_baru = cek_kelas().capitalize()
            nilai_tugas= cek_tugas()
            nilai_uts = cek_uts()
            nilai_uas= cek_uas()
            
            confirm = input('\nApakah Anda Ingin Menyimpan Data Baru Siswa Tersebut (Ya/Tidak)? ').upper()
            if confirm == 'YA':
                dataSiswa_update.append({'NISN': nomor, 'Nama': nama_lengkap, 'Kelas Siswa': kelas_baru, 'NilaiTugas': nilai_tugas, 'NilaiUTS': nilai_uts, 'NilaiUAS': nilai_uas})
                print('\nTerima Kasih, Data Anda Berhasil Disimpan ✅')
        add_menu()
    elif tambah_data == '2':
        menu_utama()
    else:
        wrong_choice()
        add_menu()

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> MENGUBAH DATA SISWA <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
def change_menu():
    while True:
        try:
            menu = {
                'MENU MENGUBAH DATA SISWA' : ['1. Mengubah Data Siswa\n2. Kembali ke Menu Utama']
            }
            print(tabulate(menu, headers = 'keys', tablefmt = 'fancy_grid'))
            
            ubah_data = input('Silakan Pilih Salah Satu Menu di Atas (1/2): ')

            if ubah_data == '1':
                input_nisn()
                nomor_awal = nomor
                ganti_data = ''
                for data_update in dataSiswa_update:
                    if data_update['NISN'] == nomor_awal:

                        # Menampilkan Data Lengkap Siswa Terlebih Dahulu
                        data = {
                            'NISN' : {data_update['NISN']},
                            'Nama Lengkap ': {data_update['Nama']},
                            'Kelas' : {data_update['Kelas Siswa']},
                            'Nilai Tugas' : {data_update['NilaiTugas']}, 
                            'Nilai UTS' : {data_update['NilaiUTS']}, 
                            'Nilai UAS' : {data_update['NilaiUAS']}
                        }
                        print(tabulate(data, headers = 'keys', tablefmt = 'fancy_grid'))

                        # Proses Update Data
                        update = input('\nApakah Anda Ingin Meng-update Data Siswa (Ya/Tidak)? ').upper()
                        if update == 'YA':
                            ganti_data= input('\nSilakan Pilih Salah Satu Subjek yang Ingin Diganti (NISN/Nama Lengkap/Kelas/Nilai Tugas/Nilai UTS/Nilai UAS): ').upper()
                            if ganti_data.replace(' ','').upper() in dataSiswa_update[0].keys():
                                if ganti_data == 'NISN':
                                    input_nisn()
                                    nisn_baru = nomor

                                    # Memastikan Tidak Ada Duplikasi NISN
                                    list_nomor = [data_update['NISN'] for data_update in dataSiswa_update]
                                    while nisn_baru in list_nomor:
                                        print('\nMaaf, NISN yang Anda Input Sudah Terpakai')
                                        input_nisn()
                                        nisn_baru= nomor
                                else:
                                    nisn_baru = input(f'\nMasukkan {ganti_data} baru: ')

                                # Perintah Update Data
                                confirm = input('\nApakah Anda Yakin Ingin Mengubah Data Siswa Tersebut (Ya/Tidak)? ').upper()
                                if confirm == 'YA':
                                    data_update[ganti_data.replace(' ','').upper()] = nisn_baru
                                    print('\nTerima Kasih, Data Siswa Berhasil Diubah ✅')
                            else:
                                wrong_choice()
                        break
                if ganti_data != nomor:
                    if data_update['NISN'] != nomor_awal:
                        data_kosong()
                change_menu()
            elif ubah_data == '2':
                menu_utama()  
            else:
                wrong_choice()
                change_menu()
        except:
            print('\nMaaf, Data Siswa yang Anda Masukkan Tidak Ada 🙏🏻')
            change_menu()
        break

# <><><><><><><><><><><><><><><><><><><><><><><><> MENGHAPUS DATA SISWA <><><><><><><><><><><><><><><><><><><><><><><><>
def delete_menu():
    while True:
        try:
            menu = {
                'MENU MENGHAPUS DATA SISWA' : ['1. Menghapus Data Siswa\n2. Kembali ke Menu Utama']
            }
            print(tabulate(menu, headers = 'keys', tablefmt = 'fancy_grid'))

            menu_delete = input('Silakan Pilih Salah Satu Menu di Atas (1/2): ')

            if menu_delete == '1':
                input_nisn()
                for i, data_update in enumerate(dataSiswa_update):
                    if data_update['NISN'] == nomor:
                        delete = input(f'\nApakah Data Siswa dengan NISN {nomor} Akan Dihapus (Ya/Tidak)? ').upper()
                        if delete == 'YA':
                            del dataSiswa_update[i]
                            print('\nDATA SISWA')
                            data = {
                            'NISN' : {data_update['NISN']},
                            'Nama Lengkap ': {data_update['Nama']},
                            'Kelas' : {data_update['Kelas Siswa']},
                            'Nilai Tugas' : {data_update['NilaiTugas']}, 
                            'Nilai UTS' : {data_update['NilaiUTS']}, 
                            'Nilai UAS' : {data_update['NilaiUAS']}
                        }
                        print(tabulate(data, headers = 'keys', tablefmt = 'fancy_grid'))
                        print('\nData Siswa Berhasil Dihapus ✅')
                        break
                if data_update['NISN'] != nomor:
                    data_kosong()
                delete_menu()
            elif menu_delete == '2':
                menu_utama()
            else:
                wrong_choice()
                delete_menu()
        except:
            print('\nMaaf, Data Siswa yang Anda Masukkan Tidak Ada 🙏🏻')
            delete_menu()
        break

# <><><><><><><><><><><><><><><><><><><><><><><><> INFORMASI NILAI AKHIR SISWA <><><><><><><><><><><><><><><><><><><><><><><><>
def final_menu():
    while True:
        try:
            menu = {
                'MENU INFORMASI NILAI AKHIR SISWA' : ['1. Informasi Nilai Akhir Siswa\n2. Kembali ke Menu Utama']
            }
            print(tabulate(menu, headers = 'keys', tablefmt = 'fancy_grid'))
            
            nilai_akhir = input('Silakan Pilih Sub Menu di Atas (1/2): ')

            # Menghitung Nilai Akhir Siswa
            if nilai_akhir == '1':
                input_nisn()
                for data_update in dataSiswa_update:
                    if data_update['NISN'] == nomor:
                        #Perhitungan Nilai Akhir Siswa
                        nilai_akhir = (25/100) * int(data_update['Nilai Tugas']) + (35/100) * int(data_update['Nilai UTS']) + (40/100) * int(data_update['Nilai UAS'])
                        data = {
                            'NISN' : {data_update['NISN']},
                            'Nama Lengkap ': {data_update['Nama']},
                            'Kelas' : {data_update['Kelas Siswa']},
                            'Nilai Tugas' : {data_update['NilaiTugas']}, 
                            'Nilai UTS' : {data_update['NilaiUTS']}, 
                            'Nilai UAS' : {data_update['NilaiUAS']},
                            'Nilai Akhir' : {round(nilai_akhir,2)}
                        }
                        print(tabulate(data, headers = 'keys', tablefmt = 'fancy_grid'))
                        break
                if data_update['NISN'] != nomor:
                    data_kosong()
                final_menu()
            elif nilai_akhir == '2':
                menu_utama()
            else: 
                wrong_choice()
                final_menu()
        except:
            print('\nMaaf, Data Siswa yang Anda Masukkan Tidak Ada 🙏🏻')
            delete_menu()
        break

# <><><><><><><><><><><><><><><><><><><><><><><><> MENU UTAMA <><><><><><><><><><><><><><><><><><><><><><><><>

def menu_utama():
    print('Halo, Selamat Datang 😊')
    
    menu = {
                'Program Data Nilai Siswa Mata Pelajaran IPA (Semester Genap) SMAN 17 Makassar' : 
                ['1. Menampilkan Seluruh Data Siswa\n2. Menambahkan Data Siswa\n3. Mengubah Data Siswa\n4. Menghapus Data Siswa\n5. Informasi Nilai Akhir Siswa\n6. Keluar / Exit']
            }
    print(tabulate(menu, headers = 'keys', tablefmt = 'fancy_grid'))
    
    mainmenu_input = input('Silakan Pilih Salah Satu Menu di Atas (1-6): ')

    if mainmenu_input == '1':
        read_menu() 
    elif mainmenu_input == '2':
        add_menu()  
    elif mainmenu_input == '3':
        change_menu()
    elif mainmenu_input == '4':
        delete_menu()
    elif mainmenu_input == '5':
        final_menu()
    elif mainmenu_input == '6':
        print('\nTerima Kasih. \nHave a Nice Day 🤗🥰\n')
    else:
        wrong_choice()
        menu_utama()

menu_utama() 

