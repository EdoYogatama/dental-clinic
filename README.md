Aplikasi Rekam Medis Klinik Dokter Gigi

Actor:
- Dokter

Action:
![Main Page](/doc/ui-example/1.png)
- Dokter melakukan login pada aplikasi
- Dokter melihat list pasien terdaftar pada hari itu pada halaman utama
    Data pada list
    - No. Antrian
    - nama
    - diagnosis komplek
    - usia
    - jk
    - penjamin
    - perawat asesmen => (apakah diperlukan juga?)
    - status pasien: Daftar (belum asesmen), menunggu (terdapat time elapse), selesai => (?)
- Dokter memilih tanggal sebelum/sesudahnya
- Dokter mencari pada search bar berdasar nama pasien, dokter, assesor

![Asesmen Medis | Pemeriksaan Awal](/doc/ui-example/2.png)
Main frame
- Dokter dapat melihat profil pasien pada bagian header
- Dokter dapat melihat riwayat medis pada bagian kanan
    Isi Riwayat Medis => (Isi form lain atau dari data sebelumnya?)
- Doktor dapat menyimpan pengisian form pada bagian footer
- Dokter dapat approve dan undo upproval (apa yang dimaksud dengan approve? apakah menyimpan dan melanjutkan proses?)

Form Frame
- Dokter dapat melihat diagram odontogram dengan penomoran gigi (inputnya bagaimana?)
- Dokter dapat melihat dan mengisi penjelasan setiap nomor gigi
    Kombinasi pasangan 15,55 14,54 13,53 12,52 11,51 21,61 22,62 23,63 24,64 25,65
                       85,45 84,44 83,41 82,42 81,41 71,31 72,32 73,33 74,34 75,35
- Dokter dapat mencetak odontogram

![Asesmen Medis | Asesmen Medis](/doc/ui-example/3.png)
- Dokter mengisi form berupa free text
    - Autoanamnesis
    - Alloamnesis
    - Riwayat penyakit
    - Pemeriksaan objektif

![Asesmen Medis | Diagnosis](/doc//ui-example/4.png)
- dokter melihat tabel dengan data
    - Elemen
    - sisi
    - kode
    - ICD 10
    - Deskripsi
    - Action (Update Delete)
- Dokter dapat menambahkan row data 
- Dokter dapat mengedit row data
- Dokter dapat menghapus row data
- Dokter dapat menambahkan catatan diagnosis

![Asesmen Medis | Tindakan](/doc/ui-example/5.png)
- Dokter melihat tabel dengan data
    - Elemen
    - sisi
    - Tindakan/terapi (Apakah ini sudah ditentukan?)
    - Medis (Apakah ini harga? jika iya apakah biaya nya tetap?)
    - RSGM (Apakah diperlukan dengan penyesuaian nama klinik?)
    - Jumlah
    - Diskon Jasmed
    - Biaya
- Dokter dapat menambahkan row data
- Dokter dapat mengedit row data
- Dokter dapat menghapus row data
- Dokter dapat menambahkan catatan tindakan

![Asesmen Medis | Catatan Edukasi](/doc/ui-example/6.png)
- Dokter memilih combobox catatan edukasi
- Dokter dapat mengisi edukasi lainnya dengan free text

![Asesmen Medis | Daftar Masalah](/doc/ui-example/7.png)

Database Analysis:
- PASIEN
    - ID
    - NAMA
    - TTL -> AGE
    - JK

- ANTRIAN
    - ID
    - TANGGAL
    - NO ANTRIAN
    - STATUS

- DOKTER
    - ID
    - NAMA
    - USERNAME
    - PASSWORD

- ODONTOGRAM
    - ID
    - NO ODONTOGRAM
    - KETERANGAN

- ASESMEN_MEDIS
    - ID
    - ID PASIEN
    - ID DOKTER
    - Autoanamnesis
    - Alloamnesis
    - Riwayat penyakit
    - Pemeriksaan objektif

