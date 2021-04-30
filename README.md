# 新型コロナ感染者数速報BOT（[Twitter Bot](https://twitter.com/covid19_sokuho)）
 
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
* 感染者数情報はスマートニュースから取得しています。  
* 当アカウント・プログラムの使用等に伴う責任は一切負いません。
 
# Author
* 作成者： U_SAY（[Twitter](https://twitter.com/sekaino_usay)）
* E-mail： sekaino.usay@gmail.com
* Web Site: https://profile.sekaino-usay.ga
 
# License
MIT License

Copyright (c) 2021 U_SAY

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
