import requests as rq
from bs4 import BeautifulSoup
import io
import time

class News:
    news_list = []

    def __init__(self,title):
        self.title = title

    def scrape(self,link):
        news_link = rq.get(link)
        soup = BeautifulSoup(news_link.text,'lxml')
        title_block = soup.find_all('p')
        for title in title_block:
            t = title.get_text().strip().strip('\r').strip('\n')
            self.news_list.append(t)
            # print(t)
        # print(self.news_list)
        return self.news_list
        
        
# UDN = News.scrape(News,'https://udn.com/news/cate/2/6638')

