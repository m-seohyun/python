# webcrawling
from bs4 import BeautifulSoup

import requests # http 요청 처리 library

headers = {
    "User-Agent": "Dongyang-Mirae Univ"
}
# 뉴스
webpage = requests.get("https://n.news.naver.com/mnews/hotissue/article/277/0005258668?cid=1089886", headers = headers)
print(webpage)

soup = BeautifulSoup(webpage.content, "html.parser")
print(soup) # dic_area

news = soup.select_one("#dic_area").get_text().strip()
print(news)