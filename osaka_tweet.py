import tweepy
import requests
from bs4 import BeautifulSoup

# Twitter APIを認証
auth = tweepy.OAuthHandler("Customer Key", "Customer Secret Key")
auth.set_access_token("Access Token", "Access Secret Token")

# APIオブジェクトを作成
api = tweepy.API(auth)

# URLを指定
url = "https://coronavirus.smartnews.com/jp/osaka"

# Requestsを利用してWebページを取得
r = requests.get(url)

# BeautifulSoupを利用してWebページを解析
soup = BeautifulSoup(r.text, 'html.parser')

# soup.find_allを利用してデータを取得
elems = soup.find_all("td", class_="stat confirmed")
elems = soup.find_all("div", class_="compare today")
date = soup.find_all("p", class_="us-updated-time")

s = [e.text for e in elems]
n = int(s[0].split()[1])
for e in date:
	api.update_status("現時点での本日の大阪府の新型コロナウイルス感染者は" + str(n) + "人です。(" + e.getText() +")\n#大阪府コロナ感染者数")