import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    page_count = 1
    start_urls = [
        "https://www.kitapyurdu.com/index.php?route=product/best_sellers&list_id=16&filter_in_stock=1&filter_in_stock=1&page=1"
    ]

    def parse(self, response):
        book_names = response.css("div.name.ellipsis a span::text").extract()
        book_authors = response.css("div.author.compact.ellipsis a.alt::text").extract()
        book_publishers = response.css("div.publisher span a span::text").extract()

        i = 1
        while(i < len(book_names)):
            yield{
                "name" : book_names[i],
                "author" : book_authors[i],
                "publisher" : book_publishers[i]
            }
            i += 1