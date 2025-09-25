import scrapy

class HacknewsSpider(scrapy.Spider):
    name = "hacknews"
    start_urls = ["https://news.ycombinator.com/"]

    def parse(self, response):
        for rows in response.css('tr.athing'):
            yield {
                "title": rows.css('a::text').get(),
                "link": rows.css('span.titleline > a::attr(href)').get(),
                "score": rows.xpath('following-sibling::tr[1]//span[@class="score"]/text()').get(),
            }
        next_page = response.css('a.morelink::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)