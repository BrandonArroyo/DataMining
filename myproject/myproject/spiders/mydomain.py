# -*- coding: utf-8 -*-
import scrapy
from myproject.items import MyprojectItem

class MydomainSpider(scrapy.Spider):
    name = "mydomain"
    allowed_domains = ["snopes.com"]
    start_urls = [
        "http://www.snopes.com/info/articles.asp"
    ]

    def parse(self, response):
        for sel in response.xpath('//ul/li'):#selection of the catagories
            item = MyprojectItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            yield item
