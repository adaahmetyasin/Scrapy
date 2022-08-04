import scrapy


class NewsSpider(scrapy.Spider):
    name = "news"
    file = open("news.json","a",encoding = "UTF-8")

    start_urls = [
        "https://siberbulten.com/"
    ]

    def parse(self, response):
        title = response.css("h2.thumb-title a ::text").extract()
        url = response.css("h2.thumb-title a ::attr(href)").extract()    
        ptitle = response.css("h2.post-title a ::text").extract()
        purl = response.css("h2.post-title a ::attr(href)").extract() 

        i=0
        while (i < len(title)):
            self.file.write("News' title: " + title[i] + "\n")
            self.file.write("News' url: " + url[i] + "\n")
        i += 1

        j=0
        while (j < len(ptitle)):

            self.file.write("News' title: " + ptitle[j] + "\n")
            self.file.write("News' url: " + purl[j] + "\n")

            j += 1
    


        self.file.close()    



