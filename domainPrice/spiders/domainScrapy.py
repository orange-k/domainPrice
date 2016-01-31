#coding:utf-8
import scrapy
import sys

from scrapy.http import HtmlResponse

from domainPrice.items import DmozItem

class DmozSpider(scrapy.spiders.Spider):
    name = "dmoz"
    # allowed_domains = ["dmoz.org"]
    start_urls = [
        "https://www.4.cn/hotsale"
    ]

    def parse(self, response):
        domainFile = open('domainPriceList.txt','wb')
        nextPage = response.xpath("//li[@class='next']/a/@href").extract()[0]
        nextPageUrl = "https://www.4.cn/hotsale" + nextPage
        for i in range(1,99):
            index = "'r_" + str(i) + "'"
            domainName = response.xpath("//li[@id="+ index +"]//span[@class='domain']/a/text()").extract()[0]
            domainPrice = response.xpath("//li[@id="+ index +"]//span[@class='price']/text()").extract()[0]
            content = domainName + ":" +domainPrice
            domainFile.write(content)
        print(nextPageUrl)

        domainFile.close()

fileM = open('test.txt','wb')
fileM.write('dds')
fileM.close()
        # print(sel.xpath("//li[@id=list]/span[@class='domain']/a/text()").extract())