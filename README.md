# TuwiliScan - SQL Injection Vulnerability Scanner

TuwiliScan adalah aplikasi pemindaian (scanner) yang dirancang untuk mendeteksi potensi kerentanannya pada situs web, khususnya **SQL Injection**, dengan cara melakukan crawling dan memeriksa parameter query di URL. Aplikasi ini ditulis menggunakan **Python** dan memanfaatkan beberapa pustaka seperti `requests`, `BeautifulSoup`, dan `termcolor`.

## Fitur Utama
- **Crawling** halaman web untuk menemukan link dengan parameter query.
- **SQL Injection Testing** untuk menguji potensi kerentanannya di URL yang mengandung parameter query.
- **Warna** pada output terminal untuk memberikan feedback yang jelas dan mudah dipahami.
- **Loop Input** untuk meminta URL baru setelah pemindaian selesai atau berhenti jika mengetikkan "exit".

## Prasyarat
Sebelum menjalankan aplikasi, pastikan Anda telah menginstal pustaka yang diperlukan dengan menjalankan perintah berikut:

```bash
pip install requests beautifulsoup4 termcolor
Cara Penggunaan
Clone Proyek Untuk meng-clone proyek ini ke komputer Anda, jalankan perintah berikut:

```bash
git clone https://github.com/tuwiliyt/tuwilscan.git
cd tuwilscan
Jalankan Aplikasi Setelah Anda berada di dalam folder proyek, jalankan aplikasi dengan perintah berikut:

```bash
python tuwilscan.py
Aplikasi akan meminta Anda untuk memasukkan URL domain yang ingin dipindai. Anda dapat memasukkan URL dalam format seperti http://example.com.

Proses Pemindaian Aplikasi akan:
```bash
Melakukan crawling untuk menemukan URL dengan parameter query.
Menguji parameter tersebut dengan beberapa payload SQL Injection.
Menampilkan hasil pemindaian dan memberi tahu jika potensi kerentanannya ditemukan.
Menggunakan Fitur Input Baru Setelah pemindaian selesai, Anda akan diminta untuk memasukkan URL baru atau mengetikkan "exit" untuk keluar dari aplikasi.

```bash
Masukkan URL yang ingin dipindai (misal: http://example.com) atau ketik 'exit' untuk keluar:
Menutup Aplikasi Untuk keluar dari aplikasi, ketikkan exit saat diminta untuk memasukkan URL.

Struktur Direktori
```bash
Copy code
TuwiliScan/
│
├── tuwilscan.py           # File utama untuk menjalankan aplikasi
├── README.md              # Dokumentasi untuk proyek ini
└── requirements.txt       # Daftar pustaka yang dibutuhkan



Contributing
Jika Anda ingin berkontribusi pada proyek ini, silakan lakukan langkah-langkah berikut:

Fork repositori ini.
Buat branch baru (git checkout -b feature-nama-fitur).
Lakukan perubahan yang diinginkan.
Commit perubahan Anda (git commit -am 'Tambah fitur baru').
Push ke branch (git push origin feature-nama-fitur).
Buat pull request.
Lisensi
Proyek ini dilisensikan di bawah lisensi MIT - lihat LICENSE untuk informasi lebih lanjut.
