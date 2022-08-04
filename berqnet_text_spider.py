import scrapy
from scrapy import Request
from bs4 import BeautifulSoup

class BerqnetTextSpider(scrapy.Spider):
    name = 'berqnetText'
    allowed_domains = ['https://berqnet.com/blog/siber-guvenlik']
    count = 1
    file3 = open("metin.json","a",encoding = "UTF-8")
    with open("urls.json", "rt") as f:
        start_urls = [url.strip() for url in f.readlines()]
    
    def requests(self):
        request=Request(url=self.start_urls, callback=self.parse)
        yield request

    def parse(self, response):
        texts=response.xpath("//*[@id='main']/section/div/article/div[2]/div/div/div[1]/div/div[1]").getall()
        for i in texts:
            clearText = BeautifulSoup(i,"lxml").text
            self.file3.write(clearText + "\n")
            self.count +=1
