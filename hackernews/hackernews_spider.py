import scrapy


class QuotesSpider(scrapy.Spider):
    name = "hackernews"
    file = open("titles.json","a",encoding = "UTF-8")
    file2 = open("urls.json","a",encoding = "UTF-8")
    start_urls =[
        "https://thehackernews.com/"
    ]
    page_count = 0
    def start_requests(self):
        url = "https://thehackernews.com/"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        titles = response.css("h2.home-title::text").getall()
        for title in titles:
            self.file.write(title + "\n")
        urls =response.css("a.story-link::attr(href)").getall()
        for url in urls:
            self.file2.write(url + "\n")
        
        self.page_count += 1
        while self.page_count < 25:
            next_page = response.xpath("//*[@id='Blog1_blog-pager-older-link']/@href").get()
            yield scrapy.Request(url = next_page, callback = self.parse)
            
