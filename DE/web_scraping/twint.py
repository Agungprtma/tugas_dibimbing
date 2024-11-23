import requests
# curl "https://api.twitter.com/2/tweets?ids=12" -H "Authorization: Bearer AAAAAAAAAAAAAAAAAAAAAD8stAEAAAAA8%2FmDEITKtJFyHAuQJa41%2BDPxp04%3DnMrLKyrxUROuJ0JGqyE6tkpbcNkK2rZinPo3RSc3fLuvAZ5nEf"
# Ganti dengan auth_token yang kamu dapatkan dari inspeksi cookies
auth_token = "AAAAAAAAAAAAAAAAAAAAAD8stAEAAAAA8%2FmDEITKtJFyHAuQJa41%2BDPxp04%3DnMrLKyrxUROuJ0JGqyE6tkpbcNkK2rZinPo3RSc3fLuvAZ5nEf"

headers = {
    'Authorization': f'Bearer {auth_token}',  # Gunakan token yang kamu dapatkan
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
}

# Contoh URL untuk mengambil tweet menggunakan token autentikasi
url = 'https://api.twitter.com/2/tweets/search/recent?query=python&max_results=10'

response = requests.get(url, headers=headers)

if response.status_code == 200:
    tweets = response.json()
    for tweet in tweets['data']:
        print(tweet['text'])
else:
    print(f'Error: {response.status_code}')
