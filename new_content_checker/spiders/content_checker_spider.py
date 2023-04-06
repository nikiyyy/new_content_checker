import scrapy
from ..items import NewContentCheckerItem


class CrawlSpider(scrapy.Spider):
    name = "nexusmods"
    allowed_domains = ["www.nexusmods.com"]
    start_urls = ["https://www.nexusmods.com/skyrimspecialedition/mods/categories/54/"]

    listings_css = [".tile-name a::attr(href)"]

    def parse(self, response):

        for product in response.css('.mod-tile'):
            yield {
                'brand' : 'test'
            }