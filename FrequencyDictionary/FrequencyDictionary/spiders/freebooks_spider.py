import scrapy 
from scrapy.linkextractors import LinkExtractor


class QuotesSpider(scrapy.Spider):
    name = "ebooks"
    start_urls = ['https://novels80.com/to-kill-a-mockingbird/page-1-10023127.html']

    def parse(self,response):
        q = response.css('div.chapter-content').get()
        yield{
            'text': q
        }

        next_page = response.xpath('//*[@id="next_chap"]/@href').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)