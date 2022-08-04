from urllib.parse import urljoin
import scrapy
import json
from bs4 import BeautifulSoup

class HackernewsSpider(scrapy.Spider):
    name = 'hackernews'
    allowed_domains = ['thehackernews.com']
    start_urls = ['https://thehackernews.com/']
    unique_data=set()
    page_count = 0
          
   

    def parse(self, response):
        div=response.xpath("/html/body/main/div/div/div/div/div/div[1]/div[1]")
     
    
        for x in div:
            baslik=x.xpath("./a/div/div[2]/h2/text()").get()
            url=x.xpath("./a/@href").get()
            
            if baslik not in self.unique_data :
                self.unique_data.add(baslik)
                yield scrapy.Request(url,callback=self.parse_detail,meta={"baslik":baslik,"url":url})

        self.page_count += 1
        while self.page_count < 25:
            next_page = response.xpath("//*[@id='Blog1_blog-pager-older-link']/@href").get()
            yield scrapy.Request(url = next_page, callback = self.parse)

    def parse_detail(self,response):

        baslik=response.meta.get("baslik")
        url=response.meta.get("url")

        metin = response.xpath("/html/body/main/div/div[1]/div/div/div/div/div/div/div[5]").getall()
        for i in metin:
            clearText = BeautifulSoup(i,"lxml").text
        with open("hackernews.json","a",encoding="UTF-8")as f:
                f.write(json.dumps({"baslik":baslik,"url":url,"metin":clearText},indent=2,ensure_ascii=False))
          
        yield {
            "baslik":baslik,
            "url":url,
            "metin":metin
        }