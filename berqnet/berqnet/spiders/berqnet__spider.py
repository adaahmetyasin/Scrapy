
from urllib.parse import urljoin
import scrapy
import json
from bs4 import BeautifulSoup

class BerqnetSpider(scrapy.Spider):
    name = 'berqnet'
    allowed_domains = ['berqnet.com']
    start_urls = ['https://berqnet.com/blog/siber-guvenlik']
    #pagenumber=2
    unique_data=set()
    
          
   

    def parse(self, response):
     div=response.xpath("//html/body/div[2]/section/div/article/div[2]/div/div[2]/div[1]/div/div")
     
    
     for x in div:
      baslik=x.xpath("./div/b/a/text()").get()
      url="https://berqnet.com" + x.xpath("./div/b/a/@href").get()
         
      if baslik not in self.unique_data :
        self.unique_data.add(baslik)
      yield scrapy.Request(url,callback=self.parse_detail,meta={"baslik":baslik,"url":url})
    
    
    
    #  pagenumber=2
    #  next_page='https://berqnet.com/blog/siber-guvenlik?page='+str(pagenumber)
    #  if pagenumber <= 7:
    #      #pagenumber += 1
    #      Url=response.urljoin(next_page)
    #      pagenumber += 1
    #      yield scrapy.Request(url=Url, callback=self.parse)
    
     for next_page in response.css("div.pagination li a::text").extract():
            if next_page != 7:
                next_page = "https://berqnet.com/blog/siber-guvenlik?page=" + next_page
                yield scrapy.Request(url = next_page, callback = self.parse)

    def parse_detail(self,response):

        baslik=response.meta.get("baslik")
        url=response.meta.get("url")

        metin= response.xpath("//*[@id='main']/section/div/article/div[2]/div/div/div[1]/div/div[1]").getall()
        for i in metin:
            clearText = BeautifulSoup(i,"lxml").text
        with open("berqnet.json","a",encoding="UTF-8")as f:
                f.write(json.dumps({"baslik":baslik,"url":url,"metin":clearText},indent=2,ensure_ascii=False))
          
        yield {
            "baslik":baslik,
            "url":url,
            "metin":metin
        }