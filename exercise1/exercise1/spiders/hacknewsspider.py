import scrapy

class HacknewsSpider(scrapy.Spider):
    """
    Spider Scrapy pour extraire les articles depuis Hacker News.

    - URL de départ : https://news.ycombinator.com/
    - Données extraites pour chaque article :
        * title (str) : le titre de larticle
        * link (str) : le lien absolu de larticle
        * score (str) : le nombre de points (ex. '37 points')

    Le spider suit automatiquement la pagination via le bouton
    « More » jusquà la fin des pages disponibles.
    """
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