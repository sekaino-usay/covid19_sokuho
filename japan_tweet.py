import tweepy
import requests
from bs4 import BeautifulSoup
import re

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

api.update_status("現時点での本日の国内（日本）の新型コロナウイルス感染者は{}".format(t[1]) + "人です。（" + date + "）\n#国内コロナ感染者数")