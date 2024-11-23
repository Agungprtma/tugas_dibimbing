import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Setup Chrome options untuk mengabaikan sertifikat SSL
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')

# Path ke driver Chrome
service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Buka website
    driver.get("https://hoopshype.com/salaries/players/")

    # Tunggu beberapa detik agar halaman selesai memuat
    time.sleep(5)

    # Ambil data pemain dan gaji
    players = driver.find_elements(By.XPATH, '//td[@class="name"]')
    salaries = driver.find_elements(By.XPATH, '//td[@class="hh-salaries-sorted"]')

    # Ekstrak teks dari elemen
    player_names = [player.text for player in players]
    player_salaries = [salary.text for salary in salaries]

    # Gabungkan data menjadi satu list
    data = list(zip(player_names, player_salaries))

    # Simpan ke file CSV
    with open("players_salaries.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Tulis header
        writer.writerow(["Player", "Salary"])
        # Tulis data
        writer.writerows(data)

    print("Data berhasil disimpan ke 'players_salaries.csv'.")

finally:
    # Tutup browser
    driver.quit()
