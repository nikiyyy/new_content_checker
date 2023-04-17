import json
import scrapy

page_template_old ='<a href="{cur_url}"><img src="{img_url}"></a>'
page_template_new ='<a href="{cur_url}"><img class="new" src="{img_url}"></a>'

def file_reader(caller):
    # opens the file with the websites that need to be scraped
    with open('content.txt') as f:
        datafile = [json.loads(line) for line in f.readlines()]

    # returns only the urls it need to visit 
    if caller == "url":
        return [i['url'] for i in datafile]
    return datafile #returns the urls and selectors

def generate_html_page(crawl):
    #opens old logs
    file = open('log.txt',mode='r')
    old_log = file.read()
    file.close()

    #generates html
    with open("index.html", "w") as f:
        f.write('<link rel="stylesheet" href="styles.css">')
        for i in crawl.all_pages:
            img = i["img_url"]
            if img in old_log:
                f.write(page_template_old.format(cur_url=i["cur_url"], img_url=img))
            else:
                f.write(page_template_new.format(cur_url=i["cur_url"], img_url=img))

    #generates new log file
    with open("log.txt", "w") as f:
        for i in crawl.all_pages:
            f.write(i["img_url"])


class CrawlSpider(scrapy.Spider):
    name = "content_checker"
    start_urls = file_reader("url")

    all_pages = []

    def parse(self, response):
        for site in file_reader(None):
            if site['url'] == response.url:
                img_selector = site['img_selector']
                container_selector = site['container_selector']
                break #exits loop after it gets the newest post 

        product = response.css(container_selector)[0]
        #holds the first image and url(newest post) from every site
        self.all_pages.append({"img_url":product.css(img_selector).get(), "cur_url":response.url})


    def __del__(self): #creates a html file with the scraped data
        generate_html_page(self)
        