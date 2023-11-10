import scrapy


class QuotesSpider(scrapy.Spider):
    name = "prueba2"
    start_urls = [
        "https://quotes.toscrape.com/page/1/",
        "https://quotes.toscrape.com/page/2/",
    ]

    def parse(self, response):
        for prueba2 in response.css("div.quote"):
            yield {
                "text": prueba2.css("span.text::text").get(),
                "author": prueba2.css("small.author::text").get(),
                "tags": prueba2.css("div.tags a.tag::text").getall(),
            }