import scrapy
from sreality_scraper.items import SrealityItem

class SrealitySpider(scrapy.Spider):
    name = "sreality"
    allowed_domains = ["sreality.cz"]
    start_urls = ["https://www.sreality.cz/api/en/v2/estates?category_main_cb=1&category_type_cb=1&per_page=500"]

    custom_settings = {
        "ROBOTSTXT_OBEY": False,
    }

    def parse(self, response):
        resp = response.json()

        sreality_item = SrealityItem()
        for estate in resp["_embedded"]["estates"]:
            # yield {
            #     "title": estate["name"],
            #     "images": estate["_links"]["images"],
            # }
            sreality_item["title"] = estate["name"]
            sreality_item["images"] = estate["_links"]["images"]
            yield sreality_item