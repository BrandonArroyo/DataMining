# -*- coding: utf-8 -*-
import scrapy
from myproject.items import MyprojectItem

class MydomainSpider(scrapy.Spider):
    name = "mydomain"
    allowed_domains = ["snopes.com"]
    allowed_domains =["search.atomz.com"]
    start_urls = [
        "http://www.snopes.com/autos/hazards/sigalert.asp"
    ]

    def parse(self, response):
        # for sel in response.xpath('//ul/li'):#selection of the catagories
            item = MyprojectItem()
        #     item['title'] = sel.xpath('a/text()').extract()
        #     item['link'] =  sel.xpath('a/@href').extract()
        #     yield item

            item['content'] = response.xpath('//div[@class="article_text"]/text()').extract()
            yield item
    # def parse(self, response):
    #     filename = response.url.split("/")[-2] + '.html'
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
