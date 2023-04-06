import json
import scrapy

def file_reader(caller):
    with open('content.txt') as f:
        datafile = [json.loads(line) for line in f.readlines()]

    if caller == "url":
        return [i['url'] for i in datafile]
    return datafile


class CrawlSpider(scrapy.Spider):
    name = "content_checker"
    start_urls = file_reader("url")

    def parse(self, response):
        for site in file_reader(None):
            if site['url'] == response.url:
                img_selector = site['img_selector']
                container_selector = site['container_selector']
                break

        product = response.css(container_selector)[0]
        yield {product.css(img_selector).get() : response.url}
