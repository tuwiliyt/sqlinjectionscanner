![TuwiliScan Screenshot](https://github.com/tuwiliyt/sqlinjectionscanner/blob/main/ss1.png)
![TuwiliScan Screenshot](https://github.com/tuwiliyt/sqlinjectionscanner/blob/main/ss2.png)

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


