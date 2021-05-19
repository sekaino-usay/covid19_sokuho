import tweepy
import requests
from bs4 import BeautifulSoup
import datetime
import time
from datetime import datetime

# Twitter APIを認証
auth = tweepy.OAuthHandler("Customer Key", "Customer Secret Key")
auth.set_access_token("Access Token", "Access Secret Token")

# APIオブジェクトを作成
api = tweepy.API(auth)

# URLを指定
url = "https://coronavirus.smartnews.com/jp/fukuoka"

# Requestsを利用してWebページを取得
r = requests.get(url)

# BeautifulSoupを利用してWebページを解析
soup = BeautifulSoup(r.text, 'html.parser')

# soup.find_allを利用してデータを取得
elems = soup.find_all("td", class_="stat confirmed")
elems = soup.find_all("div", class_="compare today")
date = soup.find_all("p", class_="us-updated-time")

# 現在時刻を表示
today = datetime.now()
hour = today.hour
minute = today.minute
print("{}:{}".format(hour, minute))

# ツイート
s = [e.text for e in elems]
n = int(s[0].split()[1])
for e in date:
	if hour >= 10 and hour <= 23:
		api.update_status("現時点での本日の福岡県の新型コロナウイルス感染者は" + str(n) + "人です。(" + e.getText() +")\n#福岡県コロナ感染者数")

	else:
		print("時間外のためツイートしませんでした。")