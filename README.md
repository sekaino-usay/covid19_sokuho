# 新型コロナ感染者数速報BOT（[Twitter Bot](https://twitter.com/covid19_sokuho)）

新型コロナウイルスの感染者数を自動的にツイートするBotです。  
要望があれば、ツイート対象地域を広げます（DMしてください）。 
 
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
pip install -r requirements.txt
```
 
# Usage
```bash
cd directory
python tweet.py
```
 
# Note
* 感染者数情報はスマートニュースから取得しています。  
* 当アカウント・プログラムの使用等に伴う責任は一切負いません。
* 当プログラムは[ブログ](https://www.sekaino-usay.ga/programming/?p=29)でも紹介しています。ぜひご覧ください。
 
# Developer
* 作成者： U_SAY（[Twitter](https://twitter.com/sekaino_usay)）
* メール： sekaino.usay@gmail.com
* プロフィール: https://www.usay05.com
