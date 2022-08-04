import scrapy


class BerqnetSpider(scrapy.Spider):
    name = "berqnet"
    file = open("titles.json","a",encoding = "UTF-8")
    file2 = open("urls.json","a",encoding = "UTF-8")
    start_urls =[
        "https://berqnet.com/blog/siber-guvenlik"
    ]

    def start_requests(self):
        url = "https://berqnet.com/blog/siber-guvenlik"
        yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):

        titles = response.css("div.text b a::text").extract()
        i=0
        while (i < len(titles)):
            self.file.write("title: " + titles[i] + "\n")
            #self.file2.write("https://berqnet.com/" + urls[i] + "\n")
            i += 1
        
        urls = response.css("div.text b a::attr(href)").extract()
        for url in urls:
            self.file2.write("https://berqnet.com/" + url + "\n")
        # for url in urls:
        #     full_link=f"{url}"
        #     self.file.write(full_link + "\n")

        for next_page in response.css("div.pagination li a::text").extract():
            if next_page != 7:
                next_page = "https://berqnet.com/blog/siber-guvenlik?page=" + next_page
                yield scrapy.Request(url = next_page, callback = self.parse)

        # for title in response.css("div.text b a::text").extract():
        #     yield{
        #         "title" : title
        #     }
        # for url in response.css("div.text b a::attr(href)").extract():
        #     url = "https://berqnet.com" + url
        #     yield{
        #         "url" : url
        #     }
