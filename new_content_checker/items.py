# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class NewContentCheckerItem(scrapy.Item):
    img = scrapy.Field()
    last_post_url = scrapy.Field()
    cur_page_url = scrapy.Field()
