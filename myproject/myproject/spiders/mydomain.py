# -*- coding: utf-8 -*-
import scrapy
from myproject.items import MyprojectItem

already_checked = []
# already_checked.append("https://twitter.com/snopes")
# already_checked.append("mailto:Insert address(es) here?subject=Automobile Urban Legends&body=I thought you might find the following article from snopes.com interesting: http://www.snopes.com/autos/autos.asp")

class MydomainSpider(scrapy.Spider):
    name = "mydomain"
    allowed_domains = ["snopes.com"]

    start_urls = [
        "http://www.snopes.com/info/whatsnew.asp"
    ]
    def parse(self, response):
        for href in  response.xpath('//a/@href'):
            # print href
            url = response.urljoin(href.extract())
            print url
            if 'http://www.snopes.com/autos/autos.asp' == str(url):
                already_checked.append(url)
                yield scrapy.Request(url, callback=self.parse_dir_contents)
            else:
                already_checked.append(url)



    def parse_dir_contents(self, response):
        for sel in response.xpath('//a/@href'):
            checker = True
            url = response.urljoin(sel.extract())
            print '\033[94m' + url + '\033[0m'
            for elem in already_checked:
                if url == elem :
                    checker = False
            if str(url)[0:28] != 'http://www.snopes.com/autos/':
                # print '\033[92m' +str(url)[0:33] +'\033[0m'
                already_checked.append(url)
                checker = False
            if checker :
                item = MyprojectItem()
                item['claim'] = url
                already_checked.append(url)
                yield scrapy.Request(url, callback = self.next_page_content)
                # yield item
            checker = False


    def next_page_content(self,response):
        for sel in response.xpath('//a/@href'):
            checker = True
            url = response.urljoin(sel.extract())
            # print '\033[94m' + url + '\033[0m'
            for elem in already_checked:
                if url == elem :
                    checker = False
            if str(url)[0:28] != 'http://www.snopes.com/autos/':
                # print '\033[92m' +str(url)[0:33] +'\033[0m'
                already_checked.append(url)
                checker = False
            if checker :
                item = MyprojectItem()
                item['claim'] = url
                already_checked.append(url)
                yield scrapy.Request(url, callback = self.next_article)
                # yield item
            checker = False



    def next_article(self,response):
        item = MyprojectItem()
        # item['status'] = response.xpath('//div[@class="article_text"]/table/tr/td/font/b/text()').extract()
        data_point = response.xpath('//font[b/text() = "Claim:"]/following-sibling::text()').extract()
        data =  "@@@ " + str(data_point) + " @@@" + "\n"
        # print data
        # f = open('122009572_computer', 'a')
        f = open('122009576_AUTOS','a')
        f.write(data)






    # def parse(self, response):
    #
    #         # item = MyprojectItem()
    #         # item['claim'] = response.xpath('//div[@class="article_text"]/text()').extract()
    #         # item['status'] = response.xpath('//div[@class="article_text"]/table/tr/td/font/b/text()').extract()
    #         # item['sourceA'] = response.xpath('//font/dl/dt/nobr/text()').extract()
    #         # item['sourceB'] = response.xpath('//font/dl/dd/nobr/text()').extract()
    #
    #         yield item
    # # def parse(self, response):
    # #     filename = response.url.split("/")[-2] + '.html'
    # #     with open(filename, 'wb') as f:
    # #         f.write(response.body)




# -*- coding: utf-8 -*-
# import scrapy
# from myproject.items import MyprojectItem
#
# already_checked = []
# already_checked.append("https://twitter.com/snopes")
# already_checked.append("mailto:Insert address(es) here?subject=Automobile Urban Legends&body=I thought you might find the following article from snopes.com interesting: http://www.snopes.com/autos/autos.asp")

# class MydomainSpider(scrapy.Spider):
#     name = "mydomain"
#     allowed_domains = ["snopes.com"]
#
#     start_urls = [
#         "http://www.snopes.com/info/whatsnew.asp"
#     ]
#     def parse(self, response):
#         for href in  response.xpath('//ul/li/a/@href'):
#             # print href
#
#             url = response.urljoin(href.extract())
#             if 'http://www.snopes.com/politics/politics.asp' == str(url):
#                 already_checked.append(url)
#                 yield scrapy.Request(url, callback=self.parse_dir_contents)
#             else:
#                 already_checked.append(url)
#
#
#
#     def parse_dir_contents(self, response):
#         for sel in response.xpath('//a/@href'):
#             checker = True
#             url = response.urljoin(sel.extract())
#             for elem in already_checked:
#                 if url == elem :
#
#                     checker = False
#
#             if str(url)[0:34] != 'http://www.snopes.com/politics/':
#                 already_checked.append(url)
#                 checker = False
#             if checker :
#                 item = MyprojectItem()
#                 item['claim'] = url
#                 already_checked.append(url)
#                 # yield scrapy.Request(url, callback = self.next_page_content)
#                 yield item
#             checker = False
