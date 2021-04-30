# 新型コロナ感染者数速報BOT[Twitter Bot](@covid19_sokuho)
 
新型コロナウイルスの感染者数を自動的にツイートするBotです。 ツイート対象地域は大阪府・兵庫県・東京都・北海道です。 （2021年4月30日現在）要望があれば、ツイート対象地域を広げます（DMしてください）。 
 
# About
自動で10分おきに感染者数情報を取得しツイートするので、いち早く感染者数情報をお届けすることができます。
 
# Point
他のウェブサイト・テレビなどの他のメディアとは違い、Twitterの通知さえオンにしておけば、通知も受け取ることができます。
 
# Requirement

* Python 3.8.5（これでなくても動く可能性が高いが、Python3以上であることが望ましい）
* Tweepy
* Requests
* BeautifulSoup

# Installation
```bash
pip install tweepy
pip install requests
pip install beautifulsoup4
```
 
# Usage
```bash
cd examples
python tweet.py
```
 
# Note
※感染者数情報はスマートニュースから取得しています。  
※当アカウント・プログラムの使用等に伴う責任は一切負いません。
 
# Author
* 作成者： U_SAY（Twitter：@sekaino_usay）
* E-mail： sekaino.usay@gmail.com
* Web Site: https://profile.sekaino-usay.ga
 
# License
プログラム（ソースコード）はご自由にお使いください。
（※無断での再配布はご遠慮ください。）
Copyright © 2021 U_SAY All Rights Reserved.
