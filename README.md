Rubric

**1. Persyaratan umum proyek**
   - Keseluruhan kode pemrograman dilakukan dengan prinsip 3-Tier Architecture (Kelas untuk antarmuka, layanan dan basis data dituliskan pada 3 file yang berbeda)

**2. Persyaratan- persyaratan dari pelanggan**
   - Sistem smart home ini memiliki moda penggunaan manual dan otomatis
   - Moda penggunaan ini dapat diganti-ganti pada antarmuka pengguna
   - Catatan perubahan moda penggunaan ini disimpan dalam basis data aplikasi
   - Untuk menggunakan aplikasi My Smart Home, pengguna harus login dengan berhasil terlebih dahulu. Apabila login belum berhasil, maka user tidak dapat memakai aplikasi My Smart Home.
   - Apabila tidak ada yg login sama sekali, maka aplikasi My Smart Home otomatis akan beralih ke mode manual
   - Informasi semua username dan password disimpan di dalam basis data
   - Ada 4 human user aplikasi dengan kemampuan yang berbeda-beda, yaitu:
      a. Admin: tidak dapat menggunakan aplikasi, hanya dapat mengirimkan password yang baru pada user lainnya melalui email (Hanya perlu implementasi sebuah tombol untuk print password yang baru untuk salah satu user. Password ini tertera juga di dalam basis data)
      b. Parent: dapat menggunakan semua fungsi smart home
      c. Children: tidak dapat merubah mode smart home
      d. Guest: hanya dapat memakai smart home apabila Parent sedang mengaktifkan fungsi guest mode
   - Username dan password untuk setiap jenis user disimpan di dalam basis data
   - Kemampuan setiap jenis user disimpan di dalam basis data

  Pada mode manual, hasil pengukuran semua sensor diabaikan. Pengguna menyalakan/mematikan lampu, AC dan musik melalui antarmuka pada smartphone
  - Setiap perubahan status lampu, AC dan penyetelan musik dicatat di dalam basis data aplikasi
  - Ada 1 user otomatis (aplikasi) yang dapat menggunakan semua fungsi smarthome apabila mode otomatis sedang diaktifkan.
  - Pengguna jenis Parent dapat merubah moda menjadi otomatis atau manual kapanpun dia mau
		
  Pada moda otomatis:
  - Pengguna tidak dapat menyetel lampu, AC dan musik melalui antarmuka pengguna
  - Hasil pengukuran sensor yang dipakai untuk menyalakan/mematikan lampu, AC dan musik
  - Semua lampu akan otomatis dinyalakan apabila ruangan mulai gelap dan ada orang di dalam ruangan tersebut
  - Semua AC akan otomatis dinyalakan apabila ruangan mulai panas dan ada orang di dalam ruangan tersebut
  - Musik di semua ruangan akan otomatis dinyalakan apabila ada orang yang masuk ke dalam ruangan tersebut
  - Status lampu, AC dan musik dapat dilihat pada antarmuka di smartphone
  - Setiap perubahan status lampu, AC dan penyetelan musik dicatat di dalam basis data aplikasi
  - Pada pagi hari (pukul 08.00-11.00) mereka menginginkan ada lagu yang dimainkan pada ruangan-ruangan di dalam rumah mereka.
  - 4 jenis ruangan akan memiliki fungsi smart home dengan spesifikasi yang berbeda-beda, yaitu:
      Bedroom: lampu dan musik di dalam ruangan ini tidak otomatis menyala pada pukul 22.00-06.00
      Bathroom: tidak ada AC di dalam ruangan ini
      Living room: memiliki lampu, AC dan musik
      Kitchen: memiliki lampu, AC dan musik

