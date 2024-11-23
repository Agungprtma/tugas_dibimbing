from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

df = pd.DataFrame(columns=['Player','Salary'])
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# driver.get("https://google.com")
driver.get("https://www.capology.com/uk/premier-league/salaries/")

time.sleep(5)

# Ambil semua baris data dari tabel
rows = driver.find_elements(By.XPATH, '//tr[@data-index]')

# Iterasi setiap baris untuk mengambil nama pemain dan gaji tahunan
for row in rows:
    try:
        # Ambil nama pemain
        player = row.find_element(By.XPATH, './td[1]/a').text.strip()
        
        # Ambil gaji tahunan (kolom terakhir dengan class money-column)
        salary = row.find_element(By.XPATH, './td[4]').text.strip()
        
        # Tambahkan data ke DataFrame
        df = pd.concat([df, pd.DataFrame({'Player': [player], 'Salary': [salary]})], ignore_index=True)
    except Exception as e:
        print(f"Error processing row: {e}")

# Cetak DataFrame hasil
print(df)

# Simpan DataFrame ke file CSV
df.to_csv('player_salaries.csv', index=False)
driver.quit()

# elm = driver.find_element(By.CLASS_NAME, "firstcol")

# pemain = [col.text for col in elm]
# print(pemain)

# for row in elm:
#     pemain = row.find_element(By.)

# input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
# input_element.send_keys("hai" + Keys.ENTER)


# 
# time.sleep(10)

# driver.quit()

# -------------------test basket
# for yr in range(1990,2019):
#     page_num = str(yr) + '-' + str(yr+1) +'/'
#     url = 'https://hoopshype.com/salaries/players/' + page_num
#     driver.get(url)
    
#     players = driver.find_elements(By.XPATH, '//td[@class="name"]')
#     salaries = driver.find_elements(By.XPATH, '//td[@class="hh-salaries-sorted"]') 
    
#     players_list = []
#     for p in range(len(players)):
#         players_list.append(players[p].text)
    
#     salaries_list = []
#     for s in range(len(salaries)):
#         salaries_list.append(salaries[s].text)
    
#     data_tuples = list(zip(players_list[1:],salaries_list[1:]))
#     temp_df = pd.DataFrame(data_tuples, columns=['Player','Salary']) 
#     temp_df['Year'] = yr
#     df = pd.concat([df, temp_df], ignore_index=True)

# df.to_csv('player_salaries.csv', index=False)
# driver.close()