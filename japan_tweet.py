import tweepy
import requests
from bs4 import BeautifulSoup
import re
import datetime
import time
import schedule
from datetime import datetime

# Twitter APIを認証
auth = tweepy.OAuthHandler("Customer Key", "Customer Secret Key")
auth.set_access_token("Access Token", "Access Secret Token")

# APIオブジェクトを作成
api = tweepy.API(auth)

# URLを指定
url = "https://coronavirus.smartnews.com/jp/"

# Requestsを利用してWebページを取得
html = requests.get(url)

# BeautifulSoupを利用してWebページを解析
soup = BeautifulSoup(html.content, "html.parser")

# soup.find_allを利用してデータを取得
data = soup.select("section.summarySec")[0]
date = [x.get_text() for x in soup.select("section.disclaimer")][0].split("\n")[2]

# データの加工
t = [int(re.sub(r"\D", "", x.get_text())) for x in data.select("div.today")]
y = [int(re.sub(r"\D", "", x.get_text())) for x in data.select("div.compare")]

# 現在時刻を表示
today = datetime.now()
hour = today.hour
minute = today.minute
print("{}:{}".format(hour, minute))
 
# ツイート
if hour >= 10 and hour <= 23:
	api.update_status("現時点での本日の国内（日本）の新型コロナウイルス感染者は{}".format(t[1]) + "人です。(" + date + ")\n#国内コロナ感染者数")

else:
	print("時間外のためツイートしませんでした。")