import scrapy


class SrealitySpider(scrapy.Spider):
    name = "sreality"
    allowed_domains = ["sreality.cz"]
    start_urls = ["https://sreality.cz"]

    def parse(self, response):
        pass
