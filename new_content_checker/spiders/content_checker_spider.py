import json
import scrapy

page_template ='<a href="{cur_url}"><img src="{page_url}"></a>'

def file_reader(caller):
    
    with open('content.txt') as f:
        datafile = [json.loads(line) for line in f.readlines()]

    if caller == "url":
        return [i['url'] for i in datafile]
    return datafile

def generate_html_page(crawl):
    with open("index.html", "w") as f:
        f.write('<link rel="stylesheet" href="styles.css">')
        for i in crawl.all_pages:
            print(i["img_url"])
            f.write(page_template.format(cur_url=i["cur_url"], page_url=i["img_url"]))


class CrawlSpider(scrapy.Spider):
    name = "content_checker"
    start_urls = file_reader("url")

    all_pages = []

    def parse(self, response):
        for site in file_reader(None):
            if site['url'] == response.url:
                img_selector = site['img_selector']
                container_selector = site['container_selector']
                break

        product = response.css(container_selector)[0]
        self.all_pages.append({"img_url":product.css(img_selector).get(), "cur_url":response.url})


    def __del__(self):
        generate_html_page(self)
        